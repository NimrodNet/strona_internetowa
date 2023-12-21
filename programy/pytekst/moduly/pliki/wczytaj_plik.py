class Wczytaj_plik:

    def __init__(self, sciezka):
        self.ustaw_sciezke(sciezka)

    def ustaw_sciezke(self, sciezka):
        self.sciezka = sciezka

    def zwroc_sciezke(self):
        return self.sciezka

    def wczytaj_plik(self):
        try:
            sciezka = self.zwroc_sciezke()
            plik = open(sciezka, "r")
            zawartosc = plik.read()
            plik.close()
        except:
            print("Nie udało się wczytać pliku " + plik)
        return zawartosc
