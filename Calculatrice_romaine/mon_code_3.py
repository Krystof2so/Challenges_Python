"""LA CALCULATRICE ROMAINE"""

import re

INTRO_MSG = "Veuillez saisir des chiffres romains à additionner\n(sous la forme : 'MCCCII+CCIV+VI' )"


class UsingRomanNumerals:
    DICT_ROMAN_ARABIC = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4
    }
    ERRORS_BECAUSE_LETTER_REPEATED = {4: ["I", "X", "C"], 2: ["V", "L", "D"]}  # {répétition max : liste lettres}

    def __init__(self, roman: str):
        self.list_roman_numbers = roman.split("+")
        # Deux définitions de validation des saisies de l'utilisateur (gestion des erreurs) qui seront évaluées :
        self.no_roman_number = self.if_roman_expression()
        self.too_many_letters = self.if_letter_repeated()

    def add_romans(self) -> bool or str:
        """
        Méthode appelée depuis le 'main'.
        1 - Vérification des saisies de l'utilisateur : retourne False si erreurs de saisie.
        2 - Réalise le calcul, en faisant appel à des méthodes de conversion : retourne le résultat
        sous la forme d'une chaîne de caractères (nombre romain calculé)
        """
        # Gestion des erreurs de saisie :
        if self.no_roman_number:  # Erreurs de saisie générale (si nombre romain n'en est pas un)
            print(self.no_roman_number)
            return False
        if self.too_many_letters:  # Certaines lettres sont trop répétées successivement
            print(f"Erreur: vous avez saisi trop de '{self.too_many_letters}' successifs...")
            return False
        if len(self.list_roman_numbers) == 1:  # L'utilisateur ne saisit qu'un seul nombre romain
            print(f"Erreur: veuillez saisir plus d'une valeur de façon à former une addition...")
            return False
        # Le calcul peut être réalisé, après la conversion des chiffres romains en nombres arabes :
        arabic_sum = sum(self.convert_roman_to_arabic(part) for part in self.list_roman_numbers)
        # Return après conversion nombre arabe vers chiffres romains :
        return self.convert_arabic_to_roman(arabic_sum)

    def convert_roman_to_arabic(self, roman_number: str) -> int:
        arabic_number = index = 0
        while index < len(roman_number):
            value_letter = self.DICT_ROMAN_ARABIC[roman_number[index]]
            try:  # Pour éviter d'aller trop loin dans l'index.
                value_letter_next = self.DICT_ROMAN_ARABIC[roman_number[index + 1]]
            except IndexError:
                return arabic_number + value_letter  # Une fois la dernière lettre évaluée
            if value_letter < value_letter_next:
                arabic_number += value_letter_next - value_letter
                index += 1  # Saut d'une lettre
            else:
                arabic_number += value_letter
            index += 1  # On passe à la lettre suivante
        return arabic_number

    def convert_arabic_to_roman(self, arabic: int) -> str:
        # Travailler avec le dictionnaire DICT_ROMAN_ARABIC_NUMERALS en inversant les clés et les valeurs :
        dict_arabic_roman_numerals = {value: key for key, value in self.DICT_ROMAN_ARABIC.items()}
        roman = []  # Contiendra les lettres romaines une fois converties depuis le nombre arabe.
        for arabic_value, roman_value in sorted(dict_arabic_roman_numerals.items(), reverse=True):
            while arabic >= arabic_value:
                roman += roman_value
                arabic -= arabic_value
        return ''.join(roman)  # Retour sous forme de chaîne de caractères, crée à partir d'une liste

    def if_roman_expression(self) -> str or None:
        """
        Deux gestions d'erreur de saisie par l'utilisateur :
        1 - L'utilisateur saisit une lettre qui ne fait partie des chiffres romains.
        2 - L'utilisateur saisit des lettres dans un ordre invalide. On procède par inversion des chiffres romains,
        pour faire comme si nous réalisions une soustraction, où l'on vérifie que la valeur suivante est inférieure
        à la précédente (Cf. lig. 'if value_letter < previous_value:')
        """
        for roman_number in self.list_roman_numbers:
            previous_value = 0  # Car n'y a pas de valeur précédente à comparer
            for letter in roman_number[::-1]:
                value_letter = self.DICT_ROMAN_ARABIC.get(letter, 0)
                if value_letter == 0:  # 1er cas d'erreur (avec des lettres non valides)
                    return f"Erreur: '{letter}' n'est pas un chiffre romain valide dans '{roman_number}'..."
                if value_letter < previous_value:  # 2e cas d'erreur (Soustraction V - X (5 -10) impossible
                    return (f"Erreur: '{letter}' ne peut pas être placé avant"
                            f" '{roman_number[roman_number.index(letter) + 1]}' dans '{roman_number}'")
                previous_value = value_letter  # Lettre précédente prend la valeur de la lettre en cours

    def if_letter_repeated(self) -> str or None:
        """
        Gestion d'erreurs de saisie : trop de lettres répétées.
        Utilise le module 're' (regex) à l'aide d'un dictionnaire répertoriant les différentes possibilités
        de saisies de lettres en trop.
        """
        for s in self.list_roman_numbers:
            for x in self.ERRORS_BECAUSE_LETTER_REPEATED[4]:
                # Recherche si le même caractère est présent au moins 4 fois consécutivement :
                if re.findall(rf'({re.escape(x)}){{4,}}', s):
                    return x  # Lettre en trop
            for x in self.ERRORS_BECAUSE_LETTER_REPEATED[2]:
                # Si deux fois consécutivement :
                if re.findall(rf'({re.escape(x)}){{2,}}', s):
                    return x


if __name__ == "__main__":
    print(INTRO_MSG)
    result = None
    while not result:
        result = UsingRomanNumerals(input("Votre saisie : ").replace(" ", "")).add_romans()
        print(result) if result else None
