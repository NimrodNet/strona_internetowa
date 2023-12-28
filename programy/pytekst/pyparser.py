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

    def pobierz_indeksy_zakonczenia(self, znacznik):
        try:
            indeksy = self.pobierz_indeks(znacznik)
            dlugosc = len(znacznik)
            indeksy_zakonczenia = []
            for indeks in indeksy:
                indeks += dlugosc
                indeksy_zakonczenia.append(indeks)
            return indeksy_zakonczenia
        except:
            print("PyParser, pobierz_indeksy_zakonczenia(): nie można pobrać indeksów zakończenia.")

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

    def zwroc_zawartosc(self, znacznik_poczatkowy, znacznik_koncowy):
        strona = self.zwroc_strone()
        poczatek = self.pobierz_indeks(znacznik_poczatkowy)
        koniec = self.pobierz_indeks(znacznik_koncowy)
        poczatek = poczatek[0] + len(znacznik_poczatkowy)
        koniec = koniec[0]
        tytul = strona[poczatek:koniec]
        return tytul

    def zwroc_tytul(self):
        znacznik_poczatkowy = "<title>"
        znacznik_koncowy = "</title>"
        tytul = self.zwroc_zawartosc(znacznik_poczatkowy, znacznik_koncowy)
        return tytul

    def zwroc_tekst(self):
        znacznik_poczatkowy = "<tekst>"
        znacznik_koncowy = "</tekst>"
        tekst = self.zwroc_zawartosc(znacznik_poczatkowy, znacznik_koncowy)
        tekst = tekst.replace("<p>", "").replace("</p>", "")
        tekst = tekst.replace("<h1>", "").replace("</h1>", "")
        return tekst

    def zwroc_opis(self):
        try:
            tekst = self.zwroc_tekst()
            linie = tekst.splitlines(2)
            opis = linie[5].replace("\n", "")
            return opis
        except:
            print("pyparser.py, zwroc_opis(): nie można zwrócić opisu.")
