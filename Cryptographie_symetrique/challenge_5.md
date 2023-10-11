## 🔶 Cryptographie symétrique
Un peu d'encryptage pour vos communications privées !

👉 Le but de ce challenge est de développer un codeur/décodeur suivant la logique de [cryptographie symétrique](https://fr.wikipedia.org/wiki/Cryptographie_sym%C3%A9trique) qui utilise une clef numérique très simple pour chiffrer et déchiffrer.

🔹 **Étapes**
1. Envoyer la phrase à chiffrer : `Salut, je suis ici pour apprendre Python` et la clef de codage : 6
2. On remplace d'abord tous les espace par des "_" -> `Salut,_je_suis_ici_pour_apprendre_Python`
3. Comme la clef est 6, on découpe la phrase en ligne de 6 caractères, les cases manquants sont comblés par des " * " :
```py
Salut,
_je_su
is_ici
_pour_
appren
dre_Py
thon**
```
4. On transpose en lisant le texte par colonne (de haut en bas et de gauche à droite) donc suivant cet ordre :
```py
1  8 15 22
2  9 16 23
3 10 17 24
4 11 18 25
5 12 19 26
6 13 20 27
7 14 21 28
```
La phrase chiffrée sera donc la suivante :
`S_i_adtajspprhle_opeou_iur_ntscreP*,ui_ny*`

**Pour le décodage, il suffira de suivre les étapes dans le sens inverse...**

🔹 **Conditions**
- L'affichage se fait via la console
- La phrase a chiffrer est a envoyer en argument, accompagnée de sa clef au format int, le résultat doit retourner la phrase codée
- Pour le décodeur, la phrase chiffrée est envoyée accompagnée de la clef, le résultat doit retourner la phrase en clair
- La clef doit être la même pour un même chiffrage et déchiffrage
- Vous êtes libre de coder en fonctionnel ou bien constituer vos classes en POO

🔹 **Exemples**
*Chiffrage*
- `Lorem ipsum dolor sit amet, consectetur adipiscing elit.` clef : 12 -> `Ldetnootugrl,r_eo__emrcal__odiisnitpisp.stei*u_cs*matc*_mei*`
- `La première machine programmable a été réalisé en 1801.` clef : 3 -> `Lpmrmherrmlatrlén8.arieai_oaae_ééi__0*_eè_cnpgmb_é_ase11*`

*Déchiffrage*
- `Lag_eeelelm*_l_aa*ced_i*hnesn*` clef : 5 -> `Le challenge de la semaine`
- `dctigosrn*` clef : 2 -> `docstring`