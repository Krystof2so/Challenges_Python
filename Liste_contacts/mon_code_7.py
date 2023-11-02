class ExtractContacts:
    MR_AND_MRS = ("M.", "Mme", "monsieur", "Mlle", "Dr", "Madame", "mademoiselle")
    DB_KEYS = ("Nom & Prénom", "Mail", "Numéro")
    CODE_ZERO = "0"  # usage numéro en national

    def __init__(self, file):
        # Création de la base de données sous forme d'un dictionnaire :
        self._all_contacts = ExtractContacts._extract_all_datas(ExtractContacts._extract_txt(file))

    @staticmethod
    def _extract_txt(file) -> str:
        """Extraction du contenu du fichier texte sous forme de chaîne de caractères"""
        with open(file, "r", encoding="utf-8") as textfile:
            return textfile.read()

    @staticmethod
    def _format_phone_number(number: str) -> str:
        """Formatage selon que le numéro de téléphone comporte 11 ou 10 chiffres."""
        match number[0]:
            case ExtractContacts.CODE_ZERO:  # 10 chiffres : 0x.xx.xx.xx.xx (usage en national)
                return ".".join(number[i:i + 2] for i in range(0, len(number), 2))
            case _:  # 11 chiffres: xx.x.xx.xx.xx.xx (usage en international)
                return f"{number[0:2]}.{number[2]}." + ".".join(number[i:i + 2] for i in range(3, len(number), 2))

    @staticmethod
    def _extract_all_datas(text: str) -> dict:
        """Extraction des données : listes de nom, de mails, de numéros de téléphone dans un dictionnaire."""
        bdd = {key: [] for key in ExtractContacts.DB_KEYS}
        for index, word in enumerate(text.split()):
            if word in ExtractContacts.MR_AND_MRS:  # Pour les noms
                bdd[ExtractContacts.DB_KEYS[0]].append(' '.join(text.split()[index + 1:index + 3])[:-1])
            elif "@" in word:  # Pour les mails
                bdd[ExtractContacts.DB_KEYS[1]].append(word.rstrip('.').rstrip(','))
        # Pour les numéros de téléphone :
        list_numbers = [n for n in text if n.isdigit()]
        while list_numbers:
            term_index = 10 if list_numbers[0] == ExtractContacts.CODE_ZERO else 11
            bdd[ExtractContacts.DB_KEYS[2]].append(
                ExtractContacts._format_phone_number("".join(list_numbers[:term_index])))
            list_numbers = list_numbers[term_index:]
        return bdd

    def __str__(self):
        longest = [len(max(c, key=len))+2 for c in self._all_contacts.values()]
        # Création des diverses 'strings' nécessaires à la construction du tableau de données :
        line_str = "\n|" + "".join(f"{'-' * long}|" for long in longest)
        header = "\n|" + "".join(f"{key_db:^{long}}|" for key_db, long in zip(ExtractContacts.DB_KEYS, longest))
        contacts = "\n|" + "\n|".join("".join(f" {contact:<{long-1}}|" for contact, long in zip(infos, longest))
                                      for infos in zip(*self._all_contacts.values()))
        # Tableau complet avec les données :
        return "".join(t + line_str for t in [header, contacts])


if __name__ == '__main__':
    print(ExtractContacts("text.txt"))