import os

class Tekst:

    def __init__(self, wejscie, wyjscie):
        self.wejscie = wejscie
        self.wyjscie = wyjscie
        self.tekst = ""
        self.linie = ""
        self.ustaw_poczatek_akapitu("<p>")
        self.czytaj()

    def czytaj(self):
        plik = ""
        wejscie = self.wejscie
        plik_istnieje = os.path.exists(wejscie)
        if plik_istnieje:
            plik = open(wejscie, "r")
            self.tekst = plik.readlines()
        return self.tekst

    def zamien(self):
        poczatek_akapitu = self.zwroc_poczatek_akapitu()
        linie =  poczatek_akapitu + """\n"""
        for linia in self.tekst:
            if linia == "\n":
                linia = """</p>
<p>
"""
            linie += linia
        linie += "</p>"
        self.linie = linie

    def ustaw_poczatek_akapitu(self, poczatek_akapitu):
        self.poczatek_akapitu = poczatek_akapitu

    def zwroc_poczatek_akapitu(self):
        return self.poczatek_akapitu

    def zwroc_linie(self):
        return self.linie
