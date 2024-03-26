import re

class Tekst:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.tekst = []
            self.ustaw_indeks(-1)
            self.ustaw_rozmiar()
            return True
        except:
            print("Klasa Tekst, metoda inicjuj(). \n" +
            "Nie można zainicjować tekstu.")

    def ustaw_rozmiar(self):
        try:
            self.rozmiar = self.zwroc_indeks()
            return True
        except:
            print("Klasa Tekst, metoda ustaw_rozmiar(). \n" +
            "Nie można ustawić rozmiaru.")

    def wyswietl_rozmiar(self):
        try:
            print(self.zwroc_rozmiar())
            return True
        except:
            print("Klasa Tekst, metoda wyswietl_rozmiar(). \n" +
            "Nie można ustawić rozmiaru.")

    def zwroc_rozmiar(self):
        try:
            return self.rozmiar
        except:
            print("Klasa Tekst, metoda zwroc_rozmiar(). \n" +
            "Nie można zwrócić rozmiaru.")

    def ustaw(self, wartosc):
        try:
            self.tekst.append(wartosc)
            self.zwieksz_indeks()
            return True
        except:
            print("Klasa Tekst, metoda ustaw(). \n" +
            "Nie można ustawić tekstu.")
            return False

    def ustaw_indeks(self, wartosc):
        try:
            self.indeks = wartosc
            return True
        except:
            print("Klasa Tekst, metoda ustaw_indeks(). \n" +
            "Nie można ustawić indeksu.")
            return False

    def resetuj_indeks(self):
        try:
            self.indeks = self.zwroc_rozmiar()
            return True
        except:
            print("Klasa Tekst, metoda resetuj_indeks(). \n" +
            "Nie można zresetować indeksu.")
            return False

    def zwieksz_indeks(self):
        try:
            self.indeks += 1
            self.ustaw_rozmiar()
            return True
        except:
            print("Klasa Tekst, metoda zwieksz_indeks(). \n" +
            "Nie można zwiększyć indeksu.")
            return False

    def zwroc_indeks(self):
        try:
            return self.indeks
        except:
            print("Klasa Tekst, metoda zwroc_indeks(). \n" +
            "Nie można zwrócić indeksu.")
            return False

    def zwroc(self):
        try:
            return self.tekst[self.zwroc_indeks()]
        except:
            print("Klasa Tekst, metoda zwroc(). \n" + 
            "Nie można zwrócić tekstu.")
            return False

    def zwroc_element(self, indeks):
        try:
            return self.zwroc()[indeks]
        except:
            print("Klasa Tekst, metoda zwroc_element(). \n" + 
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

    def wyszukaj(self, fraza):
        try:
            maksimum = self.zwroc_rozmiar() + 1
            lista_indeksow = []
            for indeks in range(0, maksimum):
                self.ustaw_indeks(indeks)
                indeksy = self.znajdz_wszystkie(fraza)
                lista_indeksow.append(indeksy)
            return lista_indeksow
        except:
            print("Klasa Tekst, metoda wyszukaj(). \n" + 
            "Nie można wyszukać frazy.")
            return False

    def wstaw(self, fraza, indeks):
        try:
            dlugosc = self.zwroc_dlugosc()
            pierwsza_czesc = self.zwroc_fragment(0, indeks - 1)
            druga_czesc = self.zwroc_fragment(indeks - 1, dlugosc)
            tekst = pierwsza_czesc + fraza + druga_czesc
            self.ustaw(tekst)
            return tekst
        except:
            print("Klasa Tekst, metoda wstaw(). \n" + 
            "Nie można wstawić tekstu.")
            return False

    def wyswietl_historie(self):
        try:
            koniec = self.zwroc_rozmiar() + 1
            for indeks in range(0, koniec):
                self.ustaw_indeks(indeks)
                self.wyswietl()
            self.resetuj_indeks()
            return True
        except:
            print("Klasa Tekst, metoda wyswietl_historie(). \n" + 
            "Nie można wyświetlić historii.")
            return False
