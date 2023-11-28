class Lokalizacja_elementu:

    def __init__(self, wartosc):
        self.konstruuj(wartosc)

    def zwroc_poczatek(cls):
        return "<loc>"

    def zwroc_koniec(cls):
        return "</loc>"

    def konstruuj(self, wartosc):
        poczatek = self.zwroc_poczatek()
        koniec = self.zwroc_koniec()
        self.lokalizacja = poczatek + wartosc + koniec

    def zwroc_element(self):
        return self.lokalizacja
