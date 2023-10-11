## 🔶 Jeu du Pierre-Papier-Ciseaux
On va jouer un peu cette semaine en développant un petit jeu très simple 😉

👉 Le but du challenge est de développer le célèbre jeu [pierre-papier-ciseaux](https://fr.wikipedia.org/wiki/Pierre-papier-ciseaux), essayez de trouver un algorithme astucieux et un code simple, propre et efficace.

🔹 **Étapes**
1. Générer un choix aléatoire pour votre session de jeu : `pierre`, `papier `ou `ciseaux`
2. Demander au joueur d'écrire son choix entre 3 propositions : `pierre`, `papier `ou `ciseaux`
3. Afficher qui a gagné en dévoilant le choix aléatoire du point n°1

🔹 **Conditions**
- L'affichage, le prompt et la réponse seront affichées / écrites via la console.
- Le fonctionnement du jeu est simple : la pierre gagne sur les ciseaux, les ciseaux gagnent sur le papier, le papier gagne sur la pierre, deux éléments identiques donnent égalité.
- Toute les chaines de caractères, `pierre`, `papier `et `ciseaux `doivent être toujours entrés en minuscule, le joueur devra donc écrire correctement ces mots, sinon vous devrez lui demander de redéfinir son choix.
- S'il y a égalité, vous devrez relancer automatiquement votre programme (en regénérant un nouveau choix aléatoire pour la nouvelle session de jeu), jusqu'à ce qu'il y ait un gagnant à la partie.

🔹**Exemples**
- Le choix aléatoire donne `pierre` et le joueur a choisi `papier`-> **Vous avez gagné ! Le papier enveloppe la pierre**
- Le choix aléatoire donne `ciseaux` et le joueur a choisi `papier`-> **Vous avez perdu ! Les ciseaux coupent le papier**
- Le choix aléatoire donne `pierre` et le joueur a choisi `pierre`-> **Égalité ! Recommencez...**