import pygame
from obraz import *
from wyjdz import *
from w_grze import *
pygame.init()

class MenedzerBanku:

    def __init__(self):
        try:
            self.inicjuj()
        except:
            self.komunikat("__init__()", "Błąd inicjacji gry.")

    def inicjuj(self):
        try:
            obraz = Obraz(pygame, 500, 500)
            self.ustaw_tytul()
            self.w_grze()
            Wyjdz(pygame)
        except:
            self.komunikat("inicjuj()", "Nie udało się zainicjować gry.")

    def w_grze(self):
        try:
            w_grze = W_grze()
            w_grze.uruchom(pygame)
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
