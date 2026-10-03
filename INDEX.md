# Context Loom – Index

Zentrale Navigation für die Repositories der Organisation **Context Loom** und die noch nicht ausgelagerten Themen in `_workbench`.

Der Index beschreibt Themen nur kurz. Fachliche Details und Arbeitsstände bleiben in den jeweils verlinkten Repositories und Dateien.

## Repositories

### Meta
- [`.github`](https://github.com/context-loom/.github) – organisationsweite Beschreibung und zentraler Index.
- [`_workbench`](https://github.com/context-loom/_workbench) – Werkbank für Recherche, Konzepte, frühe Lösungsansätze, Hilfsmittel und PoCs.

### AI und Software Engineering
- [`ai-local`](https://github.com/context-loom/ai-local) – lokale AI-Infrastruktur, Modell-Gateway, Compute und Agenten-Zielbild.
- [`ai-prompting-framework`](https://github.com/context-loom/ai-prompting-framework) – wiederverwendbare Prompt-, Recherche-, Klassifikations- und Scoring-Workflows.
- [`software-engineering-standards`](https://github.com/context-loom/software-engineering-standards) – gemeinsame Architektur-, Technologie-, UI-, Betriebs- und Coding-Standards.

### Dokumente, Zeichnungen, Qualität und IMS
- [`pdf-drawing-analysis`](https://github.com/context-loom/pdf-drawing-analysis) – automatische Analyse technischer PDF-Zeichnungen.
- [`pdf-review`](https://github.com/context-loom/pdf-review) – Annotation, Prüfung, Bewertung und Korrektur von PDF-Dokumenten.
- [`pdf-review-demo`](https://github.com/context-loom/pdf-review-demo) – reines Deploy-/Ausgabe-Repository der statischen PDF-Review-Demo.
- [`integrated-management-system`](https://github.com/context-loom/integrated-management-system) – maschinenlesbares IMS mit JSON als führendem Dokumentmodell.
- [`quality-analysis-toolbox`](https://github.com/context-loom/quality-analysis-toolbox) – Werkzeugkasten für Root-Cause- und Qualitätsanalysen.

### idPlan
- [`idPlan-dokumente-positionsbildung`](https://github.com/context-loom/idPlan-dokumente-positionsbildung) – Analyse und Positionsbildung aus idPlan-Dokumenten.
- [`idPlan-fit4future`](https://github.com/context-loom/idPlan-fit4future) – Architekturverständnis und schrittweise Modernisierung des Access-/VBA-Systems.
- [`idPlan-optimierung-angebot`](https://github.com/context-loom/idPlan-optimierung-angebot) – Standardisierung und Optimierung der Angebotserstellung.

### Infrastruktur und Integrationen
- [`logmon`](https://github.com/context-loom/logmon) – Logging- und Security-Monitoring mit rsyslog, Wazuh, WEF/WEC und angrenzenden Diensten.
- [`jira-sync`](https://github.com/context-loom/jira-sync) – read-only Jira-Cloud-Mirror mit lokalem Viewer.
- [`docker-frigate`](https://github.com/context-loom/docker-frigate) – lokales Frigate-Deployment für ereignisbasierte Videoüberwachung.
- [`start.fkm.local`](https://github.com/context-loom/start.fkm.local) – interne Browser-Startseite für Anwendungen und Dienste.

### Fachliche Anwendungen und Wissen
- [`HINWEISGEBERSYSTEM`](https://github.com/context-loom/HINWEISGEBERSYSTEM) – internes Hinweisgebersystem mit vertraulichem Workflow und Fristensteuerung.
- [`babtec`](https://github.com/context-loom/babtec) – Kontexte, Analysen und Werkzeuge rund um BabtecQ.
- [`fkm-sls-sales-onboarding`](https://github.com/context-loom/fkm-sls-sales-onboarding) – Wissensbasis und Einarbeitung für technische und wirtschaftliche SLS-Qualifizierung.

---

## Themen in `_workbench`

### 3D-Analyse
- [3D Feature Catalog](https://github.com/context-loom/_workbench/tree/main/3d-feature-catalog) – Merkmals- und Analysekatalog für 3D-Bauteile.
- [3D Analysis](https://github.com/context-loom/_workbench/tree/main/3d-analysis) – Geometrie-PoCs, derzeit insbesondere Wandstärke und Spaltmaß per Raycasting.

### AI, Research und Knowledge
- [Epistemic Diversity](https://github.com/context-loom/_workbench/blob/main/ai/knowledge-research/epistemic-diversity.md) – Claim Extraction, Meaning Classes, Entailment, Coverage und Diversität für Research/RAG.
- [Open Notebook](https://github.com/context-loom/_workbench/tree/main/ai/knowledge-research/open-notebook) – selbst gehostete Research-/Knowledge-Workspace-Schicht.

### Agenten und Tooling
- [NixOS Agent Worker PoC](https://github.com/context-loom/_workbench/tree/main/nixos-agent-worker-poc) – reproduzierbare Agent-Host-Umgebung.
- [Macro-/Micro-Orchestration](https://github.com/context-loom/_workbench/blob/main/ideas/agent-orchestration/macro-micro-orchestration.md) – Trennung von fachlicher Orchestrierung, Agent Coordination und Ausführung.
- [Agent Operations Layer](https://github.com/context-loom/_workbench/blob/main/ideas/agent-orchestration/agent-operations-layer.md) – Sessions, State, Messaging, Worktrees und Agent-Lifecycle.
- [OpenShell](https://github.com/context-loom/_workbench/blob/main/ideas/agent-runtime/openshell.md) – Kandidat für sichere Agent-Runtime und Policy-Grenzen.
- [Treg](https://github.com/context-loom/_workbench/blob/main/ideas/agent-tooling/treg.md) – Tool Registry, Credential Broker und Gateway.
- [Tool-Gateway-Vergleich](https://github.com/context-loom/_workbench/blob/main/ideas/agent-tooling/comparison-tool-gateways.md) – Treg, ToolHive, MCP-Gateway und Eigenbau.
- [Himalaya](https://github.com/context-loom/_workbench/blob/main/ideas/agent-tooling/himalaya.md) – CLI-Mailzugriff als Baustein für Agenten und Automationen.

### Knowledge Engineering
- [Knowledge Compiler](https://github.com/context-loom/_workbench/blob/main/ideas/knowledge-compiler.md) – Git-native Wissensverarbeitung: Source → Compile → Link → Lint → Query → Recompile.
- [Graphify](https://github.com/context-loom/_workbench/blob/main/ideas/repository-intelligence/graphify.md) – Repository-Knowledge-Graph für strukturierten Agent-Kontext.
- [Decision Models](https://github.com/context-loom/_workbench/tree/main/ideas/decision-models) – explizite Entscheidungsmodelle wie Jev-lite/OpenJev.

### Anwendungen und UI-Konzepte
- [Adaptive Spec Interview UI](https://github.com/context-loom/_workbench/blob/main/ideas/adaptive-spec-interview-ui.md) – von Idee und Entscheidungen über Spec bis Implementierung und Verifikation.
- [Generalized JSON Viewer/Editor](https://github.com/context-loom/_workbench/blob/main/ideas/generalized-json-viewer-editor.md) – konfigurierbare fachliche Oberfläche für strukturierte JSON-Dateien.
- [Document Signing](https://github.com/context-loom/_workbench/blob/main/ideas/document_signing.md) – Signatur-Orchestrierung mit Paperless-ngx, Zeichnungsordnung und Documenso.
- [Printer Management Microservice](https://github.com/context-loom/_workbench/blob/main/ideas/printer-management-microservice.adoc) – Verwaltung, Spooling und Status mehrerer Netzwerk-Labeldrucker.
- [Action Gateways](https://github.com/context-loom/_workbench/tree/main/www-actions-gateway) – kontrollierte Privilegiengrenze zwischen Webanwendungen und freigegebenen Systemaktionen.

### Referenzen und Technologiebeobachtung
- [Authentise](https://github.com/context-loom/_workbench/blob/main/ideas/authentise.md) – Referenzmuster für Digital Thread, Provenance und Engineering Context.
- [Heretic](https://github.com/context-loom/_workbench/blob/main/ideas/heretic.md) – Behavioral Model Editing mittels kontrastiver Aktivierungsanalyse.

### Betrieb und Hilfsmittel
- [Windows Server](https://github.com/context-loom/_workbench/tree/main/windows-server) – Windows-Server-Konzepte, Tests und Betriebsnotizen.
- [`cli/`](https://github.com/context-loom/_workbench/tree/main/cli) – wiederverwendbare CLI-Befehle für Linux, macOS und Windows.
- [`scripts/`](https://github.com/context-loom/_workbench/tree/main/scripts) – allgemeine Hilfsskripte.

## Pflegeprinzip

Neue Themen können in `_workbench` beginnen. Sobald ein Bereich dauerhaft eigenständig entwickelt, versioniert oder betrieben wird, wird er in ein eigenes Repository ausgelagert.

Der Index enthält nur **Kurzbeschreibung + Link**. Die verbindlichen operativen Regeln zur Indexpflege und zur Synchronisierung organisationsweiter Agentenregeln stehen in [`AGENTS.md`](./AGENTS.md).
