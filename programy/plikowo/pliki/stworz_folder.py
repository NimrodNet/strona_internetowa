import os

class Stworz_folder:

    def wykonaj(self, sciezka):
        try:
            os.mkdir(sciezka)
            return True
        except:
            print("Klasa Stworz_folder, metoda wykonaj(). \n" +
            "Nie można stworzyć nowego folderu.")
            return False
