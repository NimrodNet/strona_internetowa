import os

class Jest_folderem:

    def wykonaj(self, sciezka):
        try:
            jest_folderem = os.path.isdir(sciezka)
            return jest_folderem
        except:
            print("Klasa Jest_folderem, metoda wykonaj(). \n" +
            "Nie można wykonać sprawdzenia.")
            return False
