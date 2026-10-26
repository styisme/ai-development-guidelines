**🌐 Language：** [中文](README.md) | [English](README.en.md) | [日本語](README.ja.md) | [Español](README.es.md) | [Français](README.fr.md) | **Deutsch** | [한국어](README.ko.md) | [Русский](README.ru.md)

> ⚠️ **KI-Generierungserklärung**
> Dieses Dokument (einschließlich Spezifikationstext und Vorlage) wurde von KI entworfen und generiert und von einem Menschen überprüft. Wir gehen mit gutem Beispiel voran und praktizieren die in dieser Spezifikation empfohlenen Transparenzprinzipien.

> 💡 **Entwicklungsbeschränkungen:** Wenn dieses Projekt aufgrund von Hardware- oder Umgebungsbeschränkungen keine vollständigen Tests durchführen kann, lesen Sie bitte [Entwicklungsbeschränkungen](DEVELOPMENT_CONSTRAINTS.de.md).

---

# KI-Entwicklungsrichtlinien

### Eine Spezifikation zur Offenlegung, Überprüfung und Verantwortung von KI-generiertem Code

## Inhaltsverzeichnis

- [Warum diese Spezifikation existiert](#warum-diese-spezifikation-existiert)
- [Leitprinzipien](#leitprinzipien)
- [Die Spezifikation](#die-spezifikation)
  - [1. Verantwortlichkeit](#1-verantwortlichkeit)
  - [2. Anwendungsbereich](#2-anwendungsbereich)
  - [3. Generierung und Überprüfung](#3-generierung-und-überprüfung)
  - [4. Verifizierung](#4-verifizierung)
  - [5. Offenlegung](#5-offenlegung)
  - [6. Sicherheit und Compliance](#6-sicherheit-und-compliance)
  - [7. Dokumentation und Rückverfolgbarkeit](#7-dokumentation-und-rückverfolgbarkeit)
- [KI-Offenlegungsvorlage](#ki-offenlegungsvorlage)
- [FAQ](#faq)
- [Versionierung](#versionierung)
- [Übernahme dieser Spezifikation](#übernahme-dieser-spezifikation)
- [Lizenz](#lizenz)

---

## Warum diese Spezifikation existiert

KI kann heute Code schreiben, der kompiliert, ausgeführt und ausgeliefert wird. Die Frage ist nicht mehr, *ob* KI ihn schreiben kann, sondern:

- Wer ist **verantwortlich**, wenn etwas kaputt geht;
- Welche Teile generiert und welche überprüft wurden — **niemand kann es sagen**;
- Hochriskante Funktionen in die Produktion gelangen, weil KI sie geschrieben hat — **niemand stoppt sie**;
- Projekte behaupten, "KI-unterstützte Entwicklung" zu betreiben, **ohne nachprüfbaren Offenlegungsstandard**.

Diese Spezifikation definiert eine minimale Reihe von Konventionen: **Menschen treffen Entscheidungen und akzeptieren Ergebnisse, KI generiert, und generierte Inhalte müssen nachprüfbar, offenlegbar und verantwortbar sein.**

---

## Die Spezifikation

Die Schlüsselwörter **MUSS**, **SOLLTE** und **KANN** sind gemäß [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) zu interpretieren.

### 1. Verantwortlichkeit

1.1 Ein Projekt **MUSS** mindestens einen menschlichen Maintainer benennen, der für Merges und Releases verantwortlich ist.  
1.2 Entscheidungen zum Mergen, Releasen, Löschen von Daten oder Ändern von Berechtigungen **MÜSSEN** von einem Menschen getroffen werden und **DÜRFEN NICHT** von KI automatisiert werden.  
1.3 Ein Projekt **SOLLTE** in seiner Dokumentation angeben, dass KI an der Generierung beteiligt ist, während Menschen die Abnahme vornehmen.

### 2. Anwendungsbereich

2.1 Folgendes **KANN** direkt von KI generiert werden, vorbehaltlich Kompilierung und grundlegender Überprüfung: Boilerplate, UI-Layouts, Styles, Dokumentationsentwürfe, Kommentare, Testentwürfe und Build-Skripte.  
2.2 Folgendes **MUSS** eine zeilenweise menschliche Überprüfung erhalten: Authentifizierung und Sitzungen, Verschlüsselung und Zertifikate, Pfad- und Sandbox-Validierung, Protokollanalyse, Befehlsausführung, Datenbankmigrationen sowie CI/CD-Secrets und Release-Skripte.  
2.3 Ein Projekt **DARF NICHT** echte Secrets, Zertifikate, Token oder Benutzerdaten an öffentliche KI-Dienste übermitteln.  
2.4 Hochriskante Funktionen (Root-Zugriff, Vollplattenzugriff, Remote-Befehlsausführung, Selbstzerstörung, Tunneling usw.) **DÜRFEN NICHT** standardmäßig aktiviert sein und **MÜSSEN** in der Sicherheitsdokumentation separat aufgeführt werden.  
2.5 Ein Projekt **DARF NICHT** seine KI-Beteiligung in Offenlegungsdokumenten über- oder untertreiben.

### 3. Generierung und Überprüfung

3.1 Jede KI-Generierung **SOLLTE** auf einem expliziten Kontext basieren: Ziele, Einschränkungen, Zielplattform, relevante Dateien und Fehlerprotokolle.  
3.2 KI-generierter Code **MUSS** von einem Menschen überprüft werden, bevor er den Hauptzweig erreicht.  
3.3 Die Überprüfung **SOLLTE** mindestens abdecken: logische Korrektheit, Fehlerbehandlung, Notwendigkeit von Abhängigkeiten, ob Plattform-APIs tatsächlich existieren, und Lizenzkompatibilität.  
3.4 Große generierte Änderungen **SOLLTEN** separat committet werden, um die Nachverfolgung und das Zurücksetzen zu erleichtern.  
3.5 Commit-Nachrichten **KÖNNEN** mit `ai-assisted` gekennzeichnet werden, oder die PR-Beschreibung **KANN** den Umfang der KI-Beteiligung angeben.

### 4. Verifizierung

4.1 KI-generierter Code **MUSS** mindestens einmal auf der Zielplattform kompilieren.  
4.2 Änderungen an Plattform-APIs, Berechtigungen, UI, Hintergrundüberleben oder Netzwerk **MÜSSEN** auf realen Geräten oder in realen Umgebungen verifiziert werden.  
4.3 Kernlogik (Parser, Pfadvalidierung, Authentifizierung, Chunked-Uploads usw.) **SOLLTE** wiederholbare Tests haben.  
4.4 "Die KI sagte, es sei in Ordnung" **stellt keine** Verifizierung dar.  
4.5 Nach Trimmen, Portieren oder Refactoring **SOLLTE** eine vollständige Regression durchgeführt werden.

### 5. Offenlegung

5.1 Ein Projekt **SOLLTE** eine KI-Offenlegungsdatei im Repository bereitstellen (empfohlen: `AI_DISCLOSURE.md`).  
5.2 Die Offenlegung **MUSS** enthalten: den Umfang der KI-Beteiligung, die von Menschen geleistete Arbeit, bekannte Einschränkungen und Risiken sowie Lizenzbedingungen.  
5.3 Die Offenlegung **MUSS** aktualisiert werden, wenn: sich die Beteiligung wesentlich ändert, ein neues hochriskantes Modul hinzugefügt wird, ein neuer Zweig oder Port erstellt wird oder eine Hauptversion veröffentlicht wird.  
5.4 Die Offenlegung **SOLLTE** ein Datum der letzten Aktualisierung enthalten.  
5.5 Die Offenlegungsdatei **DARF NICHT** die Sicherheitsdokumentation ersetzen; hochriskante Funktionen **MÜSSEN** separat dokumentiert werden.

### 6. Sicherheit und Compliance

6.1 Secrets und Zertifikate **MÜSSEN** über Secrets-Stores oder Umgebungsvariablen injiziert werden und **DÜRFEN NICHT** in das Repository gelangen.  
6.2 Bevor eine von KI vorgeschlagene Drittanbieter-Abhängigkeit übernommen wird, **SOLLTE** ein Projekt deren Lizenz, Größe, Wartungsstatus und Sicherheitsbilanz bewerten.  
6.3 Generiertes Audio, Bilder und Texte **MÜSSEN** einen Hinweis enthalten, dass Benutzer die entsprechenden Nutzungsbedingungen und Urheberrechtsanforderungen einhalten müssen.  
6.4 Selbstsignierte Zertifikate, String-Blacklists und clientseitige Validierung **DÜRFEN NICHT** als "sicherheitsgeprüft" bezeichnet werden.

### 7. Dokumentation und Rückverfolgbarkeit

7.1 Die Dokumentation **SOLLTE** den aktuellen Code genau widerspiegeln und **DARF NICHT** geplante Funktionen als ausgeliefert beschreiben.  
7.2 Die Versionsnummer **SOLLTE** eine einzige Quelle der Wahrheit haben (z. B. `CHANGELOG.md`), die von CI injiziert wird.  
7.3 Branches, Lite-Editionen und Ports **MÜSSEN** ihre Vererbungsbeziehung zum Upstream dokumentieren.  
7.4 KI-generiertes Markdown **SOLLTE** manuell auf Branch-Namen, Repository-Links und relative Pfade überprüft werden.

---

## KI-Offenlegungsvorlage

```markdown
# KI-Offenlegung

Dieses Projekt ({{Projektname}}) hat während {{Entwicklung/Refactoring/Portierung/Trimming}} große Sprachmodelle verwendet.

**Kernaussage: Etwa {{Prozentsatz}} des Codes wurde direkt von KI generiert; menschliche Entwickler übernahmen {{Produktdefinition, Überprüfung, Tests, Abnahme und Release}}.**

## Wo KI beteiligt war
- `{{Datei oder Modul}}`: {{was generiert wurde und warum}}

## Was Menschen getan haben
- {{Anforderungen / Architekturentscheidungen / Build-Debugging / Gerätetests / Endabnahme}}

## Bekannte Einschränkungen
1. {{KI kann nicht auf echter Hardware ausgeführt werden; Plattformunterschiede erfordern menschliche Verifizierung}}
2. {{Plattform-API-Änderungen, Randfälle, Sicherheitsrisiken usw.}}

## Lizenz
Dieses Projekt wird unter {{Lizenz}} veröffentlicht.
```

---

## Lizenz

Diese Spezifikation wird unter [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.de) veröffentlicht. Sie dürfen sie frei zitieren, ändern und weiterverbreiten, sofern die Namensnennung erhalten bleibt.
