import os

class Pobierz_nazwe:

    def wykonaj(self, sciezka):
        try:
            pelna_nazwa = os.path.basename(sciezka)
            nazwa = os.path.splitext(pelna_nazwa)[0]
            return nazwa
        except:
            print("Klasa Pobierz_nazwe, metoda wykonaj(). \n" +
            "Nie można pobrać nazwy pliku.")
