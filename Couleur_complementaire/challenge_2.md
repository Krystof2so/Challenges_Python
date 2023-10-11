## 🔶 Couleur complémentaire
Nous allons jouer cette semaine avec les couleurs.

Ce n’est pas un sujet facile et cela va sûrement vous faire réfléchir 😉
Pour cette session j’ai choisi un niveau intermédiaire.
Les débutants pourront cependant résoudre la première étape en s’aidant de librairies.

👉 Le but de ce challenge est de trouver la [couleur complémentaire](https://fr.wikipedia.org/wiki/Couleur_compl%C3%A9mentaire#:~:text=Deux%20couleurs%20sont%20dites%20compl%C3%A9mentaires,%C3%A9chelle%20du%20noir%20au%20blanc.)

🔹 **Étapes**
1. Créez la fonction `get_color_types(color:str)->dict` qui permet de convertir le format RVB hexadécimal d’une couleur aux formats RVB décimal et [TSL (anglais : **H**ue**L**ight**S**aturation)](https://fr.wikipedia.org/wiki/Teinte_saturation_lumi%C3%A8re)

color : [string] la couleur RVB codé en hexadécimal, envoyée en paramètre
dict : [dict] contient le résultat de la conversion en différents styles d'écriture contenant les clés et valeurs suivantes :
- hex : [str] valeur hexadécimale de la couleur passée en paramètre
- rvb : [list] valeurs de chaque éléments RVB en décimal
- tsl_norm : [tuple] valeurs de chaque élément TSL (teinte en degrés 360°, saturation en % et luminosité en %)
- tsl : [tuple] valeurs de chaque élément TSL (teinte au format [0-1], saturation [0-1] (float) et luminosité [0-1] (float))

2. Afficher le contenu du dictionnaire retourné par cette fonction
3. Créez la fonction `get_complementary(color:str)->str` pour trouver la couleur complémentaire et qui retourne la couleur au format hexadécimal

🔹 **Conditions**
- L'affichage se fera via la console
- Les valeurs hexadécimales sont précédées de "#" et les lettres en minuscules

🔹**Exemple**
- get_color_types("#19021e") -> **{'hex': '#19021e', 'rvb': [25, 2, 30], 'tsl_norm': ('289°', '88%', '6%'), 'tsl': (0.8035714285714285, 0.875, 0.06274509803921569)}**
- get_complementary("#19021e") -> **"#071e02"**