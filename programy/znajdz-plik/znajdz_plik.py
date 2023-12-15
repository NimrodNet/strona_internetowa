from moduly.wszystkie_pliki import *
import os

class Znajdz_plik:

    def __init__(self, sciezka, nazwa):
        self.sciezka = sciezka
        self.nazwa = nazwa

    def zwroc_pliki(self):
        rozszerzenia = {".html"}
        wszystkie_pliki = Wszystkie_pliki(self.sciezka)
        pliki = wszystkie_pliki.zwroc_wszystkie_pliki(rozszerzenia)
        szukane_pliki = []
        for plik in pliki:
            nazwa_pliku = os.path.basename(str(plik))
            if self.nazwa in nazwa_pliku:
                szukane_pliki.append(nazwa_pliku)
        return szukane_pliki

sciezka = "/home/qwerty891/Pulpit/strona_internetowa/artykuly/"
nazwa = input("Podaj nazwę pliku: ")
znajdz_plik = Znajdz_plik(sciezka, nazwa)
szukane_pliki = znajdz_plik.zwroc_pliki()
print(szukane_pliki)
