import os
from os import walk
import pathlib

class Plik:

    def __init__(self, sciezka):
        try:
            self.sciezka = sciezka
            self.tryby = Tryby()
        except:
            print("Nie udało się zainicjować pliku.")

    def zwroc_sciezke(self):
        try:
            return self.sciezka
        except:
            print("Nie udało się zwrócić ścieżki.")

    def stworz(self):
        try:
            tresc = ""
            tryb_pliku = self.tryby.tworzenie()
            sciezka_lokalna = self.zwroc_sciezke()
            plik_lokalny = open(sciezka_lokalna, tryb_pliku)
            plik_lokalny.write(tresc)
            plik_lokalny.close()
        except:
            print("Nie udało się stworzyć pliku.")

    def istnieje(self):
        try:
            sciezka = self.zwroc_sciezke()
            return os.path.exists(sciezka)
        except:
            print("Nie wiadomo, czy plik istnieje.")

    def usun(self):
        try:
            sciezka = self.zwroc_sciezke()
            os.remove(sciezka)
        except:
            print("Nie udało się usunąć pliku.")

    def usun_katalog(self):
        try:
            sciezka = self.zwroc_sciezke()
            sciezka_katalogu = pathlib.Path("pusty katalog")
            sciezka_katalogu.rmdir()
        except:
            print("Nie udało się usunąć katalogu.")

    def lista_plikow(self):
        try:
            sciezka_lokalna = self.zwroc_sciezke()
            pliki = []
            for (dirpath, dirnames, filenames) in walk(sciezka_lokalna): 
                pliki.extend(filenames)
                break
        except:
            print("Nie udało się pobrać listy plików.")

class Tryby: 

    def tworzenie(cls):
        try:
            return "x"
        except:
            print("Nie udało się zwrócić trybu tworzenia.")

    def dodawanie(cls):
        return "a"

    def czytanie(cls):
        return "r"

    def pisanie(cls):
        return "w"

class Sciezka:

    def ustaw(self, sciezka):
        self.sciezka = sciezka

    def zwroc(self):
        return self.sciezka

plik = Plik("witaj.txt")
plik.stworz()
