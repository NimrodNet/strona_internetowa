import pygame
from okno import *
from wyjdz import *
from w_grze import *
from rozdzielczosc import *
pygame.init()

class MenedzerBanku:

    def __init__(self):
        try:
            self.inicjuj()
        except:
            self.komunikat("__init__()", "Błąd inicjacji gry.")

    def inicjuj(self):
        try:
            rozdzielczosc = Rozdzielczosc()
            szerokosc = rozdzielczosc.zwroc_szerokosc()
            wysokosc = rozdzielczosc.zwroc_wysokosc()
            okno = Okno(pygame, wysokosc, szerokosc)
            self.ustaw_obraz(okno)
            self.ustaw_tytul()
            self.w_grze()
            Wyjdz(pygame)
        except:
            self.komunikat("inicjuj()", "Nie udało się zainicjować gry.")

    def ustaw_obraz(self, obraz):
        try:
            self.obraz = obraz
        except:
            self.komunikat("ustaw_obraz(obraz)", "Nie można ustawić obrazu.")

    def zwroc_obraz(self):
        try:
            return self.obraz
        except:
            self.komunikat("zwroc_obraz()", "Nie można zwrócić obrazu.")
            return False

    def w_grze(self):
        try:
            w_grze = W_grze()
            obraz = self.zwroc_obraz()
            w_grze.uruchom(pygame, obraz)
        except:
            self.komunikat("w_grze()", "Nie udało się uruchomić gry.")

    def ustaw_tytul(self):
        try:
            pygame.display.set_caption('Menedżer Banku')
        except:
            self.komunikat("ustaw_tytul()", "Nie udało się ustawić tytułu.")

    def komunikat(self, metoda, wiadomosc):
        try:
            print("Plik menedzer.py, klasa MenedzerBanku, metoda " + metoda + ".  " + wiadomosc)
        except:
            print("Plik menedzer.py, klasa MenedzerBanku, metoda komunikat(). Nie udało się wyświetlić komunikatu.")
