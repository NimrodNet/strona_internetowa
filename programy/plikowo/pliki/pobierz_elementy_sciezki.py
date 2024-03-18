from pathlib import Path

class Pobierz_elementy_sciezki:

    def wykonaj(self, sciezka):
        try:
            elementy = Path(sciezka).parts
            return elementy
        except:
            print("Klasa Pobierz_elementy_sciezki, metoda wykonaj(). \n" +
            "Nie można pobrać ścieżek.")
            return False
