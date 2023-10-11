from random import randint  # importation de random.randint

data = {
    "element": ["papier", "pierre", "ciseaux"],  # Rangement délibéré
    1: "Le papier enveloppe la pierre !",  # 0+1 ou 1+0
    2: "Les ciseaux coupent le papier !",  # 0+2 ou 2+0
    3: "La pierre casse les ciseaux !",  # 2+1 ou 1+2
    "winner": ["10", "21", "02"]}  # combinaisons gagnantes : 10 -> pierre contre papier etc...

# Boucle principale
while True:
    joueur = input("pierre, papier ou ciseaux: ")  # input du joueur
    if joueur in data["element"]:
        # le choix aleatoire -> choix, on utilise la fonction randint de random, un chiffre entre 0 et 2
        # l'entrée du joueur -> joueur, la recherche de l'index par rapport à la table data["element"]
        choix, joueur = randint(0, 2), data["element"].index(joueur)

        if choix != joueur:
            break  # pas d'égalité donc on sort de la boucle while
        print("Égalité, recommencez...")  # égalité, on reboucle pour tout recalculer
    else:
        print("Faute de frappe !")  # faute de frappe on reboucle

# On associe les deux chiffre d'index string pour connaître les choix de chacun et on en déduit qui gagne et
# perd par rapport à la liste data["winner"]
# affichage du gagnant et on révèle le choix aléatoire via la petite phrase sympa
print(f'Vous avez {"gagné" if (str(choix) + str(joueur)) in data["winner"] else "perdu"} ! {data[choix + joueur]}')
