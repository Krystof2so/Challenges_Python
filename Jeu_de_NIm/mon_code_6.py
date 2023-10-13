from random import randint

MENU_GAME = (
    "Niveau 1",
    f"Niveau 2 (Impossible de gagner \U0001F606)"
)


def get_user_int_choice(question: str, min_choice: int, max_choice: int) -> int:
    while True:
        try:
            user_choice = int(input(question))
            if min_choice <= user_choice <= max_choice:
                return user_choice
        except ValueError:
            pass
        print(f"Erreur de saisie: veuillez saisir un nombre entier compris entre {min_choice} et {max_choice}")


def nim_game(perfect_ia: bool) -> str:
    sticks, number_of_laps = 20, 0
    while sticks > 0:
        number_of_laps += 1
        print(("# " * sticks + "\n") * 3)
        if number_of_laps % 2 == 0:  # Tour de jeu joueur
            sticks -= get_user_int_choice("Combien prenez-vous de bâtonnets ? ", *(1, 3))
        else:  # Tour de jeu ordinateur
            computer = randint(1, 3) if not perfect_ia else sticks - max(range(1, sticks, 4))
            print(f"L'ordinateur prend {computer} bâtonnet(s).")
            sticks -= computer
    return "Le joueur" if number_of_laps % 2 == 0 else "L'ordinateur"


if __name__ == "__main__":
    for item, game_choice in enumerate(MENU_GAME, start=1):
        print(f"\t[{item}] - {game_choice}")
    print(f"{nim_game(False if get_user_int_choice('Votre choix : ', *(1, 2)) == 1 else True)} perd...")
