import os

class Pobierz_rozszerzenie:

    def wykonaj(self, sciezka):
        try:
            pelna_nazwa = os.path.basename(sciezka)
            rozszerzenie = os.path.splitext(pelna_nazwa)[1]
            return rozszerzenie
        except:
            print("Klasa Pobierz_rozszerzenie, metoda wykonaj(). \n" +
            "Nie można pobrać rozszerzenia.")
            return False
