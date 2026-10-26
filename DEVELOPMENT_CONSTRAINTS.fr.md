**🌐 Language：** [中文](DEVELOPMENT_CONSTRAINTS.md) | [English](DEVELOPMENT_CONSTRAINTS.en.md) | [日本語](DEVELOPMENT_CONSTRAINTS.ja.md) | [Español](DEVELOPMENT_CONSTRAINTS.es.md) | **Français** | [Deutsch](DEVELOPMENT_CONSTRAINTS.de.md) | [한국어](DEVELOPMENT_CONSTRAINTS.ko.md) | [Русский](DEVELOPMENT_CONSTRAINTS.ru.md)

---

# Contraintes de l'Environnement de Développement & Modèle de Divulgation Honnête

> Copiez ce modèle dans votre projet, cochez et remplissez selon les conditions réelles. Ce document explique les conditions réelles de développement et les limites de responsabilité de ce dépôt.

## I. Environnement de Développement (Cocher selon le cas)

- [ ] Dispose d'un IDE / SDK local, peut compiler localement
- [ ] Dispose d'outils diff locaux, peut réviser ligne par ligne
- [ ] Peut exécuter lint / tests unitaires
- [ ] Suit le flux de PR standard (fork → PR → review)
- [ ] **Dépend uniquement de la compilation CI cloud (pas de toolchain local)**
- [ ] **Développe uniquement sur mobile / montre connectée**
- [ ] **Push direct vers master (pas de flux de PR)**

> Les éléments non cochés signifient qu'il est **physiquement impossible de les exécuter dans ce dépôt**, et non qu'ils ont été "ignorés".

## II. Mécanismes Réellement Mis en Œuvre (Cocher ce qui a été fait)

### Divulgation
- [ ] Fournit `AI_DISCLOSURE.md` expliquant l'implication et le pourcentage de l'IA
- [ ] Lien vers ce fichier en haut du README
- [ ] Message de validation étiqueté `[ai-assisted]`

### Fonctionnalités à Haut Risque
- [ ] Fonctionnalités à haut risque désactivées par défaut (au niveau du code, pas seulement des documents)
- [ ] Section d'avertissement distincte pour les fonctionnalités à haut risque (voir `SECURITY.md` ou équivalent)
- [ ] Confirmation explicite requise avant d'utiliser des fonctionnalités à haut risque

### Portes (Gates)
- [ ] **Publication uniquement après validation de la compilation CI** (la seule porte automatisée de ce projet)
- [ ] Les artefacts de publication ont des numéros de version et des balises
- [ ] `CHANGELOG.md` enregistre chaque modification

### Tests
- [ ] **Tests sur appareil réel** (appareils physiques réels)
- [ ] **Tests sur émulateur** (lorsqu'aucun appareil physique n'est disponible)
- [ ] **Non testé** (voir la divulgation honnête ci-dessous)

> Les éléments non cochés signifient que **ce dépôt n'a pas les conditions pour le faire**, et non qu'il a "oublié de le faire".

## III. Divulgation Honnête

**Les situations suivantes doivent être déclarées avec honnêteté, sans enjolivement :**

- Si ce dépôt **n'a effectué aucun test sur appareil réel ou émulateur**, indiquez-le clairement ici :
  > "Le code de ce dépôt n'a pas été testé sur des appareils réels. La réussite de la compilation CI signifie uniquement que la syntaxe et les dépendances sont correctes, et non que les fonctionnalités fonctionnent. Veuillez évaluer les risques vous-même avant utilisation."

- Si un module est **sensible mais non vérifié**, marquez-le comme `⚠️ Non vérifié` dans la liste ci-dessous.

- Si une fonctionnalité est **activée par défaut** (violant le principe "haut risque désactivé par défaut"), indiquez clairement la raison.

## IV. Liste des Modules Sensibles (Remplir selon la situation réelle)

| Module | État de Vérification |
|---|---|
| `{{votre module d'authentification}}` | ✅ Appareil réel / ⚠️ CI uniquement / ❌ Non vérifié |
| `{{votre module de système de fichiers}}` | ✅ Appareil réel / ⚠️ CI uniquement / ❌ Non vérifié |
| `{{votre module d'analyse de protocole}}` | ✅ Appareil réel / ⚠️ CI uniquement / ❌ Non vérifié |
| `{{votre script de publication CI/CD}}` | ✅ Appareil réel / ⚠️ CI uniquement / ❌ Non vérifié |

> Les modules marqués `❌ Non vérifié` **ne sont pas nécessairement non publiables**, mais veuillez évaluer les risques avant utilisation.

## V. Nous admettons que ce n'est pas parfait

Les processus formels de PR, les révisions de code ligne par ligne et l'analyse statique locale **peuvent tous être absents** dans certains dépôts.

Nous assumons une **responsabilité substantielle** à travers "**Divulgation + Portes (ce que nous pouvons faire) + Désactivé par défaut**", plutôt que de prétendre remplir toutes les **responsabilités formelles**.

C'est un choix sous contraintes, pas un rejet des normes.
