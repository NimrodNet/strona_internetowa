class Strona:

    def __init__(self, nazwa):
        self.ustaw_nazwe(nazwa)
        self.ustaw_kodowanie()
        self.ustaw_tytul("")
        self.ustaw_css("")
        self.ustaw_tresc("")
        self.ustaw_stopke("")

    def ustaw_kodowanie(self):
        self.kodowanie = """<meta charset="UTF-8">"""

    def ustaw_nazwe(self, nazwa):
        self.nazwa = nazwa + ".html"

    def ustaw_tytul(self, tytul):
        self.tytul = tytul

    def ustaw_css(self, css):
        self.css = css

    def ustaw_slowa_kluczowe(self, slowa_kluczowe):
        self.slowa_kluczowe = slowa_kluczowe

    def ustaw_naglowek(self, naglowek):
        self.naglowek = naglowek

    def ustaw_tresc(self, tresc):
        self.tresc = tresc

    def ustaw_stopke(self, stopka):
        self.stopka = stopka

    def dodaj_css(self, link):
        css = """        <link ref="stylesheet" href=\"""" + link + """\">\n"""
        self.css += css

    def generuj(self):
        self.strona = """<html>
    <head>
        """ + self.zwroc_kodowanie() + """
        """ + self.zwroc_tytul() + """
""" + self.zwroc_css() + """
    </head>
    <body>
        """ + self.zwroc_tresc() + """ 
        """ + self.zwroc_stopke() + """
    </body>
</html>"""

    def zwroc_nazwe(self):
        return self.nazwa

    def zwroc_kodowanie(self):
        return self.kodowanie

    def zwroc_tytul(self):
        tytul = ""
        tytul_istnieje = self.tytul
        if tytul_istnieje:
            tytul = """<title>""" + self.tytul + """</title>"""
        return tytul

    def zwroc_css(self):
        css = ""
        if self.css:
            css = self.css
        return css

    def zwroc_tresc(self):
        tresc = ""
        if self.tresc:
            tresc = self.tresc
        return tresc

    def zwroc_stopke(self):
        stopka = ""
        if self.stopka:
            stopka = self.stopka
        return stopka

    def zwroc_strone(self):
        return self.strona

    def zapisz(self, sciezka):
        sciezka = sciezka + ".html"
        plik = open(sciezka, "w")
        plik.write(self.zwroc_strone())
        plik.close()
