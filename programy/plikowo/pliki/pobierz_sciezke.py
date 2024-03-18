import os

class Pobierz_sciezke:

    def wykonaj(self, sciezka):
        try:
            nazwa = os.path.dirname(sciezka)
            return nazwa
        except:
            print("Klasa Pobierz_nazwe, metoda wykonaj(). \n" +
            "Nie można pobrać nazwy.")
            return False
