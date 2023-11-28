import os
import sys

class Wszystkie_pliki:

    def __init__(self, sciezka):
        self.sciezka = sciezka

    def zwroc_wszystkie_pliki(self, rozszerzenie):
        path = self.sciezka
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if rozszerzenie in file:
                    files.append(os.path.join(r, file))
        return files

    def zwroc_pliki(self, rozszerzenia):
        pliki = []
        for rozszerzenie in rozszerzenia:
            tymczasowe_pliki = self.zwroc_wszystkie_pliki(rozszerzenie)
            pliki.append(tymczasowe_pliki)
        return pliki
