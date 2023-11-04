### Avec les *regex*
Ça se passe en une seule ligne `return ` :
```py
def extract_regex(txt: str)-> dict:
    return {t: next(REGEX).findall(txt) if i < 2 else \
               list(map(format_tel, next(REGEX).findall("".join(t for t in txt if t not in " .")))) \
            for i, t in enumerate(TITLE)}
```
les *regex* sont tout d'abord compilées puis utilisée avec` re.findall()` afin de pouvoir tout extraire d'un coup et éviter de surchager le code de boucles inutiles

La compilation se fait directement à la déclaration des constantes, via l'utilisation d'un simple générateur :
```py
REGEX = (compile(r) for r in (
             r'(?:monsieur|Madame|mademoiselle|Mme|Mlle|M.|Dr)\s((?:[A-Z]\w+\s?){2})',
             r'[\w.]+@\w+\.\w{2,}',
             r'[+0]\d+'))
```
Les **noms et prénoms** sont extraits par cette *regex* :
```r'(?:monsieur|Madame|mademoiselle|Mme|Mlle|M.|Dr)\s((?:[A-Z]\w+\s?){2})'```
- un premier bloc qui me permet de chercher la civilité de la personne : `(?:monsieur|Madame|mademoiselle|Mme|Mlle|M.|Dr)`
notez le `?:` qui permet d'utiliser des parenthèses associatives sans en extraire le contenu. Ainsi le resultat de la recherche n'enverra pas ces données
- le `\s` pour cherche un espace
- un jeu de parenthèses pour permettre d'extraire proprement les données et d'éviter aussi des répétitions dans la *regex* : ```((?:[A-Z]\w+\s?){2})```
Ainsi, on cherche ici ce pattern : `(?:[A-Z]\w+\s?){2}` qui est donc répété 2x via `{2}`
notez encore un `?` qui permet de définir un caractère optionnel, ici l'espace noté `\s` qui est présent entre les noms et prénoms mais pas à la fin de la chaine à extraire.
Avec `[A-Z]` on cherche une majuscule puis un mot avec `\w+` et finalement un espace `\s`
Encore une fois le `?:` permet d'éviter d'avoir des doublons dans le résultat de la *regex*

Les **emails** sont extrait grâce à cette *regex* :
```r'[\w.]+@\w+\.\w{2,}'```
- on cherche un mot pouvant contenir un point
- le caractère "@"
- un autre mot derrière
- un point
- un mot de 2 lettres minimum pour l'extension de l'adresse mail.

Pour finir l'extraction des **numéros de téléphone** se fait via cette *regex* :
```r'[+0]\d+'```
- on cherche le signe "+" ou le chiffre "0" [+0]
- suivi de plusieurs chiffres `\d+`

### Affichage
Là, c'est une grosse partie et je voudrais pour cela vous présenter, dans un but pédagogique, un peu les décorateurs qui ont leur importance en Python

L'affiche est géré par la fonction `show(bdd: dict)-> None` qui fait appel à 3 autres fonctions, chacune décorée de `@printl` :
```py
def printl(func):
    def wrapper(*args):
        result = func(*args)
        print("|" + result)
        return result
    return wrapper

...

@printl
def t_title(*args):
    return "".join(f'{t:^{length}}|' for t, length in zip(TITLE, args[0]))

@printl
def t_sep_line(*args):
    return "".join(f'{"-"*length}|' for length in args[0])

@printl
def t_content(*args):
    return "\n|".join("".join(f" {el:<{length-1}}|" for el, length in zip(el_, args[0])) for el_ in zip(*args[1].values()))

def show(bdd: dict)-> None:
    length = [len(max(bdd, key = len))+2 for bdd in bdd.values()]

    for text_function in [t_title, t_content]:
        text_function(length, bdd)
        t_sep_line(length)
```
En termes simples, un décorateur permet d'encapsuler une fonction, qu'il prend en paramètre, pour intégrer d'autres actions autour d'elle.
```py
def printl(func):
    def wrapper(*args):
        result = func(*args)
        print("|" + result)
        return result
    return wrapper
```
Ici, je fais simplement un `print("|" + result)`, cela me permet de simplifier la fonction ` show()` et les formatages des contenus du tableau

`*args` permet de récupérer les arguments de la fonction et si besoin de les utiliser dans le décorateur.
Ici j'affiche simplement ce que me renvoi les fonctions en ajoutant un` "|"` au tout début

On utilise les décorateur 1 ligne au-dessus des fonctions, Python s'occupe du reste 😉
```py
@printl
def t_title(*args):
    return "".join(f'{t:^{length}}|' for t, length in zip(TITLE, args[0]))
```
l'appel de cette fonction fait donc simplement cela :
```py
print("|" + "".join(f'{t:^{length}}|' for t, length in zip(TITLE, args[0])))
```
Ce serait donc équivalent à cela sans le décorateur :
```py
def t_title(length:list)-> None:
    print("|" + "".join(f'{t:^{l}}|' for t, l in zip(TITLE, length)))
```
Au passage, cette fonction réunie les titres avec la taille des colonnes grâce à la fonction `zip()` puis on centre le tout avec les fonctions de formatage de `fstring` ->  ` :^` (pour centrer)

Pour plus d'info, voici un lien pour mieux appréhender fstring : https://discord.com/channels/396825382009044994/1155460501409628230

La deuxième fonction pour les lignes de séparation fonctionne de la même façon :
```py
@printl
def t_sep_line(*args):
    return "".join(f'{"-"*length}|' for length in args[0])
```
On affiche des `"-"` en fonction de la taille des colonnes

Pour finir le contenu du tableau se faire par l'intermédiaire de 2 boucles et pour le coup 2x `zip()` (oui j'aime beaucoup les zip 😉 ) :
```py
@printl
def t_content(*args):
    return "\n|".join("".join(f" {el:<{length-1}}|" for el, length in zip(el_, args[0])) for el_ in zip(*args[1].values()))
```
- La première boucle :` for el_ in zip(*args[1].values())` permet de lire chaque ligne du contenu du tableau
- la deuxième, permet, comme dans la fonction des titres, de créer un tuple pour associer les tailles de colonnes du tableau
- Le formatage permet d'aligner à gauche : `:<` et ajoute des espaces pour bien formater les données dans les cases

Pour revenir à la fonction show() :
```py
def show(bdd: dict)-> None:
    length = [len(max(bdd, key = len))+2 for bdd in bdd.values()]

    for text_function in [t_title, t_content]:
        text_function(length, bdd)
        t_sep_line(length)
```
La taille de chaque colonne est calculé par l'intermédiaire de `max(..., key = len)` qui est très pratique pour éviter de faire encore des boucles, ainsi l'élément de la liste de taille la plus longue est alors directement renvoyée, et c'est la fonction `len()` qui permet de récupérer la taille en question.
`length `est donc une liste contenant la taille de chaque colonne du tableau.

Cette dernière fonctionnalité est un peu bonus pour éviter les répétition de la ligne séparatrice du tableau :
```py
    for text_function in [t_title, t_content]:
        text_function(length, bdd)
        t_sep_line(length)
```
J'itère donc sur les deux types d'éléments à ajouter dans le tableau : `t_title `et `t_content`, qui sont appelés avec les arguments `length `et `bdd`.

Puis après chaque type d'élément du tableau, une ligne séparatrice est ajoutée : `t_line`()
