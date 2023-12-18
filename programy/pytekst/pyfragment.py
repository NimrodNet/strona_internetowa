class Fragment:

    def __init__(self, tekst):
        self.tekst = tekst
        self.oddzielniki = ["-", "_"]
        self.fragmenty = []

    def generuj_fragmenty(self):
        try:
            poczatek = 0
            oddzielnik = "-"
            tekst = str(self.tekst)
            koniec = tekst.index(oddzielnik)
            dlugosc = len(tekst)
            fragment = self.tekst[poczatek:koniec]
            print(fragment)
            while poczatek < dlugosc:
                poczatek = koniec + 1
                koniec = tekst.index(oddzielnik, poczatek)
                print(koniec)
        except ValueError:
            print("Błąd")
