class Stworz_plik:

    def wykonaj(self, sciezka):
        try:
            plik = open(sciezka, "x")
            return True;
        except:
            print("Klasa Stworz_plik, metoda wykonaj().\n" +
            "Nie można stworzyć pliku.")
            return False;
