import os
import sys

class Wszystkie_pliki:

    def __init__(self, sciezka):
        self.sciezka = sciezka

    def zwroc_wszystkie_pliki(self, rozszerzenia):
        path = self.sciezka
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                nazwa_pliku = file
                indeks_kropki = nazwa_pliku.rfind(".")
                dlugosc = len(nazwa_pliku)
                rozszerzenie_pliku = nazwa_pliku[int(indeks_kropki):int(dlugosc)]
                for rozszerzenie in rozszerzenia:
                    if rozszerzenie == rozszerzenie_pliku:
                        sciezka = os.path.join(r, file)
                        files.append(sciezka)
        return files

    def zwroc_pliki(self, rozszerzenia):
        pliki = []
        for rozszerzenie in rozszerzenia:
            tymczasowe_pliki = self.zwroc_wszystkie_pliki(rozszerzenie)
            pliki.append(tymczasowe_pliki)
        return pliki
