#!/usr/bin/env python3
"""Synchronize Context Loom agent instructions and housekeeping guidance.

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

AGENTS_SOURCE = "AGENTS.md"
AGENTS_TARGET = "AGENTS.md"

MANAGED_FILES = {
    "housekeeping.md": ".context-loom/housekeeping.md",
    "housekeeping-audit.md": ".context-loom/housekeeping-audit.md",
}

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
    return content[start : end + len(END)]


def local_agents_skeleton(shared: str) -> str:
    return (
        "# Agent Instructions\n\n"
        "Der folgende Block wird aus `context-loom/.github/AGENTS.md` synchronisiert.\n"
        "Organisationsweite Regeln dort ändern, nicht in dieser Kopie.\n\n"
        f"{shared}\n\n"
        "## Repository-spezifische Regeln\n\n"
        "Derzeit keine zusätzlichen Regeln.\n"
    )


def merge_agents(existing: str, shared: str) -> str | None:
    start = existing.find(START)
    end = existing.find(END)

    if start < 0 and end < 0:
        return None
    if start < 0 or end < 0 or end < start:
        raise ValueError("unvollständige Shared-Marker")

    return existing[:start] + shared + existing[end + len(END) :]


def put_file(repo: str, path: str, content: str, sha: str | None, message: str) -> None:
    payload = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha

    gh_json(f"repos/{ORG}/{repo}/contents/{path}", method="PUT", payload=payload)


def plan_file(repo: str, target: str, desired: str) -> tuple[str, str | None] | None:
    existing = get_file(repo, target)
    if existing is None:
        return ("CREATE", None)
    if existing.content == desired:
        return None
    return ("UPDATE", existing.sha)


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

    source_agents = get_file(SOURCE_REPO, AGENTS_SOURCE)
    if source_agents is None:
        raise SystemExit(f"{ORG}/{SOURCE_REPO}/{AGENTS_SOURCE} nicht gefunden.")
    shared = extract_shared(source_agents.content)

    managed_sources: dict[str, str] = {}
    for source_path in MANAGED_FILES:
        source = get_file(SOURCE_REPO, source_path)
        if source is None:
            raise SystemExit(f"{ORG}/{SOURCE_REPO}/{source_path} nicht gefunden.")
        managed_sources[source_path] = source.content

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
        existing_agents = get_file(repo, AGENTS_TARGET)
        desired_agents = None
        agents_action = None

        if existing_agents is None:
            desired_agents = local_agents_skeleton(shared)
            agents_action = ("CREATE", None)
        else:
            try:
                merged_agents = merge_agents(existing_agents.content, shared)
            except ValueError as exc:
                print(f"MANUAL {repo}/{AGENTS_TARGET}: {exc}")
                manual += 1
            else:
                if merged_agents is None:
                    print(
                        f"MANUAL {repo}/{AGENTS_TARGET}: "
                        "bestehende Datei ohne Context-Loom-Marker"
                    )
                    manual += 1
                else:
                    desired_agents = merged_agents
                    if desired_agents != existing_agents.content:
                        agents_action = ("UPDATE", existing_agents.sha)

        if agents_action:
            changed += 1
            action, sha = agents_action
            if args.apply:
                put_file(
                    repo,
                    AGENTS_TARGET,
                    desired_agents,
                    sha,
                    "docs: sync Context Loom agent instructions",
                )
                print(f"{action:6} {repo}/{AGENTS_TARGET}")
            else:
                print(f"DRY-{action:6} {repo}/{AGENTS_TARGET}")
        elif desired_agents is not None:
            print(f"OK     {repo}/{AGENTS_TARGET}")

        for source_path, target_path in MANAGED_FILES.items():
            desired = managed_sources[source_path]
            planned = plan_file(repo, target_path, desired)

            if planned is None:
                print(f"OK     {repo}/{target_path}")
                continue

            changed += 1
            action, sha = planned
            if args.apply:
                put_file(
                    repo,
                    target_path,
                    desired,
                    sha,
                    "docs: sync Context Loom housekeeping guidance",
                )
                print(f"{action:6} {repo}/{target_path}")
            else:
                print(f"DRY-{action:6} {repo}/{target_path}")

    mode = "angewendet" if args.apply else "gefunden (Dry-Run)"
    print(f"\n{changed} Änderung(en) {mode}; {manual} manuelle Prüfung(en).")
    return 1 if manual else 0


if __name__ == "__main__":
    raise SystemExit(main())
