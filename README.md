# Context Loom – Organisation und Vorgaben

Dieses Repository enthält die **organisationsweiten Meta-, Navigations- und Agentenvorgaben** für Context Loom.

Es ist die zentrale Stelle für Regeln und Übersichten, die nicht zu einem einzelnen Fach- oder Softwareprojekt gehören.

## Inhalte

- [`profile/README.md`](./profile/README.md) – kurzer öffentlicher Einstieg in die Organisation
- [`INDEX.md`](./INDEX.md) – zentraler Index aller Repositories und wesentlichen `_workbench`-Themen
- [`AGENTS.md`](./AGENTS.md) – kanonische organisationsweite Agentenregeln
- [`housekeeping.md`](./housekeeping.md) – laufende Housekeeping-Vorgaben für agentische Bearbeitung
- [`housekeeping-audit.md`](./housekeeping-audit.md) – Methode für Housekeeping Review und Repository-Audit
- [`scripts/sync-agents.py`](./scripts/sync-agents.py) – Synchronisierung der gemeinsamen Agenten- und Housekeeping-Vorgaben in die Repositories

## Verteilungsprinzip

Die kanonischen organisationsweiten Regeln werden **hier** gepflegt.

In den einzelnen Context-Loom-Repositories liegen lokale Arbeitskopien:

```text
<repo>/
├── AGENTS.md
└── .context-loom/
    ├── housekeeping.md
    └── housekeeping-audit.md
```

Der gemeinsam verwaltete Block in `AGENTS.md` sowie die beiden Dateien unter `.context-loom/` werden aus diesem Repository synchronisiert.

Repo-spezifische Regeln bleiben außerhalb des verwalteten Blocks in der jeweiligen lokalen `AGENTS.md`.

## Grundsatz

**Organisationsweite Vorgaben hier ändern, nicht in den synchronisierten Kopien der einzelnen Repositories.**

Details zur Pflege und Synchronisierung stehen in [`AGENTS.md`](./AGENTS.md).
