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