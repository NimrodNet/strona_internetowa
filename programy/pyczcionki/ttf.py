from fontTools.ttLib import TTFont
import fontforge

class PyCzcionka:

    def __init__(self, zrodlo, cel):
        self.zrodlo = zrodlo
        self.cel = cel

    def ttf_to_otf(self):
        font = fontforge.open(self.zrodlo)
        font.generate(self.cel)

    def otf_to_woff2(self):
        czcionka = TTFont(self.zrodlo)
        czcionka.flavor='woff2'
        czcionka.save(self.cel)

zrodlo = '../../czcionki/roboto/Roboto-BlackItalic.ttf'
cel = '../../czcionki/roboto/black-italic.woff2'
ttf = Czcionka_ttf(zrodlo, cel)
ttf.ttf_to_otf()
