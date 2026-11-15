# MISSION ORION-7

**Étudiant(e) :** Olinga Timothee
**Date de remise :** dimanche 8 novembre 2026

## Objectif

Développer en autonomie un escape game spatial console en Python orienté objet.
Lire les PDF dans `../DOCUMENTATION_ETUDIANTS` avant de coder.

## Lancer le programme

```bash
python main.py
```

Remplacer ce texte par les consignes adaptées à **votre réalisation**.

## À compléter avant remise
Le projet est composé de plusieurs fichiers :
main.py : permet de lancer le jeu, d'afficher le menu et de récupérer les choix du joueur.
joueur.py : contient la classe Joueur, qui gère l'oxygène et l'inventaire.
salle.py : contient les classes Salle et Objet, qui représentent les pièces de la station et les objets disponibles.
enigme.py : contient les classes Enigme, EnigmeObjet et EnigmeCode.
station.py : contient la classe StationManager, qui gère les règles et le déroulement de la partie.
tests.py : contient les tests permettant de vérifier le fonctionnement du jeu.
REPONSES_POO_15_QUESTIONS.txt : contient les réponses aux questions sur la programmation orientée objet.
Et d'un senarios_Verfication etc

Joueur
Gérer l'oxygène et l'inventaire
Salle
Gérer les objets et les sorties
Objet
Représenter un objet
Enigme
Représenter la classe mère des énigmes
EnigmeObjet
Vérifier la possession d'un objet
EnigmeCode
Vérifier le code du réacteur
StationManager
Pour se déplacer dans la réserve :
Sélectionner le choix 3.
Écrire réserve.
Le joueur se déplace dans la réserve et perd 6 unités d'oxygène.
Pour récupérer le badge, sélectionner le choix 4 et écrire badge.

Le fichier tests.py utilise des assert pour vérifier :
Le niveau initial d'oxygène.
La capacité maximale de 80 unités.
L'impossibilité d'avoir un oxygène négatif.
Les déplacements interdits.
Le ramassage des objets.
L'impossibilité de ramasser deux fois le même objet.
L'utilisation unique de la bonbonne.
Le refus d'un code lorsque le réacteur est incomplet.
Le fonctionnement du code incorrect.
Les conditions de victoire et de défaite.
Pour exécuter les tests :
python tests.py
J'ai rencontré plusieurs difficultés pendant la réalisation du projet.
La première difficulté était de comprendre comment les classes communiquent entre elles et comment utiliser les instances.
J'ai également rencontré des erreurs d'indentation dans les conditions du menu.
Une autre erreur concernait l'appel des méthodes. J'avais oublié les parenthèses après station.observer et station.etat. Python affichait alors un message bound method au lieu du résultat attendu.
J'ai essayer de corrigé cette erreur en ajoutant les parenthèses. mais le terminal affiche quand meme une erreur et je ne comprend pas certain erreur
Le code du réacteur est toujours identique et la carte contient seulement cinq salles.
Une amélioration possible serait d'ajouter de nouvelles salles, des énigmes supplémentaires, une sauvegarde de la partie ou une interface graphique.
⚠️ Les propriétés et méthodes des classes **ne sont pas fournies** : elles font partie du travail évalué.
