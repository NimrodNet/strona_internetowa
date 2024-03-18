import shutil

class Kopiuj_plik:

    def wykonaj(self, zrodlo, cel):
        try:
            shutil.copy(zrodlo, cel)
            return True
        except:
            print("Klasa Kopiuj_plik, metoda wykonaj(). " + 
            "Nie udało się skopiować pliku")
