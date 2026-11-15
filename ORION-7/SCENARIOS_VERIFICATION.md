# Scénarios de vérification fonctionnelle

Ces scénarios décrivent les **comportements** attendus et non une interface précise. Pour chaque scénario, indiquez dans le README comment vous l'avez vérifié.
Scénario 1 : Victoire

Récupérer le badge et le câble dans la réserve.
Aller au laboratoire en passant par le sas.
Récupérer le fusible et la bonbonne.
Utiliser la bonbonne et lire le journal.
Utiliser le badge pour ouvrir les machines.
Installer le câble et le fusible.
Saisir le code 4729.
Aller dans la salle de commande et évacuer.
Résultat attendu : victoire avec 25 unités d'oxygène restantes.

Scénario 2 : Défaite

Lancer une nouvelle partie.
Sélectionner 10 fois le choix 8 pour attendre.
Résultat attendu : l'oxygène atteint zéro et la partie se termine par une défaite.

Scénario 3 : Passage verrouillé

Aller dans le laboratoire.
Essayer d'accéder aux machines sans utiliser le badge.
Résultat attendu : le déplacement est refusé et aucun oxygène supplémentaire n'est consommé.

Scénario 4 : Code incorrect
Installer le câble et le fusible dans les machines.
Saisir le code 1234.
Résultat attendu : le réacteur reste éteint et le joueur perd 3 unités d'oxygène.

Scénario 5 : Objet déjà ramassé

Aller dans la réserve.
Ramasser deux fois le badge.
Résultat attendu : le deuxième ramassage est refusé et l'oxygène reste inchangé.

Scénario 6 : Utilisation de la bonbonne
Récupérer la bonbonne dans le laboratoire.
Utiliser la bonbonne deux fois.
Résultat attendu : la première utilisation recharge l'oxygène de 30 unités après un coût de 2 unités. La deuxième utilisation est refusée.

Scénario 7 : Réacteur incomplet
Aller dans les machines.
Saisir le bon code sans installer le câble et le fusible.
Résultat attendu : le réacteur ne démarre pas et aucun oxygène n'est consommé.

**Conseil :** Vous pouvez fournir vos propres tests automatiques, mais une démonstration reproductible des scénarios suffit pour ce devoir.
