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

**Workbench:** [`context-loom/_workbench`](https://github.com/context-loom/_workbench)

Die sichtbaren Pfade sind relativ zum Root von `_workbench`.

### 3D-Analyse
- [`3d-feature-catalog/`](https://github.com/context-loom/_workbench/tree/main/3d-feature-catalog) — **3D Feature Catalog** – Merkmals- und Analysekatalog für 3D-Bauteile.
- [`3d-analysis/`](https://github.com/context-loom/_workbench/tree/main/3d-analysis) — **3D Analysis** – Geometrie-PoCs, derzeit insbesondere Wandstärke und Spaltmaß per Raycasting.

### AI Allgemein
- [`ai-allgemein/`](https://github.com/context-loom/_workbench/tree/main/ai-allgemein) — gemeinsame Klammer für Ergebnisse aus dem ChatGPT-Projekt **„ai-allgemein“**: AI-/Agenten-Architektur, Modelle, Research, Knowledge Engineering, Tooling und PoCs.

#### Agenten, Runtime und Tooling
- [`ai-allgemein/nixos-agent-worker-poc/`](https://github.com/context-loom/_workbench/tree/main/ai-allgemein/nixos-agent-worker-poc) — **NixOS Agent Worker PoC** – reproduzierbare Agent-Host-Umgebung.
- [`ai-allgemein/agent-orchestration/macro-micro-orchestration.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/agent-orchestration/macro-micro-orchestration.md) — **Macro-/Micro-Orchestration** – Trennung von fachlicher Orchestrierung, Agent Coordination und Ausführung.
- [`ai-allgemein/agent-orchestration/agent-operations-layer.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/agent-orchestration/agent-operations-layer.md) — **Agent Operations Layer** – Sessions, State, Messaging, Worktrees und Agent-Lifecycle.
- [`ai-allgemein/agent-runtime/openshell.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/agent-runtime/openshell.md) — **OpenShell** – Kandidat für sichere Agent-Runtime und Policy-Grenzen.
- [`ai-allgemein/agent-tooling/treg.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/agent-tooling/treg.md) — **Treg** – Tool Registry, Credential Broker und Gateway.
- [`ai-allgemein/agent-tooling/comparison-tool-gateways.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/agent-tooling/comparison-tool-gateways.md) — **Tool-Gateway-Vergleich** – Treg, ToolHive, MCP-Gateway und Eigenbau.
- [`ai-allgemein/agent-tooling/himalaya.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/agent-tooling/himalaya.md) — **Himalaya** – CLI-Mailzugriff als Baustein für Agenten und Automationen.

#### Models, Research und Knowledge Engineering
- [`ai-allgemein/decision-models/`](https://github.com/context-loom/_workbench/tree/main/ai-allgemein/decision-models) — **Decision Models** – lokale Decision Models / System-1-Modelle wie Jev-lite/OpenJev.
- [`ai-allgemein/knowledge-research/epistemic-diversity.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/knowledge-research/epistemic-diversity.md) — **Epistemic Diversity** – Claim Extraction, Meaning Classes, Entailment, Coverage und Diversität für Research/RAG.
- [`ai-allgemein/knowledge-research/open-notebook/`](https://github.com/context-loom/_workbench/tree/main/ai-allgemein/knowledge-research/open-notebook) — **Open Notebook** – selbst gehostete Research-/Knowledge-Workspace-Schicht.
- [`ai-allgemein/knowledge-compiler.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/knowledge-compiler.md) — **Knowledge Compiler** – Git-native Wissensverarbeitung: Source → Compile → Link → Lint → Query → Recompile.
- [`ai-allgemein/repository-intelligence/graphify.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/repository-intelligence/graphify.md) — **Graphify** – Repository-Knowledge-Graph für strukturierten Agent-Kontext.
- [`ai-allgemein/heretic.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/heretic.md) — **Heretic** – Behavioral Model Editing mittels kontrastiver Aktivierungsanalyse.

#### Übertragbare Anwendungen und Referenzen
- [`ai-allgemein/adaptive-spec-interview-ui.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/adaptive-spec-interview-ui.md) — **Adaptive Spec Interview UI** – von Idee und Entscheidungen über Spec bis Implementierung und Verifikation.
- [`ai-allgemein/authentise.md`](https://github.com/context-loom/_workbench/blob/main/ai-allgemein/authentise.md) — **Authentise** – Referenzmuster für Digital Thread, Provenance und Engineering Context.

### Compliance und Vorgaben
- [`compliance-traceability/`](https://github.com/context-loom/_workbench/tree/main/compliance-traceability) — **Compliance Traceability** – generisches Modell für Quellenstruktur, atomare Anforderungen, Umsetzungszuordnung, Nachweise und Abdeckungsanalyse.

### Weitere Ideen und Anwendungen
- [`ideas/generalized-json-viewer-editor.md`](https://github.com/context-loom/_workbench/blob/main/ideas/generalized-json-viewer-editor.md) — **Generalized JSON Viewer/Editor** – konfigurierbare fachliche Oberfläche für strukturierte JSON-Dateien.
- [`ideas/document_signing.md`](https://github.com/context-loom/_workbench/blob/main/ideas/document_signing.md) — **Document Signing** – Signatur-Orchestrierung mit Paperless-ngx, Zeichnungsordnung und Documenso.
- [`ideas/printer-management-microservice.adoc`](https://github.com/context-loom/_workbench/blob/main/ideas/printer-management-microservice.adoc) — **Printer Management Microservice** – Verwaltung, Spooling und Status mehrerer Netzwerk-Labeldrucker.
- [`www-actions-gateway/`](https://github.com/context-loom/_workbench/tree/main/www-actions-gateway) — **Action Gateways** – kontrollierte Privilegiengrenze zwischen Webanwendungen und freigegebenen Systemaktionen.

### Betrieb und Hilfsmittel
- [`windows-server/`](https://github.com/context-loom/_workbench/tree/main/windows-server) — **Windows Server** – Windows-Server-Konzepte, Tests und Betriebsnotizen.
- [`cli/`](https://github.com/context-loom/_workbench/tree/main/cli) – wiederverwendbare CLI-Befehle für Linux, macOS und Windows.
- [`scripts/`](https://github.com/context-loom/_workbench/tree/main/scripts) – allgemeine Hilfsskripte.

## Pflegeprinzip

Neue Themen können in `_workbench` beginnen. Sobald ein Bereich dauerhaft eigenständig entwickelt, versioniert oder betrieben wird, wird er in ein eigenes Repository ausgelagert.

Der Index enthält nur **Kurzbeschreibung + Link**. Die verbindlichen operativen Regeln zur Indexpflege und zur Synchronisierung organisationsweiter Agentenregeln stehen in [`AGENTS.md`](./AGENTS.md).
