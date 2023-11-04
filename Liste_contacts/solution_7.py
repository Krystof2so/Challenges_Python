"""Solution proposée par @bucdany
Pour des explications complètes et détaillées:
https://discord.com/channels/396825382009044994/1168757567200165940
"""
from re import compile

FILE = "text.txt"
REGEX = (compile(r) for r in (
        r'(?:monsieur|Madame|mademoiselle|Mme|Mlle|M.|Dr)\s((?:[A-Z]\w+\s?){2})',
        r'[\w\.]+@\w+\.\w{2,}',
        r'[+0]\d+'
        ))
PREFIX = ("monsieur", "Madame", "mademoiselle", "Mme", "Mlle", "M.", "Dr")
TITLE = ("Nom & Prénom", "Mail", "Numéro")


def printl(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\n|" + result, end="")
        return result
    return wrapper


def get_text(file: str) -> str:
    with open(file, encoding="utf8") as f_content:
        return f_content.read()


def format_tel(tel: str) -> str:
    tel_ = "".join(tel[i:i+2] + "." for i in range(0, len(tel), 2)).rstrip(".")
    return tel_[1:2] + tel_[3:1:-1] + tel_[4:] if tel_.startswith("+") else tel_


def extract_regex(txt: str) -> dict:
    return {t: next(REGEX).findall(txt) if i < 2 else list(map(format_tel, next(REGEX).findall("".join(
        t for t in txt if t not in " .")))) for i, t in enumerate(TITLE)}


def extract_no_regex(txt: str) -> dict:
    bdd = {k: [] for k in TITLE}

    txt_ = "".join(t for i, t in enumerate(txt) if t not in " ." or not txt[i-1].isdigit()).split()
    for j, l in enumerate(txt_):
        if l in PREFIX:
            bdd[TITLE[0]].append(" ".join(txt_[j+1:j+3])[:-1])
        elif "@" in l:
            bdd[TITLE[1]].append(l.rstrip(",").rstrip("."))
        elif any(n.isdigit() for n in l):
            bdd[TITLE[2]].append(format_tel(l[:12] if l.startswith("+") else l[:10]))
    return bdd


@printl
def t_title(*args):
    return "".join(f'{t:^{length}}|' for t, length in zip(TITLE, args[0]))


@printl
def t_sep_line(*args):
    return "".join(f'{"-"*length}|' for length in args[0])


@printl
def t_content(*args):
    return "\n|".join("".join(f" {el:<{length-1}}|" for el, length in zip(el_, args[0]))
                      for el_ in zip(*args[1].values()))


def show(bdd: dict) -> None:
    length = [len(max(bdd, key=len))+2 for bdd in bdd.values()]

    for text_function in [t_title, t_content]:
        text_function(length, bdd)
        t_sep_line(length)


if __name__ == "__main__":
    DATA = get_text(FILE)

    show(extract_regex(DATA))
    show(extract_no_regex(DATA))
