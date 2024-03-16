import os

class Usun_plik:

    def wykonaj(self, sciezka):
        try:
            os.remove(sciezka)
            return True
        except:
            print("Klasa Usun_plik, metoda wykonaj(). \n" +
            "Nie można usunąć pliku.")
            return False
