from pypliki import *

class PyParser:

    def __init__(self, sciezka):
        try:
            self.sciezka = sciezka
            self.pypliki = PyPliki(sciezka)
            self.pobierz_strone()
        except:
            print("PyParser, init(): nie można rozpocząć działania.")

    def ustaw_sciezke(self, sciezka):
        try:
            self.sciezka = str(sciezka)
        except:
            print("PyParser, ustaw_sciezke(sciezka): nie można ustawić ścieżki.")

    def zwroc_sciezke(self):
        return self.sciezka

    def pobierz_strone(self):
        self.strona_internetowa = self.pypliki.wczytaj_plik()
        return self.strona_internetowa

    def wyswietl_strone(self):
        print(self.strona_internetowa)

    def zwroc_strone(self):
        return str(self.strona_internetowa)

    def pobierz_indeks(self, znacznik):
        tekst = self.strona_internetowa
        poczatek = 0
        koniec = 0
        indeks = tekst.find(znacznik, poczatek)
        indeksy = []
        while indeks >= 0:
            indeksy.append(indeks)
            poczatek = indeks + 1
            indeks = tekst.find(znacznik, poczatek)
        return indeksy

    def wytnij(self, poczatek, koniec):
        tekst = self.strona_internetowa
        dlugosc = len(tekst)
        fragment = ""
        if poczatek >= 0 and koniec <= dlugosc:
            fragment = tekst[poczatek:koniec]
        return fragment

    def pobierz_fragmenty(self, znacznik_poczatkowy, znacznik_koncowy):
        indeksy_poczatkowe = self.pobierz_indeks(znacznik_poczatkowy)
        indeksy_koncowe = self.pobierz_indeks(znacznik_koncowy)
        iteracje = len(indeksy_poczatkowe)
        indeks = 0
        fragmenty = []
        while indeks < iteracje:
            poczatek = indeksy_poczatkowe[indeks]
            koniec = indeksy_koncowe[indeks] + len(znacznik_koncowy)
            indeks += 1
            fragment = self.wytnij(poczatek, koniec)
            fragmenty.append(fragment)
        return fragmenty

    def wstaw_fragment(self, fragment, indeks):
        tekst = self.strona_internetowa
        tekst = tekst[ : indeks] + fragment + tekst[indeks : ]
        self.strona_internetowa = tekst
