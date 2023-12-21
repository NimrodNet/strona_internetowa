import os
from moduly.pliki.wszystkie_pliki import *
from moduly.pliki.zapisz_plik import *
from moduly.pliki.wczytaj_plik import *
from pathlib import Path

class PyPliki:

    def __init__(self, sciezka):
        self.ustaw_sciezke(sciezka)

    def ustaw_sciezke(self, sciezka):
        self.sciezka = sciezka

    def zwroc_sciezke(self):
        return self.sciezka

    def zwroc_wszystkie_pliki(self):
        wszystkie_pliki = Wszystkie_pliki(self.sciezka)
        return wszystkie_pliki.zwroc_wszystkie_pliki()

    def zwroc_pliki_z_rozszerzeniami(self, rozszerzenia):
        wszystkie_pliki = Wszystkie_pliki(self.sciezka)
        pliki_z_rozszerzeniami = wszystkie_pliki.zwroc_pliki_z_rozszerzeniami(rozszerzenia)
        return pliki_z_rozszerzeniami

    def zwroc_nazwe_pliku(self):
        return os.path.basename(self.zwroc_sciezke())

    def zwroc_nazwe_pliku_bez_rozszerzenia(self):
        return Path(self.zwroc_sciezke()).stem

    def zapisz_plik(self, tekst):
        zapisz_plik = Zapisz_plik(self.sciezka)
        zapisz_plik.zapisz(tekst)

    def wczytaj_plik(self):
        wczytanie_pliku = Wczytaj_plik(self.sciezka)
        return wczytanie_pliku.wczytaj_plik()

    def plik_istnieje(self):
        return os.path.exists(self.sciezka)
