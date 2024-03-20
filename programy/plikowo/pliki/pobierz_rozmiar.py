import os

class Pobierz_rozmiar_pliku:

    def wykonaj(self, sciezka):
        try:
            rozmiar = os.path.getsize(sciezka)
            return rozmiar
        except:
            print("Klasa Pobierz_rozmiar, metoda wykonaj(). " +
            "Nie można pobrać rozmiaru pliku.")
