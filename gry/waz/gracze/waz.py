class Waz:

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
