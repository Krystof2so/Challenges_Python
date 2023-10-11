TEST_SENTENCES = {
    "encrypt": (("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", 12),
                ("La première machine programmable a été réalisé en 1801.", 3)),
    "decypher": (("Lag_eeelelm*_l_aa*ced_i*hnesn*", 5),
                 ("dctigosrn*", 2),
                 ("C_hnryh__r_e_o_e'uagèmiaeenlnnanenlespqvn_olospds_l__auecduet_prtcetstecoevsiàre", 5))
}


class SymmetricEncryption:

    def __init__(self, expression: str, key: int):
        self.expression, self.key = f"{expression} -> ", key
        # Liste de sous-chaînes extraites de 'expression', de 'key' caractères, avec '_' au lieu des espaces :
        self.cut_with_key = [expression.replace(" ", "_")[i:i + key] for i in range(0, len(expression), key)]
        # Longueur des sous-chaînes issues de la première étape de déchiffrement :
        self.substring_length = len(expression) // key
        # Liste des sous-chaînes extraites de 'expression', composées avec 'key' caractères (déchiffrement) :
        self.expression_cut = [expression[i:i+self.substring_length]
                               for i in range(0, len(expression), self.substring_length)]

    def encryption(self) -> str:
        # Ajout des '*', si nécessaires à la dernière sous-chaîne de la liste :
        self.cut_with_key[-1] += "*" * (self.key - len(self.cut_with_key[-1]))
        # Algorithme d'encryptage : double itération (sur chaque position de sous-chaîne et chaque sous-chaîne)
        # et construction de la nouvelle chaîne, caractère par caractère :
        return self.expression + ''.join(s[position] for position in range(self.key) for s in self.cut_with_key)

    def decryption(self) -> str:
        # Déchiffrement : deux itérations (sur la longueur de la sous-chaîne et sur la liste 'self.expression_cut' :
        return self.expression + "".join(self.expression_cut[s][long] for long in range(self.substring_length)
                                         for s in range(len(self.expression_cut))).replace("*", "").replace("_", " ")


if __name__ == "__main__":
    for k, v in TEST_SENTENCES.items():
        for it in range(len(v)):
            decode = SymmetricEncryption(*v[it])
            print(decode.encryption() if k == "encrypt" else decode.decryption())
