## 🔶 Affichage digital 7 segments
Il faudra bien être à l'heure pour résoudre le challenge de cette semaine 😉

👉 Le but de ce challenge est de développer la fonction `digital_time()->str` qui retourne l'heure actuelle au format d'affichage [digital à 7 segments](https://fr.wikipedia.org/wiki/Affichage_%C3%A0_sept_segments).

🔹 **Étapes**
1. Transcrire les chiffres de 0 à 9 en 7 segments digitaux
2. Transcrire plusieurs chiffres à la suite sur une seule ligne
3. Afficher l'heure en la retranscrivant

🔹 **Conditions**
- L'affichage se fait via la console
- L'heure doit être affichée au format 24h.
- L'heure et les minutes sont séparées par deux points, le tout sur une même ligne d'affichage avec 2 espaces de séparation
- Le résultat de l'affichage de l'heure actuelle doit correspondre aux exemples ci-dessous à l'aide du caractère "#"
- Les 7 segments a, b, c, d, e, f, g sont les suivants :
```py
     a
     v 
    ####   
f-> #  # <- b
    #### <- g
e-> #  # <- c
    ####
     ^
     d
```
- Pour des raisons d'ergonomie et d'esthétisme, les segments se superposent et s'affichent de manière plus allongée, ainsi le chiffre 2 s'affichera
```py
             ####                        ##
                #                          #
comme ceci : ####   et pas comme cela :  ## 
             #                          #
             ####                        ##
```
🔹**Exemples**
- À 17h26, le résultat de `digital_time()` donne ->
```py
   #  ####     ####  ####
   #     #  #     #  #  
   #     #     ####  ####
   #     #  #  #     #  #
   #     #     ####  ####
```
- À 23h59, le résultat de `digital_time()` donne ->
```py
####  ####     ####  ####
   #     #  #  #     #  #
####  ####     ####  ####
#        #  #     #     #
####  ####     ####  ####
```
- À 4h08, le résultat de `digital_time()` donne ->
```py
      #  #     ####  ####
      #  #  #  #  #  #  #
      ####     #  #  ####
         #  #  #  #  #  #
         #     ####  ####
```