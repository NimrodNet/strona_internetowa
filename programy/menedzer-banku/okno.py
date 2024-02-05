class Okno:

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
            wyswietlacz = instancja.display.set_mode([wysokosc, szerokosc])
            self.ustaw_wyswietlacz(wyswietlacz)
        except:
            self.komunikat("ustaw_rozdzielczosc()", "Nie udało się ustawić rozdzielczości.")

    def ustaw_wyswietlacz(self, wyswietlacz):
        try:
            self.wyswietlacz = wyswietlacz
        except:
            self.komunikat("ustaw_wyswietlacz()", "Nie udało się ustawić wyświetlacza")

    def zwroc_wyswietlacz(self):
        try:
            return self.wyswietlacz
        except:
            self.komunikat("zwroc_wyswietlacz()", "Nie można zwrócić wyświetlacza.")
            return False

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

    def ustaw_tlo(self, tlo):
        try:
            self.tlo = tlo
            wyswietlacz = self.zwroc_wyswietlacz()
            wyswietlacz.fill(tlo)
        except:
            self.komunikat("ustaw_tlo(tlo)", "Nie udało się ustawić tła.")

    def zwroc_tlo(self):
        try:
            return self.tlo
        except:
            self.komunikat("ustaw_tlo(tlo)", "Nie udało się zwrócić tła.")

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
