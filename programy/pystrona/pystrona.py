from moduly.sciezka import *

class PyStrona:

    def __init__(self, sciezka):
        self.sciezka = Sciezka(sciezka)

    def ustaw_sciezke(self, sciezka):
        self.sciezka.ustaw(sciezka)

    def zwroc_sciezke(self):
        return self.sciezka.zwroc()

    def zwroc_tresc(self):
        sciezka = self.zwroc_sciezke()
        tresc = ""
        return tresc
