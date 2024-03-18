import os

class Plik_istnieje:

    def wykonaj(self, sciezka):
        try:
            plik_istnieje = os.path.exists(sciezka)
            return plik_istnieje
        except:
            print("Klasa Plik_istnieje, metoda wykonaj(). \n" +
            "Niepoprawne wywołanie metody lub plik nie istnieje.")
            return False
