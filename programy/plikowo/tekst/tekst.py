import re

class Tekst:

    def __init__(self):
        self.ustaw("")

    def ustaw(self, wartosc):
        try:
            self.wartosc = str(wartosc)
            return True
        except:
            print("Klasa Tekst, metoda ustaw(). \n" +
            "Nie można ustawić tekstu.")
            return False

    def zwroc(self):
        try:
            return self.wartosc
        except:
            print("Klasa Tekst, metoda zwroc(). \n" + 
            "Nie można zwrócić tekstu.")
            return False

    def zwroc_dlugosc(self):
        try:
            return len(self.zwroc())
        except:
            print("Klasa Tekst, metoda zwroc(). \n" + 
            "Nie można zwrócić tekstu.")
            return False

    def zwroc_fragment(self, poczatek, koniec):
        try:
            return self.zwroc()[poczatek:koniec]
        except:
            print("Klasa Tekst, metoda zwroc_fragment(). \n" + 
            "Nie można zwrócić fragmentu.")
            return False

    def wyswietl(self):
        try:
            print(self.zwroc())
            return True
        except:
            print("Klasa Tekst, metoda wyswietl(). \n" + 
            "Nie można wyświetlić tekstu.")
            return False

    def znajdz(self, fraza):
        try:
            return self.zwroc().find(str(fraza))
        except:
            print("Klasa Tekst, metoda znajdz(). \n" + 
            "Nie można znaleźć frazy.")
            return False

    def znajdz_od(self, fraza, od):
        try:
            do = self.zwroc_dlugosc()
            return self.zwroc().find(str(fraza), od, do)
        except:
            print("Klasa Tekst, metoda znajdz_od(). \n" + 
            "Nie można znaleźć frazy.")
            return False

    def znajdz_od_do(self, fraza, od, do):
        try:
            return self.zwroc().find(str(fraza), od, do)
        except:
            print("Klasa Tekst, metoda znajdz_od_do(). \n" + 
            "Nie można znaleźć frazy.")
            return False

    def znajdz_wszystkie(self, fraza):
        try:
            return [m.start() for m in re.finditer(fraza, self.zwroc())]
        except:
            print("Klasa Tekst, metoda znajdz_wszystkie(). \n" + 
            "Nie można znaleźć fraz.")
            return False

    def znajdz_wszystkie_od(self, fraza, od):
        try:
            do = self.zwroc_dlugosc()
            indeksy = self.znajdz_wszystkie(fraza)
            tymczasowa = []
            for wartosc in indeksy:
                if wartosc >= od:
                    tymczasowa.append(wartosc)
            indeksy = tymczasowa
            return indeksy
        except:
            print("Klasa Tekst, metoda znajdz_wszystkie_od(). \n" + 
            "Nie można znaleźć fraz.")
            return False

    def znajdz_wszystkie_od_do(self, fraza, od, do):
        try:
            indeksy = self.znajdz_wszystkie(fraza)
            tymczasowa = []
            for wartosc in indeksy:
                if wartosc >= od and wartosc <= do:
                    tymczasowa.append(wartosc)
            indeksy = tymczasowa
            return indeksy
        except:
            print("Klasa Tekst, metoda znajdz_wszystkie_od_do(). \n" + 
            "Nie można znaleźć fraz.")
            return False
