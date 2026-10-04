# Context Loom – Agent Instructions

Diese Datei ist die **kanonische Quelle für organisationsweite Agentenregeln** von Context Loom.

Wichtig: Eine `AGENTS.md` in diesem Repository wird von Agenten, die in einem anderen Repository arbeiten, nicht automatisch geerbt. Deshalb wird der markierte Shared-Block in die Root-`AGENTS.md` der einzelnen Repositories synchronisiert.

<!-- context-loom:shared:start -->
## Context Loom – gemeinsame Regeln

### Arbeitsmodell

- `_workbench` ist Eingang und Inkubator für Recherche, Konzepte, frühe fachliche Modelle, Experimente und PoCs.
- Ein Thema erhält ein eigenes Repository, sobald es dauerhaft eigenständig entwickelt, versioniert, betrieben oder organisatorisch klar getrennt wird.
- Detaildokumentation bleibt im fachlich zuständigen Repository bzw. Workbench-Dokument. Organisationsweite Übersichten duplizieren diese Inhalte nicht.

### Zentraler Index

Die zentrale Navigation liegt in:

`context-loom/.github/INDEX.md`

Prüfe bei Arbeiten in Context Loom **vor Abschluss jeder strukturellen Änderung**, ob der Index angepasst werden muss.

Eine Indexänderung ist insbesondere zu prüfen bei:

- neuem Repository;
- Umbenennung, Archivierung, Ersatz oder Entfernung eines Repositories;
- wesentlicher Änderung des Zwecks eines Repositories;
- neuem wesentlichem Thema in `_workbench`;
- Umbenennung, Verschiebung oder Entfernung eines indexierten Workbench-Themas;
- Auslagerung eines Workbench-Themas in ein eigenes Repository.

Regeln für Einträge:

- ein kurzer Satz zum **Zweck**, nicht zum tagesaktuellen Arbeitsstand;
- vorhandene fachliche Gruppe verwenden; neue Gruppen nur bei echtem Bedarf;
- keine Detaildokumentation in den Index kopieren;
- keine künstlichen Dubletten zwischen Workbench und eigenständigem Repository;
- bei Auslagerung den bisherigen Workbench-Eintrag entfernen oder sinnvoll auf das neue Repository überführen;
- Links und Namen bei strukturellen Änderungen mitprüfen.

Der Index soll **vollständig genug zum Entdecken, aber knapp genug als Inhaltsverzeichnis** bleiben.

### Änderungen an Agentenregeln

- Organisationsweite Regeln werden zuerst in `context-loom/.github/AGENTS.md` geändert.
- Der Shared-Block zwischen den Markern `context-loom:shared:start` und `context-loom:shared:end` wird anschließend in die Root-`AGENTS.md` der Context-Loom-Repositories synchronisiert.
- Repo-spezifische Regeln stehen **außerhalb** dieses verwalteten Blocks und dürfen bei der Synchronisierung nicht überschrieben werden.
- Wenn eine neue Regel nur ein Repository betrifft, gehört sie ausschließlich in dessen lokale `AGENTS.md`.

### Housekeeping

Für jede agentische Bearbeitung gelten zusätzlich die zentralen Aufräum- und Abschlussregeln in:

`context-loom/.github/housekeeping.md`

Vor Abschluss einer Änderung insbesondere Repository-Zustand, Bearbeitungsreste, obsolete oder doppelte Inhalte, Tests/Build, Dokumentation, Navigation und den vollständigen eigenen Diff prüfen.

### Allgemeine Hygiene

- Keine Zugangsdaten, Tokens, privaten Schlüssel oder produktiven Secrets committen.
- Bestehende fachliche Dokumentation und getroffene Architekturentscheidungen nicht ohne sachlichen Grund duplizieren oder widersprüchlich neu formulieren.
- Bei Umstrukturierungen Links und nahe liegende Navigationsdokumente mitprüfen.
<!-- context-loom:shared:end -->

## Pflege und Synchronisierung

Die lokalen Root-`AGENTS.md` enthalten eine synchronisierte Kopie des Shared-Blocks sowie darunter einen freien Abschnitt für repo-spezifische Regeln.

Für zukünftige Änderungen:

1. gemeinsame Regel hier ändern;
2. Shared-Block in alle betroffenen Repositories synchronisieren;
3. lokale Inhalte außerhalb des Blocks unverändert lassen;
4. Änderungen gemeinsam reviewen/committen.

Das Hilfsskript `scripts/sync-agents.py` unterstützt diesen Vorgang und läuft standardmäßig nur als Dry-Run.
