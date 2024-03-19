import os

class Pobierz_bajty:

    def wykonaj(self, sciezka):
        try:
            bajty = os.path.getsize(sciezka)
            return bajty
        except:
            print("Klasa Pobierz_bajty, metoda wykonaj(). \n" +
            "Nie można pobrać bajtów.")
