**🌐 Langue / Language：** [中文](README.md) | [English](README.en.md) | [日本語](README.ja.md) | [Español](README.es.md) | Français

> ⚠️ **Déclaration de Génération par l'IA**
> Ce document (y compris le texte de la spécification et le modèle) a été rédigé et généré par l'IA, et révisé par un humain. Nous montrons l'exemple en pratiquant les principes de transparence préconisés dans cette spécification.

---

# Directives de Développement par IA

### Une spécification pour divulguer, réviser et assumer la responsabilité du code généré par l'IA

## Table des Matières

- [Pourquoi cette spécification existe](#pourquoi-cette-spécification-existe)
- [Principes Directeurs](#principes-directeurs)
- [La Spécification](#la-spécification)
  - [1. Responsabilité](#1-responsabilité)
  - [2. Portée de l'utilisation](#2-portée-de-lutilisation)
  - [3. Génération et Révision](#3-génération-et-révision)
  - [4. Vérification](#4-vérification)
  - [5. Divulgation](#5-divulgation)
  - [6. Sécurité et Conformité](#6-sécurité-et-conformité)
  - [7. Documentation et Traçabilité](#7-documentation-et-traçabilité)
- [Modèle de Déclaration d'IA](#modèle-de-déclaration-dia)
- [FAQ](#faq)
- [Versionnage](#versionnage)
- [Adoption de cette Spécification](#adoption-de-cette-spécification)
- [Licence](#licence)

---

## Pourquoi cette spécification existe

L'IA peut désormais écrire du code qui compile, s'exécute et est livré. La question n'est plus de savoir *si* l'IA peut l'écrire, mais :

- Qui est **responsable** en cas de défaillance ;
- Quelles parties ont été générées et lesquelles ont été révisées — **personne ne peut le dire** ;
- Des fonctionnalités à haut risque se retrouvent en production parce que l'IA les a écrites — **personne ne les arrête** ;
- Les projets revendiquent un « développement assisté par l'IA » **sans norme de divulgation vérifiable**.

Cette spécification définit un ensemble minimal de conventions : **les humains possèdent les décisions et l'acceptation, l'IA génère, et le contenu généré doit être vérifiable, divulguable et accountable (responsable).**

Cette spécification ne classe pas les outils d'IA et n'impose pas de modèle spécifique.

---

## Principes Directeurs

1. **Les humains sont responsables.** L'IA n'est ni auteure ni partie responsable.
2. **Généré n'est pas synonyme d'utilisable.** Le code qui n'a pas été compilé, révisé et vérifié n'est pas terminé.
3. **La rigueur de la révision évolue avec le privilège.** Plus le code est proche de l'authentification, du système de fichiers, de l'exécution de commandes ou des pipelines de publication, plus la révision est stricte.
4. **Sécurisé et désactivé par défaut.** Les fonctionnalités à haut risque sont désactivées par défaut ; leur activation nécessite une confirmation explicite et un enregistrement.
5. **Divulguer honnêtement.** Écrivez « environ 80 % » plutôt que « entièrement généré par l'IA » sans offrir de piste de vérification.

---

## La Spécification

Les mots-clés **DOIT**, **DEVRAIT** et **PEUT** doivent être interprétés comme décrit dans la [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

### 1. Responsabilité

1.1 Un projet **DOIT** désigner au moins un mainteneur humain responsable des fusions et des versions.  
1.2 Les décisions de fusionner, publier, supprimer des données ou modifier des autorisations **DOIVENT** être prises par un humain et **NE DOIVENT PAS** être automatisées par l'IA.  
1.3 Un projet **DEVRAIT** indiquer dans sa documentation que l'IA participe à la génération tandis que les humains assurent l'acceptation.

### 2. Portée de l'utilisation

2.1 Les éléments suivants **PEUVENT** être générés directement par l'IA, sous réserve de compilation et de révision de base : code passe-partout, mises en page d'interface, styles, brouillons de documentation, commentaires, brouillons de tests et scripts de compilation.  
2.2 Les éléments suivants **DOIVENT** faire l'objet d'une révision humaine ligne par ligne : authentification et sessions, chiffrement et certificats, validation des chemins et du bac à sable, analyse de protocoles, exécution de commandes, migrations de bases de données, et secrets/scripts de publication CI/CD.  
2.3 Un projet **NE DOIT PAS** soumettre de secrets réels, certificats, jetons ou données utilisateur à des services d'IA publics.  
2.4 Les fonctionnalités à haut risque (accès root, accès au disque complet, exécution de commandes à distance, auto-destruction, tunneling, etc.) **NE DOIVENT PAS** être activées par défaut et **DOIVENT** être signalées séparément dans la documentation de sécurité.  
2.5 Un projet **NE DOIT PAS** surestimer ou sous-estimer son implication dans l'IA dans les documents de divulgation.

### 3. Génération et Révision

3.1 Chaque génération d'IA **DEVRAIT** être fondée sur un contexte explicite : objectifs, contraintes, plateforme cible, fichiers pertinents et journaux d'erreurs.  
3.2 Le code généré par l'IA **DOIT** être révisé par un humain avant d'atteindre la branche principale.  
3.3 La révision **DEVRAIT** couvrir au minimum : l'exactitude logique, la gestion des erreurs, la nécessité des dépendances, l'existence réelle des API de la plateforme et la compatibilité des licences.  
3.4 Les modifications générées volumineuses **DEVRAIENT** être validées séparément pour faciliter le suivi et le retour en arrière.  
3.5 Les messages de validation **PEUVENT** être étiquetés `ai-assisted`, ou la description de la PR **PEUT** indiquer l'étendue de l'implication de l'IA.

### 4. Vérification

4.1 Le code généré par l'IA **DOIT** compiler au moins une fois sur la plateforme cible.  
4.2 Les modifications impliquant des API de plateforme, des autorisations, l'interface utilisateur, la survie en arrière-plan ou la mise en réseau **DOIVENT** être vérifiées sur des appareils ou environnements réels.  
4.3 La logique de base (analyseurs, validation de chemin, authentification, téléchargements par morceaux, etc.) **DEVRAIT** avoir des tests reproductibles.  
4.4 « L'IA a dit que c'était bien » **NE** constitue **PAS** une vérification.  
4.5 Après un élagage, un portage ou une refactorisation, une régression complète **DEVRAIT** être effectuée.

### 5. Divulgation

5.1 Un projet **DEVRAIT** fournir un fichier de déclaration d'IA dans le référentiel (recommandé : `AI_DISCLOSURE.md`).  
5.2 La divulgation **DOIT** inclure : l'étendue de l'implication de l'IA, le travail effectué par les humains, les limites et risques connus, et les conditions de licence.  
5.3 La divulgation **DOIT** être mise à jour lorsque : l'implication change matériellement, un nouveau module à haut risque est ajouté, une nouvelle branche ou un port est créé, ou une version majeure est publiée.  
5.4 La divulgation **DEVRAIT** inclure une date de dernière mise à jour.  
5.5 Le fichier de divulgation **NE DOIT PAS** se substituer à la documentation de sécurité ; les fonctionnalités à haut risque **DOIVENT** être documentées séparément.

### 6. Sécurité et Conformité

6.1 Les secrets et certificats **DOIVENT** être injectés via des coffres-forts de secrets ou des variables d'environnement et **NE DOIVENT PAS** entrer dans le référentiel.  
6.2 Avant d'adopter une dépendance tierce suggérée par l'IA, un projet **DEVRAIT** évaluer sa licence, sa taille, son état de maintenance et ses antécédents en matière de sécurité.  
6.3 L'audio, les images et le texte générés **DOIVENT** porter un avis indiquant que les utilisateurs doivent se conformer aux conditions de service et aux exigences de droits d'auteur pertinentes.  
6.4 Les certificats auto-signés, les listes noires de chaînes et la validation côté client **NE DOIVENT PAS** être décrits comme « audités en matière de sécurité ».

### 7. Documentation et Traçabilité

7.1 La documentation **DEVRAIT** refléter fidèlement le code actuel et **NE DOIT PAS** décrire des fonctionnalités planifiées comme livrées.  
7.2 Le numéro de version **DEVRAIT** avoir une source de vérité unique (par exemple, `CHANGELOG.md`) injectée par CI.  
7.3 Les branches, éditions lite et ports **DOIVENT** documenter leur relation d'héritage avec l'upstream.  
7.4 Le Markdown généré par l'IA **DEVRAIT** être vérifié manuellement pour les noms de branches, les liens de référentiel et les chemins relatifs.

---

## Modèle de Déclaration d'IA

Les nouveaux projets peuvent copier ce qui suit dans `AI_DISCLOSURE.md` :

```markdown
# Déclaration d'IA

Ce projet ({{nom du projet}}) a utilisé de grands modèles de langage lors de {{développement/refactorisation/portage/élagage}}.

**Déclaration principale : environ {{pourcentage}} du code a été généré directement par l'IA ; les développeurs humains ont géré {{la définition du produit, la révision, les tests, l'acceptation et la publication}}.**

## Où l'IA a été impliquée
- `{{fichier ou module}}` : {{ce qui a été généré et pourquoi}}

## Ce que les humains ont fait
- {{exigences / décisions d'architecture / débogage de compilation / tests sur appareil / acceptation finale}}

## Limites Connues
1. {{L'IA ne peut pas s'exécuter sur du matériel réel ; les différences de plateforme nécessitent une vérification humaine}}
2. {{changements d'API de plateforme, cas extrêmes, risques de sécurité, etc.}}

## Licence
Ce projet est publié sous {{licence}}.
```

---

## FAQ

**Le pourcentage d'IA doit-il être exact ?**  
Non. Il doit être conservateur et honnête, et indiquer la base (par ligne, par module ou par fonctionnalité).

**Les petits projets ont-ils aussi besoin de divulgation ?**  
Recommandé. La divulgation est peu coûteuse ; ne pas pouvoir expliquer ce qui s'est passé est coûteux.

**Un humain peut-il être responsable sans écrire une seule ligne ?**  
Oui, à condition que l'humain ait effectué la définition des exigences, la révision, la vérification et les décisions de publication. La responsabilité vient des décisions et de l'acceptation, pas des frappes au clavier.

---

## Versionnage

Cette spécification suit le [Versionnage Sémantique](https://semver.org/lang/fr/) :

- **Majeure** : changements incompatibles des clauses ;
- **Mineure** : nouvelles clauses ou sections ;
- **Correctif** : clarifications de formulation et corrections de fautes de frappe.

Version actuelle : **1.0.0**

---

## Adoption de cette Spécification

Dans votre projet :

1. Copiez ce fichier dans `docs/AI-DEVELOPMENT-GUIDELINES.md` ;
2. Créez un lien vers celui-ci depuis `README.md` et `CONTRIBUTING.md` ;
3. Créez `AI_DISCLOSURE.md` en utilisant le [modèle](#modèle-de-déclaration-dia) ;
4. Ajoutez trois vérifications à votre modèle de PR : « implication de l'IA déclarée », « compilé sur la plateforme cible » et « code sensible à la sécurité révisé ».

---

## Licence

Cette spécification est publiée sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr). Vous pouvez la citer, la modifier et la redistribuer librement, à condition que l'attribution soit préservée.