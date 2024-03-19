import os

class Jest_plikiem:

    def wykonaj(self, sciezka):
        try:
            jest_plikiem = os.path.isfile(sciezka)
            return jest_plikiem
        except:
            print("Klasa Jest_plikiem, metoda wykonaj(). \n" + 
            "Błąd wywołania metody.")
