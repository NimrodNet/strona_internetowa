class Czytaj_plik:

    def wykonaj(self, sciezka):
        wiadomosc = ""
        try:
            plik = open(sciezka, "r")
            wiadomosc = plik.read()
            return wiadomosc
        except:
            print("Klasa Czytaj_plik, metoda wykonaj(). \n" +
                  "Nie udało się odczytać pliku.")
            return wiadomosc
