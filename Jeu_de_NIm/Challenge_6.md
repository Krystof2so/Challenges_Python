## 🔶 Énoncé :
Mais qui va tomber sur le dernier ?

👉 Le but de ce challenge est de développer le jeu de [Nim](https://fr.wikipedia.org/wiki/Jeux_de_Nim), chaque joueur prend entre 1 et 3 bâtonnets à son tour, celui qui obtient le dernier à perdu.

🔹 **Étapes**
1. Afficher n bâtonnets sur une seule ligne
2. Gérer le jeu entre le joueur et le choix aléatoire de l'ordinateur.
**Bonus** : Développer une *IA* pour faire gagner l'ordinateur à tous les coups (en modifiant la fonction aléatoire)

🔹 **Conditions**
- L'affichage se fait via la console
- Un bâtonnet est affiché par " # " sur 3 lignes (voir l'exemple)
- Le jeu commence avec 20 bâtonnets
- Chaque joueur peut prendre au choix  entre 1 et 3 bâtonnets à la fois
- Afficher les bâtonnets restants à chaque tour
- Le joueur qui prend le dernier bâtonnet à perdu

🔹 **Exemple**
```
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
```
L'ordinateur en prend 3
```
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
```
Combien en prenez-vous ? `2`
```
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #
```
L'ordinateur en prend  1
```
#  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #  #  #  #
```
Combien en prenez-vous ? `3`
```
#  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #  #  #  #
```
L'ordinateur en prend 3
```
#  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #
#  #  #  #  #  #  #  #
```
Combien en prenez-vous ? `3`
```
#  #  #  #  #
#  #  #  #  #
#  #  #  #  #
```
L'ordinateur en prend 2
```
#  #  #
#  #  #
#  #  #
```
Combien en prenez-vous ?  `2`
```
#
#
#
```
Gagné !