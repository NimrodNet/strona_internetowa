import shutil

class Usun_folder:

    def wykonaj(self, sciezka):
        try:
            shutil.rmtree(sciezka)
            return True
        except:
            print("Klasa Usun_folder, metoda wykonaj(). \n" +
            "Nie można usunąć pliku.")
