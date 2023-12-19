class Zapisz_plik:

    def __init__(self, sciezka):
        self.sciezka = sciezka

    def zapisz(self, tekst):
        plik = open(self.sciezka, "w")
        plik.write(tekst)
        plik.close()
