from pathlib import Path

class Zamien_na_sciezke:

    def wykonaj(self, foldery):
        try:
            sciezka = ""
            for folder in foldery:
                sciezka += folder + "\\"
            return sciezka
        except:
            print("Klasa Zamien_na_sciezke, metoda wykonaj(). \n" +
            "Nie udało się zamienić na ścieżkę.")
