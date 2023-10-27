import sqlite3
from re import findall

TEXT = """
Récemment, j'ai eu l'opportunité de rencontrer des entrepreneurs exceptionnels lors d'une conférence. Par exemple, j'ai 
été inspiré par l'histoire de M. Thomas Bernard, qui a démarré sa propre entreprise dans la Silicon Valley. Vous pouvez 
le contacter à l'adresse email thomas.b@alphamail.com ou au numéro suivant +33 1 12 34 56 78. Une autre personne 
fascinante était Mme Claire Martin, la fondatrice d'une startup technologique innovante. Elle est joignable à 
cmartin@betaInbox.org, son numéro de téléphone est le 09 01 23 45 67. Ensuite, il y avait monsieur Lucas Petit, un 
innovateur dans le domaine de la construction durable, contactable à lp@experimentalpost.net, son téléphone est le 
0890 12 34 56.

En parcourant mon ancien annuaire, je suis tombé sur quelques contacts intéressants. Par exemple, j'ai redécouvert le 
contact de Mlle Sophie Martin. Son numéro de téléphone est 07 89 01 23 45, et elle est facilement joignable à l'adresse 
sophie@prototypemail.com. Un autre contact noté était celui du Dr Lucas Dupont. Je me souviens avoir eu plusieurs 
discussions avec lui. Son numéro est 06 78 90 12 34 et son mail est drdupont@randomInbox.org. C'est fascinant de voir 
comment certains contacts peuvent rapidement nous rappeler des souvenirs passés.

Lors de notre dernière réunion, Madame Jennifer Laroche, joignable au 05.67.890.123 ou par e-mail à 
laroche@trialmail.net, a exprimé sa satisfaction concernant les avancées du projet. 
Elle a insisté sur la pertinence du feedback fourni par M. Sébastien Girard, qui peut être contacté au 0456789012 ou 
par email à sébastieng@demomail.org. De plus, notre consultante externe, mademoiselle Chloé Lefebvre, dont le numéro 
est le 03.45.67.89.01 et l'e-mail est lefebvre_chloé@testInbox.net, a fourni un rapport détaillé qui a été bien reçu 
par l'équipe.
"""


class ExtractContacts:
    mr_and_mrs = ("M.", "Mme", "monsieur", "Mlle", "Dr", "Madame", "mademoiselle")

    def __init__(self, text: str):
        self.text = text
        self.text_split = text.split()
        list_names, list_mails = self._extract_names_and_mails()
        self.all_contacts = list(zip(list_names, list_mails, self._extract_phone()))
        self.longest_name = self._longest(0)
        self.longest_mail = self._longest(1)
        self.longest_number = self._longest(2)

    def __str__(self):
        header = (f"{self._display_plain_line()}\n| {'Nom & Prénom'.center(self.longest_name)} "
                  f"| {'Mail'.center(self.longest_mail)} | {'Numéro'.center(self.longest_number)} "
                  f"|\n{self._display_plain_line()}\n")
        return f"{header}{self._all_contacts_in_db_and_strings()}{self._display_plain_line()}"

    def _all_contacts_in_db_and_strings(self) -> str:
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Contacts (NomPrénom TEXT, Mail TEXT, Numéro TEXT)")
        str_contacts = ""
        for contact in self.all_contacts:
            cursor.execute("INSERT INTO Contacts (NomPrénom, Mail, Numéro) VALUES (?, ?, ?)", contact)
            str_contacts += (f"| {contact[0]}{' ' * (self.longest_name - len(contact[0]))} "
                             f"| {contact[1]}{' ' * (self.longest_mail - len(contact[1]))} "
                             f"| {contact[2]}{' ' * (self.longest_number - len(contact[2]))} |\n")
        conn.commit()
        conn.close()
        return str_contacts

    def _extract_names_and_mails(self) -> tuple[list[str], list[str]]:
        names, mails = [], []
        for word in self.text_split:
            if word in self.mr_and_mrs:
                word_index = self.text_split.index(word)
                names.append(' '.join(self.text_split[word_index + 1:word_index + 3]).rstrip('.').rstrip(','))
            mails.append(word.rstrip('.').rstrip(',')) if "@" in word else ...
        return names, mails

    def _extract_phone(self) -> list[str]:
        list_numbers = findall(r'\d', self.text)
        list_numbers_phone, index = [], 0
        while index < len(list_numbers):
            term_index = 11 if list_numbers[index] == "3" else 10
            list_numbers_phone.append(self._format_phone_number("".join(list_numbers[index:index + term_index])))
            index += term_index
        return list_numbers_phone

    def _longest(self, index: int) -> int:
        return len(max([self.all_contacts[i][index] for i in range(len(self.all_contacts))], key=len))

    def _display_plain_line(self) -> str:
        return f"|{'-' * (self.longest_name + 2)}|{'-' * (self.longest_mail + 2)}|{'-' * (self.longest_number + 2)}|"

    @staticmethod
    def _format_phone_number(number: str) -> str:
        return f"{number[0:2]}.{number[2]}." + ".".join([number[i:i+2] for i in range(3, len(number), 2)]) \
            if len(number) == 11 else ".".join([number[i:i+2] for i in range(0, len(number), 2)])


if __name__ == '__main__':
    print(ExtractContacts(TEXT))
