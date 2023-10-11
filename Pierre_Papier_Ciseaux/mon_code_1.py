import random

# VARIABLES
USER_WIN = "Vous avez gagné !"
EQUALITY = "Égalité ! Recommencez..."
USER_LOST = "Vous avez perdu !"

DICT_WITH_ALL_COMBINATIONS = {  # dict = objet: ((tuples possibles), message avec objet gagnant)
    "pierre": (
        (("pierre", "ciseaux"), ("ciseaux", "pierre")),
        "La pierre casse les ciseaux"),
    "papier": (
        (("papier", "pierre"), ("pierre", "papier")),
        "Le papier enveloppe la pierre"),
    "ciseaux": (
        (("ciseaux", "papier"), ("papier", "ciseaux")),
        "Les ciseaux coupent le papier")
}


# CLASS AND METHODS
class Chifoumi:
    def __init__(self, dict_game):
        self.dict_game = dict_game
        self.list_items = list(self.dict_game.keys())
        self.selected_items = self.item_user(), random.choice(self.list_items)
        self.winner_item = self.winning_item()

    def display_result(self) -> str or None:
        """Pour afficher le résultat. Méthode appelée pour l'exécution du code."""
        if not self.winner_item:
            return None  # Valuer qui permettra la continuité d'exécution
        final_msg = self.dict_game[self.winner_item][1]
        winner_is = USER_WIN if self.selected_items == self.dict_game[self.winner_item][0][0] else USER_LOST
        return (f"Vous: {self.selected_items[0]} - Machine: {self.selected_items[1]}"
                f"\n{winner_is} {final_msg}")  # True -> Fin d'exécution

    def item_user(self) -> str:
        """Pour le choix de l'utilisateur, avec gestion de l'erreur de saisie."""
        for i in self.list_items:
            print(f"- {i}")
        user_item = input("Votre choix : ")
        if user_item not in self.list_items:
            print("ERREUR DE SAISIE: Veuillez respecter orthographe et casse")
            return self.item_user()
        return user_item

    def winning_item(self) -> str or None:
        """Elément gagnant - Clé du dictionnaire."""
        for item in self.list_items:
            test_tuple = self.dict_game[item][0]
            if self.selected_items in test_tuple:
                return item
            return None


if __name__ == "__main__":
    while True:
        the_game = Chifoumi(DICT_WITH_ALL_COMBINATIONS)
        game = the_game.display_result()
        if game:
            print(game)
            break
        else:
            print(EQUALITY)

    print("\nTerminé...")
