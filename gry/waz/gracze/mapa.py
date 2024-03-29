class Mapa:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.mapa = []
            self.szerokosc = 10
            self.wysokosc = 10
            rozmiar = self.szerokosc * self.wysokosc
            for x in range(0, self.szerokosc):
                for y in range(0, self.wysokosc):
                    punkt = Punkt()
                    punkt.stworz([x, y], 1)
                    self.mapa.append(punkt)
            return True
        except:
            print("Klasa Mapa, metoda inicjuj(). \n" +
            "Nie można zainicjować mapy.")
            return False

    def wyswietl(self):
        try:
            rozmiar = self.szerokosc * self.wysokosc
            for x in range(0, rozmiar):
                punkt = self.mapa[x]
                wartosc_punktu = punkt.zwroc_wartosc()
                print(wartosc_punktu, end="")
                if x % self.szerokosc == 0:
                    print("")
            return True
        except:
            print("Klasa Mapa, metoda inicjuj(). \n" +
            "Nie można zainicjować mapy.")
            return False


class Punkt:

    def stworz(self, wspolrzedne, wartosc):
        try:
            self.wspolrzedne = wspolrzedne
            self.wartosc = wartosc
            return True
        except:
            print("Klasa Mapa, metoda stworz(). \n" + 
            "Nie można stworzyć punktu..")
            return False

    def zwroc_wartosc(self):
        try:
            return self.wartosc
        except:
            print("Klasa Mapa, metoda zwroc_wartosc(). \n" + 
            "Nie można zwrócić wartości.")
            return False

