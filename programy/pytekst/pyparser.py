from pypliki import *

class PyParser:

    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.pypliki = PyPliki(sciezka)

    def ustaw_sciezke(self, sciezka):
        self.sciezka = sciezka

    def zwroc_sciezke(self):
        return self.sciezka

    def pobierz_strone(self):
        self.strona_internetowa = self.pypliki.wczytaj_plik()
        return self.strona_internetowa

    def pobierz_element(self, znacznik_poczatkowy, znacznik_koncowy):
        tekst = self.strona_internetowa
        poczatek = 0
        koniec = 0
        indeks_poczatkowy = tekst.find(znacznik_poczatkowy, poczatek)
        print("Indeks początkowy: " + str(indeks_poczatkowy))
        #res = [i for i in range(len(tekst)) if test_str.startswith(poczatek, i)]
