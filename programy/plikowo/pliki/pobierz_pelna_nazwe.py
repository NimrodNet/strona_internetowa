import os

class Pobierz_pelna_nazwe:

    def wykonaj(self, sciezka):
        try:
            pelna_nazwa = os.path.basename(sciezka)
            return pelna_nazwa
        except:
            print("Klasa Pobierz_pelna_nazwe, metoda wykonaj(). \n" +
            "Nie można pobrać nazwy pliku.")
