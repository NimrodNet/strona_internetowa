import glob

class Pobierz_poziom_plikow:

    def wykonaj(self, sciezka):
        try:
            pliki = glob.glob(sciezka + "*", recursive=True)
            return pliki
        except:
            print("Klasa Pobierz_poziom_plikow, metoda wykonaj(). \n" + 
            "Nie można pobrać plików.")
