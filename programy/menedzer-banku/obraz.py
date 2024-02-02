class Obraz:

    def __init__(self, instancja, szerokosc, wysokosc):
        try:
            self.inicjuj(instancja, szerokosc, wysokosc)
        except:
            self.komunikat("__init__()", "Nie udało się zainicjować obrazu.")

    def inicjuj(self, instancja, szerokosc, wysokosc):
        try:
            self.ustaw_instancje(instancja)
            self.ustaw_szerokosc(szerokosc)
            self.ustaw_wysokosc(wysokosc)
            self.ustaw_rozdzielczosc()
        except:
            self.komunikat
            ("inicjuj(instancja, szerokosc, wysokosc)", 
            "Nie udało się zainicjować ustawień.")

    def ustaw_rozdzielczosc(self):
        try:
            instancja = self.zwroc_instancje()
            wysokosc = self.zwroc_wysokosc()
            szerokosc = self.zwroc_szerokosc()
            instancja.display.set_mode([wysokosc, szerokosc])
        except:
            self.komunikat("ustaw_rozdzielczosc()", "Nie udało się ustawić rozdzielczości.")

    def ustaw_instancje(self, instancja):
        try:
            self.instancja = instancja
        except:
            self.komunikat("ustaw_instancje(instancja)", "Nie udało się ustawić instancji.")

    def ustaw_szerokosc(self, szerokosc):
        try:
            self.szerokosc = szerokosc
        except:
            self.komunikat("ustaw_szerokosc(szerokosc)", "Nie udało się ustawić szerokości.")

    def ustaw_wysokosc(self, wysokosc):
        try:
            self.wysokosc = wysokosc
        except:
            self.komunikat("ustaw_wysokosc(wysokosc)", "Nie udało się ustawić wysokości.")

    def zwroc_instancje(self):
        try:
            return self.instancja
        except:
            self.komunikat("zwroc_instancje()", "Nie udało się zwrócić instancji.")

    def zwroc_szerokosc(self):
        try:
            return self.szerokosc
        except:
            self.komunikat("zwroc_szerokosc()", "Nie udało się zwrócić szerokości.")
            return 0

    def zwroc_wysokosc(self):
        try:
            return self.wysokosc
        except:
            self.komunikat("zwroc_wysokosc()", "Nie udało się zwrócić wysokości.")

    def komunikat(metoda, wiadomosc):
        try:
            print("Plik obraz.py, klasa Obraz, metoda " + metoda + ". " + wiadomosc)
        except:
            print("Nie udało się wyświetlić komunikatu.")
