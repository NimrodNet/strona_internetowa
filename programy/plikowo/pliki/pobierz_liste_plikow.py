import os
import glob

class Pobierz_liste_plikow:

    def wykonaj(self, sciezka):
        try:
           pliki = glob.glob(sciezka + r'\**\*.py', recursive=True)
           return pliki
        except:
            print("Klasa Lista_plikow, metoda wykonaj(). \n" +
            "Nie udało się pobrać listy plików")
            return False
