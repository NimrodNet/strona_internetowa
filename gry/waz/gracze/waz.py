class Waz:

    def __init__(self):
        self.ustaw_punkty(0)
        self.ustaw_dlugosc(1)

    def ustaw_punkty(self, punkty):
        try:
            self.punkty = punkty
            return True
        except:
            print("Klasa Waz, metoda ustaw_punkty(). \n" +
            "Nie można ustawić punktów.")
            return False

    def zwroc_punkty(self):
        try:
            return self.punkty
        except:
            print("Klasa Waz, metoda zwroc_punkty(). \n" +
            "Nie można zwrócić punktów.")
            return False

    def zwieksz_punkty(self):
        try:
            self.punkty += 1
            return True
        except:
            print("Klasa Waz, metoda zwieksz_punkty(). \n" +
            "Nie można zwiększyć punktów.")
            return False

    def ustaw_dlugosc(self, dlugosc):
        try:
            self.dlugosc = dlugosc
            return True
        except:
            print("Klasa Waz, metoda ustaw_dlugosc(). \n" +
            "Nie można ustawić długości.")
            return False

    def zwieksz_dlugosc(self):
        try:
            self.dlugosc += 1
            return True
        except:
            print("Klasa Waz, metoda zwieksz_dlugosc(). \n" + 
            "Nie można zwiększyć długości.")
            return False

    def zwroc_dlugosc(self):
        try:
            return self.dlugosc
        except:
            print("Klasa Waz, metoda zwroc_dlugosc(). \n" + 
            "Nie można zwrócić długości.")
            return False

    def wyswietl_statystyki(self):
        try:
            print("Liczba punktów wynosi", self.zwroc_punkty(), ".")
            return True
        except:
            print("Klasa Waz, metoda wyswietl_statystyki(). \n" + 
            "Nie można wyświetlić statystyk..")
            return False
