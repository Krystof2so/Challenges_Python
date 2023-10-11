from datetime import datetime

# Définition des segments :
plain = "#" * 4
right = "   #"
left = "#   "
borders = "#  #"
sep = "  #  "
empty = " " * 5

# Les segments :
SET_SEGMENTS = (
    (plain, borders, borders, borders, plain),
    (right, right, right, right, right),
    (plain, right, plain, left, plain),
    (plain, right, plain, right, plain),
    (borders, borders, plain, right, right),
    (plain, left, plain, right, plain),
    (left, left, plain, borders, plain),
    (plain, right, right, right, right),
    (plain, borders, plain, borders, plain),
    (plain, borders, plain, right, right),
    (empty, empty, empty, empty, empty),
    (empty, sep, empty, sep, empty)
)

HOUR = datetime.now().strftime("%H:%M").lstrip("0").split(":")


def digit(el, row):
    digits = []
    if el == "h":
        digits = [f"{SET_SEGMENTS[10][row]}{SET_SEGMENTS[int(HOUR[0][0])][row]}"] if len(HOUR[0]) == 1 \
            else [f"{SET_SEGMENTS[int(HOUR[0][x])][row]}" for x in range(2)]
    elif el == "m":
        digits = [f"{SET_SEGMENTS[int(HOUR[1][x])][row]}" for x in range(2)]
    elif el == ":":
        digits = [f"{SET_SEGMENTS[11][row]}"]
    return "  ".join(digits)


def digital_time() -> str:
    return "\n".join(([f'{digit("h", row)}{digit(":", row)}{digit("m", row)}'
                       for row in range(len(SET_SEGMENTS[0]))]))


if __name__ == "__main__":
    print(digital_time())
