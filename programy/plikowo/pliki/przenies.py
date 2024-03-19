import shutil

class Przenies:

    def wykonaj(self, zrodlo, cel):
        try:
            shutil.move(zrodlo, cel)
            return True
        except:
            print("Klasa Przenies, metoda wykonaj(). \n" + 
            "Nie można przenieść pliku.")
            return False
