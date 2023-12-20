import os
import sys

class Wszystkie_pliki:

    def __init__(self, sciezka):
        self.sciezka = sciezka

    def zwroc_wszystkie_pliki(self):
        path = self.sciezka
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                files.append(os.path.join(r, file))
        return files

    def zwroc_pliki_z_rozszerzeniami(self, rozszerzenia):
        path = self.sciezka
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                nazwa_pliku = os.path.basename(file)
                indeks_kropki = nazwa_pliku.rfind(".")
                dlugosc = len(nazwa_pliku)
                rozszerzenie_pliku = nazwa_pliku[int(indeks_kropki):int(dlugosc)]
                for rozszerzenie in rozszerzenia:
                    if rozszerzenie == rozszerzenie_pliku:
                        files.append(os.path.join(r, file))
        return files
