class Tablica:

    def __init__(self):
        self.stworz()

    def stworz(self):
        try:
            self.tablica = []
            return True
        except:
            print("Klasa Tablica, metoda stworz(). \n" + 
            "Nie można stworzyć tablicy.")
            return False

    def zwroc(self):
        try:
            return self.tablica
        except:
            print("Klasa Tablica, metoda stworz(). \n" + 
            "Nie można stworzyć tablicy.")
            return False

    def ustaw(self, tablica):
        try:
            self.tablica = tablica
            return self.tablica
        except:
            print("Klasa Tablica, metoda ustaw(). \n" + 
            "Nie można ustawić tablicy.")
            return False

    def dodaj(self, element):
        try:
            self.zwroc().append(element)
            return self.zwroc()
        except:
            print("Klasa Tablica, metoda dodaj(). \n" +
            "Nie można dodać elementu.")
            return False

    def wyswietl(self):
        try:
            tablica = self.zwroc()
            for element in tablica:
                print(element)
            return self.zwroc()
        except:
            print("Klasa Tablica, metoda wyswietl(). \n" +
            "Nie można wyświetlić tablicy.")
            return False

    def rozmiar(self):
        try:
            return len(self.zwroc())
        except:
            print("Klasa Tablica, metoda rozmiar(). \n" +
            "Nie można wyświetlić rozmiaru.")
            return False

    def wyczysc(self):
        try:
            self.zwroc().clear()
            return self.zwroc()
        except:
            print("Klasa Tablica, metoda wyczysc(). \n" +
            "Nie można wyczyścić tablicy.")
            return False

    def wstaw(self, element, numer):
        try:
            self.zwroc().insert(numer, element)
            return self.zwroc()
        except:
            print("Klasa Tablica, metoda wstaw(). \n" +
            "Nie można wstawić elementu.")
            return False

    def element(self, element):
        try:
            return self.zwroc().count(element)
        except:
            print("Klasa Tablica, metoda element(). \n" +
            "Nie można pobrać elementu.")
            return False

    def scal(self, tablica):
        try:
            for element in tablica:
                self.dodaj(element)
            return self.zwroc()
        except:
            print("Klasa Tablica, metoda scal(). \n" +
            "Nie można scalić tablic.")
            return False

    def zamien(self, oryginal, nowy_element):
        try:
            self.zwroc()[oryginal] = nowy_element
            return self.zwroc()
        except:
            print("Klasa Tablica, metoda zamien(). \n" +
            "Nie można zamienić elementów.")
            return False

    def wyzeruj(self):
        try:
            poczatek = [0]
            koniec = [self.rozmiar()]
            indeks = [0]
            element = [" "]
            ja = [self]
            zwroc = [ja[0].zwroc()]
            zakres = [range(poczatek[0], koniec[0])]
            for indeks[0] in zakres[0]:
                ja[0].zamien(indeks[0], element[0])
            return zwroc[0]
        except:
            komunikat = [print("Klasa Tablica, metoda wyzeruj(). \n" +
            "Nie można wyzerować elementów."), False]
            komunikat[0]
            return komunikat[1]
