import os
from os import walk
import pathlib
import json

def wiadomosc(tresc):
    print(tresc)

class Plik:

    def __init__(self, sciezka):
        try:
            self.sciezka = sciezka
            self.tryby = Tryby()
        except:
            wiadomosc("Nie udało się zainicjować pliku.")

    def zwroc_sciezke(self):
        try:
            return self.sciezka
        except:
            wiadomosc("Nie udało się zwrócić ścieżki.")

    def stworz(self):
        sciezka = self.zwroc_sciezke()
        tresc = ""
        tryb_pliku = self.tryby.tworzenie()
        plik = open(sciezka, tryb_pliku)
        plik.write(tresc)
        plik.close()

    def stworz_folder(self):
        try:
            sciezka = self.zwroc_sciezke()
            folder_istnieje = istnieje(sciezka)
            if folder_istnieje:
                wiadomosc("Folder " + sciezka + " już istnieje.")
            else:
                os.mkdir(sciezka)
        
        except:
            wiadomosc("Nie udało się stworzyć folderu " + sciezka)
            
    def istnieje(self):
        try:
            sciezka = self.zwroc_sciezke()
            return os.path.exists(sciezka)
        except:
            wiadomosc("Nie wiadomo, czy plik istnieje.")

    def usun(self):
        try:
            sciezka = self.zwroc_sciezke()
            os.remove(sciezka)
        except:
            wiadomosc("Nie udało się usunąć pliku.")

    def usun_katalog(self):
        try:
            sciezka = self.zwroc_sciezke()
            sciezka_katalogu = pathlib.Path("pusty katalog")
            sciezka_katalogu.rmdir()
        except:
            wiadomosc("Nie udało się usunąć katalogu.")

    def lista_plikow(self):
        try:
            sciezka_lokalna = self.zwroc_sciezke()
            pliki = []
            for (dirpath, dirnames, filenames) in walk(sciezka_lokalna): 
                pliki.extend(filenames)
                break
        except:
            wiadomosc("Nie udało się pobrać listy plików.")

    def czytaj_json(self):
        try:
            sciezka = self.zwroc_sciezke()
            plik = open(sciezka)
            informacje = json.load(plik)
            print(informacje)
            plik.close()
        except:
            wiadomosc("Nie udało się czytać pliku " + sciezka)
class Tryby: 

    def tworzenie(cls):
        try:
            return "x"
        except:
            wiadomosc("Nie udało się zwrócić trybu tworzenia.")

    def dodawanie(cls):
        try:
            return "a"
        except:
            wiadomosc("Nie udało się zwrócić trybu dodawania.")

    def czytanie(cls):
        try:
            return "r"
        except:
            wiadomosc("Nie udało się zwrócić trybu czytania.")

    def pisanie(cls):
        try:
            return "w"
        except:
            wiadomosc("Nie udało się zwrócić trybu pisania.")

class Sciezka:

    def ustaw(self, sciezka):
        try:
            self.sciezka = sciezka
        except:
            wiadomosc("Nie udało się ustawić ścieżki.")

    def zwroc(self):
        try:
            return self.sciezka
        except:
            wiadomosc("Nie udało się zwrócić ścieżki.")

def wiadomosc(self, wiadomosc):
    print(wiadomosc)

plik_powitania = Plik("witaj.txt")
plik_powitania.stworz()
