class Plik:

    def __init__(self, sciezka):
        self.sciezka = sciezka

    def stworz(self):
        tresc = ""
        tryb_pliku = "x" 
        plik_lokalny = open(self.sciezka, tryb_pliku)
        plik_lokalny.write(tresc)
        plik_lokalny.close()

class Tryby: 

    def tworzenie():
        return "x"

    def dodawanie():
        return "a"

    def czytanie():
        return "r"

    def pisanie():
        return "w"

class Sciezka:

    def ustaw(self, sciezka):
        self.sciezka = sciezka

    def zwroc(self):
        return self.sciezka

plik = Plik("witaj.txt")
plik.stworz()
