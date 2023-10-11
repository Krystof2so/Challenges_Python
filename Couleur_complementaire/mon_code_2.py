"""
LES COULEURS

1 - Convertir une couleur au format hexadécimal aux formats RVB et TLS
2 - Indiquer la couleur complémentaire au format hexadécimal

Resources :
- https://fr.wikipedia.org/wiki/Teinte_saturation_luminosit%C3%A9
- https://fr.wikipedia.org/wiki/Teinte_Saturation_Valeur
- https://members.loria.fr/moberger/Enseignement/ENSG/representationCouleur.pdf
- Module 'colorsys' : https://github.com/python/cpython/blob/3.11/Lib/colorsys.py
"""

from colorsys import rgb_to_hls, hls_to_rgb

# Dictionnaire des couleurs : {'color_name': 'hex'}
COLORS_DICT = {
    'Vert': '#00ff00',
    'Rouge': '#ff0000',
    'Bleu': '#0000ff',
    'Violet': '#19021e',
}


class ColourConversion:

    def __init__(self, color_hex):
        self.color_hex = color_hex
        # Conversions RVB ('i' = index):
        self.rgb = [int(color_hex[i:i+2], 16) for i in range(1, len(color_hex), 2)]

    def get_color_types(self) -> dict:
        """
        Méthode appelée depuis le 'main' afin de lancer les conversions.
        À l'aide du module 'colorsys'
        """
        hls = list(rgb_to_hls(*[x/255 for x in self.rgb]))
        hls.insert(-1, hls.pop())  # Récupération de la dernière valeur de la liste est placée à l'index -1
        tsl_norm_str = (f"{round(hls[0]*360)}°", *[f"{el:.0%}" for el in hls[1:3]])
        return {'hex': self.color_hex, 'RVB': tuple(self.rgb),
                'tsl_norm': tsl_norm_str, 'tsl': tuple(hls)}

    @property
    def get_complementary(self) -> str:
        """Méthode appelée depuis le "main' pour obtenir la couleur complémentaire."""
        tsl = self.get_color_types()['tsl']
        # 180/360 = 1/2 = 0.5 - Le modulo permet de rester dans la norme [0-1]
        # Convertir le nouveau TSL au format RGB :
        r, g, b = hls_to_rgb(tsl[0] + .5 % 1, *tsl[2:0:-1])
        # Retour de la valeur hexadécimal de la couleur :
        return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255), int(b * 255))


if __name__ == "__main__":
    for color, hex_color in COLORS_DICT.items():
        conversion = ColourConversion(hex_color)
        print(f"{color} :\nLes différentes valeurs : {conversion.get_color_types()}\n"
              f"Couleur complémentaire : {conversion.get_complementary}\n")
