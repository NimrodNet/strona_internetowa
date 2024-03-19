import os

class Pobierz_nazwe_systemu:

    def wykonaj(self):
        try:
            system = os.name
            return system
        except:
            print("Klasa Pobierz_nazwe_systemu, metoda wykonaj(). \n" +
            "Nie można pobrać nazwy systemu.")
            return False
