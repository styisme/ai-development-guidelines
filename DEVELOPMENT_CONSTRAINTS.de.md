**🌐 Language：** [中文](DEVELOPMENT_CONSTRAINTS.md) | [English](DEVELOPMENT_CONSTRAINTS.en.md) | [日本語](DEVELOPMENT_CONSTRAINTS.ja.md) | [Español](DEVELOPMENT_CONSTRAINTS.es.md) | [Français](DEVELOPMENT_CONSTRAINTS.fr.md) | **Deutsch** | [한국어](DEVELOPMENT_CONSTRAINTS.ko.md) | [Русский](DEVELOPMENT_CONSTRAINTS.ru.md)

# Entwicklungsbeschränkungen & Vorlage für ehrliche Offenlegung

> Kopieren Sie diese Vorlage in Ihr Projekt und füllen Sie sie gemäß den tatsächlichen Bedingungen aus. Dieses Dokument erläutert die tatsächlichen Entwicklungsbedingungen und Verantwortungsgrenzen dieses Repositorys.

## I. Entwicklungsumgebung (Zutreffendes ankreuzen)

- [ ] Lokale IDE / SDK vorhanden, lokale Kompilierung möglich
- [ ] Lokale Diff-Tools vorhanden, zeilenweise Überprüfung möglich
- [ ] Lint / Unit-Tests können ausgeführt werden
- [ ] Standard-PR-Ablauf (fork → PR → review)
- [ ] **Verlässt sich ausschließlich auf Cloud-CI-Kompilierung (keine lokale Toolchain)**
- [ ] **Entwickelt ausschließlich auf Mobilgeräten / Smartwatches**
- [ ] **Direkter Push auf master (kein PR-Ablauf)**

> Nicht angekreuzte Punkte bedeuten, dass sie in diesem Repository **physisch nicht ausgeführt werden können**, nicht dass sie "ignoriert" wurden.

## II. Tatsächlich umgesetzte Mechanismen (Ankreuzen, was getan wurde)

### Offenlegung
- [ ] `AI_DISCLOSURE.md` wird bereitgestellt, um Umfang und Anteil der KI-Beteiligung zu erläutern
- [ ] Link zu dieser Datei oben im README
- [ ] Commit-Nachricht mit `[ai-assisted]` gekennzeichnet

### Hochriskante Funktionen
- [ ] Hochriskante Funktionen standardmäßig deaktiviert (auf Codeebene, nicht nur in der Dokumentation)
- [ ] Separater Warnabschnitt für hochriskante Funktionen (siehe `SECURITY.md` oder gleichwertig)
- [ ] Ausdrückliche zweite Bestätigung vor der Nutzung hochriskante Funktionen erforderlich

### Kontrollpunkte (Gates)
- [ ] **Veröffentlichung erst nach erfolgreicher CI-Kompilierung** (das einzige automatisierte Gate in diesem Projekt)
- [ ] Release-Artefakte haben Versionsnummern und Tags
- [ ] `CHANGELOG.md` zeichnet jede Änderung auf

### Tests
- [ ] **Tests auf echten Geräten** (echte physische Geräte)
- [ ] **Emulator-Tests** (wenn keine physischen Geräte verfügbar sind)
- [ ] **Ungetestet** (siehe ehrliche Offenlegung unten)

> Nicht angekreuzte Punkte bedeuten, dass dieses Repository **keine Bedingungen hat, sie durchzuführen**, nicht dass es "vergessen" wurde.

## III. Ehrliche Offenlegung

**Die folgenden Situationen müssen wahrheitsgemäß dargestellt werden, ohne Beschönigung:**

- Wenn dieses Repository **keine Tests auf echten Geräten oder Emulatoren durchgeführt hat**, geben Sie dies hier klar an:
  > "Der Code in diesem Repository wurde nicht auf echten Geräten getestet. Eine erfolgreiche CI-Kompilierung bedeutet nur, dass Syntax und Abhängigkeiten korrekt sind, nicht dass die Funktionen funktionieren. Bitte bewerten Sie die Risiken selbst, bevor Sie es verwenden."

- Wenn ein Modul **sensibel, aber nicht verifiziert** ist, markieren Sie es in der folgenden Liste als `⚠️ Nicht verifiziert`.

- Wenn eine Funktion **standardmäßig aktiviert** ist (was gegen das Prinzip "Hochrisiko standardmäßig aus" verstößt), geben Sie den Grund klar an.

## IV. Liste sensibler Module (Gemäß den tatsächlichen Bedingungen ausfüllen)

| Modul | Verifizierungsstatus |
|---|---|
| `{{Ihr Auth-Modul}}` | ✅ Echtes Gerät / ⚠️ Nur CI / ❌ Nicht verifiziert |
| `{{Ihr Dateisystem-Modul}}` | ✅ Echtes Gerät / ⚠️ Nur CI / ❌ Nicht verifiziert |
| `{{Ihr Protokollanalyse-Modul}}` | ✅ Echtes Gerät / ⚠️ Nur CI / ❌ Nicht verifiziert |
| `{{Ihr CI/CD-Release-Skript}}` | ✅ Echtes Gerät / ⚠️ Nur CI / ❌ Nicht verifiziert |

> Mit `❌ Nicht verifiziert` gekennzeichnete Module **sind nicht unbedingt unveröffentlichbar**, aber bitte bewerten Sie die Risiken vor der Verwendung.
