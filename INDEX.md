# Context Loom – Index

Zentrale Navigation für die Repositories der Organisation **Context Loom** und die noch nicht ausgelagerten Themen in `_workbench`.

Der Index beschreibt Themen nur kurz. Fachliche Details und Arbeitsstände bleiben in den jeweils verlinkten Repositories und Dateien.

## Repositories

### Meta
- [`.github`](https://github.com/context-loom/.github) – organisationsweite Beschreibung und zentraler Index.
- [`_workbench`](https://github.com/context-loom/_workbench) – Werkbank für Recherche, Konzepte, frühe Lösungsansätze, Hilfsmittel und PoCs.

### AI und Software Engineering
- [`ai-allgemein`](https://github.com/context-loom/ai-allgemein) – zentrale Ablage für allgemeine AI-/Agenten-Architektur, Research, Knowledge Engineering, Tooling und PoCs aus dem Projekt AI.Allgemein.
- [`ai-local`](https://github.com/context-loom/ai-local) – lokale AI-Infrastruktur, Modell-Gateway, Compute und Agenten-Zielbild.
- [`ai-prompting-framework`](https://github.com/context-loom/ai-prompting-framework) – wiederverwendbare Prompt-, Recherche-, Klassifikations- und Scoring-Workflows.
- [`software-engineering-standards`](https://github.com/context-loom/software-engineering-standards) – gemeinsame Architektur-, Technologie-, UI-, Betriebs- und Coding-Standards.

### Dokumente, Zeichnungen, Qualität und IMS
- [`pdf-drawing-analysis`](https://github.com/context-loom/pdf-drawing-analysis) – automatische Analyse technischer PDF-Zeichnungen.
- [`pdf-review`](https://github.com/context-loom/pdf-review) – Annotation, Prüfung, Bewertung und Korrektur von PDF-Dokumenten.
- [`pdf-review-demo`](https://github.com/context-loom/pdf-review-demo) – reines Deploy-/Ausgabe-Repository der statischen PDF-Review-Demo.
- [`integrated-management-system`](https://github.com/context-loom/integrated-management-system) – maschinenlesbares IMS mit JSON als führendem Dokumentmodell.
- [`bpmn-editor`](https://github.com/context-loom/bpmn-editor) – kollaborativer BPMN-Editor für Prozessmodellierung, Versionierung, Review und spätere IMS-/Workflow-Integration.
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
- [`fkm-central`](https://github.com/context-loom/fkm-central) – erweiterbare Stammdaten- und Katalogplattform für eigene Organisationen mit kontrollierten Beziehungen, Governance und konfigurierbaren CRUD-Ansichten.
- [`3d-feature-catalog`](https://github.com/context-loom/3d-feature-catalog) – Merkmals- und Analysekatalog für 3D-Druck-Bauteile, Geometrie-Features und nachgelagerte Bewertungsmodelle.
- [`compliance-traceability`](https://github.com/context-loom/compliance-traceability) – generisches Modell für Quellenstruktur, atomare Anforderungen, Umsetzungszuordnung, Nachweise und Abdeckungsanalyse.
  - [IDP – Intelligent Document Processing](https://github.com/context-loom/compliance-traceability/tree/main/IDP-Intelligent%20Document%20Processing) – Werkzeugvergleich für Dokumentstrukturierung, sinnerhaltende Anforderungsextraktion und Qualitätsprüfung.
- [`HINWEISGEBERSYSTEM`](https://github.com/context-loom/HINWEISGEBERSYSTEM) – internes Hinweisgebersystem mit vertraulichem Workflow und Fristensteuerung.
- [`babtec`](https://github.com/context-loom/babtec) – Kontexte, Analysen und Werkzeuge rund um BabtecQ.
- [`fkm-sls-sales-onboarding`](https://github.com/context-loom/fkm-sls-sales-onboarding) – Wissensbasis und Einarbeitung für technische und wirtschaftliche SLS-Qualifizierung.

---

## Themen in `_workbench`

**Workbench:** [`context-loom/_workbench`](https://github.com/context-loom/_workbench)

Die sichtbaren Pfade sind relativ zum Root von `_workbench`.

### 3D-Analyse
- [`3d-analysis/`](https://github.com/context-loom/_workbench/tree/main/3d-analysis) — **3D Analysis** – Geometrie-PoCs, derzeit insbesondere Wandstärke und Spaltmaß per Raycasting.

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
