from cipher_text import SymmetricEncryption


def enter_integer() -> int:
    try:
        return int(input("Clé de chiffrement : "))
    except ValueError:
        print("ERREUR: veuillez saisir un nombre entier...")
        return enter_integer()


if __name__ == "__main__":
    method = ""
    while method not in ["c".upper(), "d".upper()]:
        method = input("(C)hiffrer ou (D)chiffrer - Votre choix : ").upper()

    decode = SymmetricEncryption(input("Expression à chiffrer ou déchiffrer : "), enter_integer())
    print(decode.encryption() if method == "C" else decode.decryption())
