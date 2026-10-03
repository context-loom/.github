#!/usr/bin/env python3
"""Synchronize the Context Loom shared AGENTS.md block across repositories.

Requires an authenticated GitHub CLI (`gh auth status`).

Default: dry-run.
Apply changes: python scripts/sync-agents.py --apply
Limit scope:   python scripts/sync-agents.py --repo pdf-review --repo logmon --apply
"""

from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
from dataclasses import dataclass

ORG = "context-loom"
SOURCE_REPO = ".github"
SOURCE_PATH = "AGENTS.md"
TARGET_PATH = "AGENTS.md"
START = "<!-- context-loom:shared:start -->"
END = "<!-- context-loom:shared:end -->"


@dataclass
class RemoteFile:
    content: str
    sha: str


def gh_json(path: str, *, method: str = "GET", payload: dict | None = None):
    cmd = ["gh", "api", path]
    if method != "GET":
        cmd += ["--method", method]
    try:
        if payload is None:
            run = subprocess.run(cmd, check=True, text=True, capture_output=True)
        else:
            cmd += ["--input", "-"]
            run = subprocess.run(
                cmd,
                check=True,
                text=True,
                input=json.dumps(payload),
                capture_output=True,
            )
    except FileNotFoundError:
        raise SystemExit("GitHub CLI 'gh' wurde nicht gefunden.")
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout).strip()
        raise RuntimeError(detail or f"gh api failed: {path}") from exc

    return json.loads(run.stdout) if run.stdout.strip() else None


def get_file(repo: str, path: str) -> RemoteFile | None:
    try:
        data = gh_json(f"repos/{ORG}/{repo}/contents/{path}")
    except RuntimeError as exc:
        if "404" in str(exc) or "Not Found" in str(exc):
            return None
        raise

    raw = base64.b64decode(data["content"]).decode("utf-8")
    return RemoteFile(raw, data["sha"])


def extract_shared(content: str) -> str:
    start = content.find(START)
    end = content.find(END)
    if start < 0 or end < 0 or end < start:
        raise SystemExit("Shared-Marker in der zentralen AGENTS.md fehlen oder sind ungültig.")
    end += len(END)
    return content[start:end]


def local_skeleton(shared: str) -> str:
    return (
        "# Agent Instructions\n\n"
        "Der folgende Block wird aus `context-loom/.github/AGENTS.md` synchronisiert.\n"
        "Organisationsweite Regeln dort ändern, nicht in dieser Kopie.\n\n"
        f"{shared}\n\n"
        "## Repository-spezifische Regeln\n\n"
        "Derzeit keine zusätzlichen Regeln.\n"
    )


def merge_existing(existing: str, shared: str) -> str | None:
    start = existing.find(START)
    end = existing.find(END)

    if start < 0 and end < 0:
        return None
    if start < 0 or end < 0 or end < start:
        raise ValueError("unvollständige Shared-Marker")

    end += len(END)
    return existing[:start] + shared + existing[end:]


def put_file(repo: str, content: str, sha: str | None) -> None:
    payload = {
        "message": "docs: sync Context Loom agent instructions",
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    gh_json(f"repos/{ORG}/{repo}/contents/{TARGET_PATH}", method="PUT", payload=payload)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Änderungen tatsächlich schreiben")
    parser.add_argument(
        "--repo",
        action="append",
        default=[],
        help="Nur dieses Repository bearbeiten; mehrfach verwendbar",
    )
    parser.add_argument(
        "--include-archived",
        action="store_true",
        help="Auch archivierte Repositories berücksichtigen",
    )
    args = parser.parse_args()

    source = get_file(SOURCE_REPO, SOURCE_PATH)
    if source is None:
        raise SystemExit(f"{ORG}/{SOURCE_REPO}/{SOURCE_PATH} nicht gefunden.")
    shared = extract_shared(source.content)

    repos = gh_json(f"orgs/{ORG}/repos?per_page=100&type=all")
    names = []
    wanted = set(args.repo)

    for repo in repos:
        name = repo["name"]
        if name == SOURCE_REPO:
            continue
        if repo.get("archived") and not args.include_archived:
            continue
        if wanted and name not in wanted:
            continue
        names.append(name)

    if wanted:
        missing = sorted(wanted - set(names))
        if missing:
            print("Nicht gefunden/übersprungen: " + ", ".join(missing), file=sys.stderr)

    changed = 0
    manual = 0

    for repo in sorted(names, key=str.lower):
        existing = get_file(repo, TARGET_PATH)

        if existing is None:
            desired = local_skeleton(shared)
            action = "CREATE"
            sha = None
        else:
            try:
                desired = merge_existing(existing.content, shared)
            except ValueError as exc:
                print(f"MANUAL {repo}: {exc}")
                manual += 1
                continue

            if desired is None:
                print(f"MANUAL {repo}: bestehende AGENTS.md ohne Context-Loom-Marker")
                manual += 1
                continue
            if desired == existing.content:
                print(f"OK     {repo}")
                continue
            action = "UPDATE"
            sha = existing.sha

        changed += 1
        if args.apply:
            put_file(repo, desired, sha)
            print(f"{action:6} {repo}")
        else:
            print(f"DRY-{action:6} {repo}")

    mode = "angewendet" if args.apply else "gefunden (Dry-Run)"
    print(f"\n{changed} Änderung(en) {mode}; {manual} manuelle Prüfung(en).")
    return 1 if manual else 0


if __name__ == "__main__":
    raise SystemExit(main())
