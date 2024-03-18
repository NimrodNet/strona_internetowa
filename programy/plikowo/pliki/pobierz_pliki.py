import glob

class Pobierz_pliki:

    def wykonaj(self, sciezka):
        try:
           pliki = glob.glob(sciezka + "**", recursive=True)
           return pliki
        except:
            print("Klasa Lista_plikow, metoda wykonaj(). \n" +
            "Nie udało się pobrać listy plików")
            return False
