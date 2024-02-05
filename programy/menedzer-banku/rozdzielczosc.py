class Rozdzielczosc:

    def __init__(self):
        self.ustaw_szerokosc(500)
        self.ustaw_wysokosc(700)

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

    def zwroc_szerokosc(self):
        try:
            return self.szerokosc
        except:
            self.komunikat("zwroc_szerokosc()", "Nie udało się zwrócić szerokości.")
            return False

    def zwroc_wysokosc(self):
        try:
            return self.wysokosc
        except:
            self.komunikat("zwroc_wysokosc()", "Nie udało się zwrócić wysokości.")
            return False

    def komunikat(self, metoda, wiadomosc):
        try:
            print("Plik rozdzielczosc.py, klasa Rozdzielczosc, metoda " + metoda + ". " + wiadomosc)
        except:
            print("Nie udało się wyświetlić komunikatu.")
