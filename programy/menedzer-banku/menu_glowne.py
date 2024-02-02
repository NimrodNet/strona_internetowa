from nowa_gra import *
from wczytaj_gre import *
from autorzy_gry import *
from wyjscie_z_gry import *

class Menu_glowne:

    def nowa_gra(self):
        try:
            nowa_gra = Nowa_gra()
        except:
            print("Nie udało się utworzyć nowej gry.")

    def wczytaj_gre(self):
        try:
            wczytaj_gre = Wczytaj_gre()
        except:
            print("Nie udało się wczytać nowej gry.")

    def autorzy(self):
        try:
            autorzy = Autorzy_gry()
        except:
            print("Nie udało się wczytać autorów gry.")

    def wyjscie(self):
        try:
            wyjscie = Wyjscie_z_gry()
        except:
            print("Nie udało się wyjść poprawnie z gry.")
