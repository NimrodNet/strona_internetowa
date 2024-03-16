class Zapisz_plik:

    def wykonaj(self, sciezka, wiadomosc):
        try:
            plik = open(sciezka, "a")
            plik.write(wiadomosc)
            plik.close()
        except:
            print("Klasa Zapisz_plik(), metoda wykonaj(). \n" +
            "Nie można zapisać pliku.")
