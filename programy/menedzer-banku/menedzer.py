import pygame
from obraz import *
from wyjdz import *
pygame.init()

class MenedzerBanku:

    def __init__(self):
        obraz = Obraz(pygame, 500, 500)
        self.ustaw_flage_gry(True)
        self.w_grze()
        Wyjdz(pygame)

    def ustaw_flage_gry(self, flaga_gry):
        try:
            self.flaga_gry = flaga_gry
        except:
            self.komunikat("ustaw_flage_gry()", "Problem z ustawieniem flagi gry.")

    def zwroc_flage_gry(self):
        try:
            return self.flaga_gry
        except:
            self.komunikat("zwroc_flage_gry()", "Nie udało się zwrócić flagi gry.")

    def w_grze(self):
        uruchomiono = self.zwroc_flage_gry()
        while uruchomiono:
            for zdarzenie in pygame.event.get():
                graczNaciskaCzerwonyX = zdarzenie.type == pygame.QUIT
                if graczNaciskaCzerwonyX:
                    self.ustaw_flage_gry(False)
            pygame.display.flip()
            uruchomiono = self.zwroc_flage_gry()

    def komunikat(self, metoda, wiadomosc):
        print("Plik menedzer.py, klasa MenedzerBanku, metoda " + metoda + ".  " + wiadomosc)

MenedzerBanku()
