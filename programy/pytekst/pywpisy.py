from pystrony import *
from pyparser import *
from pypliki import *
from pyartykul import *
from pywpis import *
from datetime import datetime
import os

class PyWpisy:

    def __init__(self):
        try:
            self.sciezka = "/home/qwerty891/Pulpit/strona_internetowa/programy/pytekst/"
            self.sciezka_wejsciowa = self.sciezka + "wejscie/"
            self.sciezka_wyjsciowa = self.sciezka + "wyjscie/"
            self.sciezka_strony_glownej = self.sciezka + "index.html"
            self.pyparser = PyParser(self.sciezka_strony_glownej)
        except:
            print("PyWpisy, init(): nie można uruchomić pliku.")

    def zamien_tekst_na_strony(self):
        try:
            wejscie = self.sciezka_wejsciowa
            wyjscie = self.sciezka_wyjsciowa
            pystrony = PyStrony(wejscie, wyjscie)
        except:
            print("PyWpisy, zamien_tekst_na_strony(): nie można zamienić tekstu na strony.")

    def dodaj_wpis(self, wpis):
        try:
            sciezka = self.sciezka_strony_glownej
            pyparser = self.pyparser
            pyparser.ustaw_sciezke(sciezka)
            indeksy = pyparser.pobierz_indeks("<wpisy>")
            indeks = indeksy[0] + len("<wpisy>") + 1
            pyparser.wstaw_fragment(wpis, int(indeks))
        except:
            print("PyWpisy, dodaj_wpis(): błąd dodawania wpisu.")

    def wyswietl_strone(self):
        try:
            sciezka = self.sciezka_strony_glownej
            pyparser = self.pyparser
            pyparser.ustaw_sciezke(sciezka)
            pyparser.wyswietl_strone()
        except:
            print("PyWpisy, wyswietl_strone(): nie można wyświetlić strony.")

    def aktualizuj(self):
        try:
            sciezka = self.sciezka_strony_glownej
            pypliki = PyPliki(sciezka)
            strona_glowna = self.pyparser.zwroc_strone()
            pypliki.zapisz_plik(strona_glowna)
        except:
            print("PyWpisy, zapisz_strone_glowna(): nie można zapisać strony głównej.")

    def zwroc_liste_artykulow(self):
        try:
            sciezka = self.sciezka_wyjsciowa
            pypliki = PyPliki(sciezka)
            rozszerzenia = {".html"}
            lista_plikow = pypliki.zwroc_pliki_z_rozszerzeniami(rozszerzenia)
            lista_plikow.sort(key=os.path.getmtime, reverse=False)
            return lista_plikow
        except:
            print("PyWpisy, zwroc_liste_artykulow(): błąd.")

    def zwroc_wpisy(self):
        try:
            sciezka = self.sciezka_strony_glownej
            pyparser = self.pyparser
            pyparser.ustaw_sciezke(sciezka)
            wpisy = pyparser.pobierz_fragmenty("<wpis>", "</wpis>")
            return wpisy
        except:
            print("PyWpisy, zwroc_wpisy(): nie udało się zwrócić wpisów.")
