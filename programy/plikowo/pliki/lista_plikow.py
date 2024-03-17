import glob

class Lista_plikow:

    def wykonaj(self, sciezka):
        try:
           return glob.glob(sciezka)
        except:
            print("Klasa Lista_plikow, metoda wykonaj(). \n" +
            "Nie udało się pobrać listy plików")
