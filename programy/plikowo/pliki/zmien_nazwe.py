import os

class Zmien_nazwe:

    def wykonaj(self, zrodlo, cel):
        try:
            os.rename(zrodlo, cel)
            return True
        except:
            print("Klasa Zmien_nazwe, metoda wykonaj(). " +
            "Nie można zmienić nazwy.")
