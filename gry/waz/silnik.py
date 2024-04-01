import pygame
import random
from gracze.waz import *

class Silnik:

    def __init__(self):
        nazwa_klasy = "Silnik"
        self.inicjuj()

    def zwroc_nazwe_klasy(self):
        try:
            return "Silnik"
        except:
            print("Klasa " + nazwa_klasy + ", metoda zwroc_nazwe_klasy(). \n" + 
            "Nie można zwrócić nazwy klasy.")
            return False

    def inicjuj(self):
        try:
            pygame.init()
            self.zegar = pygame.time.Clock()
            self.ustaw_rozdzielczosc(1280, 720)
            self.ustaw_logike_gry()
            return True
        except:
            print("Klasa " + nazwa_klasy + ", metoda inicjuj(). \n" +
            "Nie można zainicjować silnika.")
            return False

    def ustaw_rozdzielczosc(self, szerokosc, wysokosc):
        try:
            self.okno = pygame.display.set_mode((szerokosc, wysokosc))
            return True
        except:
            print("Klasa " + nazwa_klasy + ", ustaw_rozdzielczosc(). \n" +
            "Nie można ustawić roździelczości.")
            return False

    def ustaw_logike_gry(self):
        try:
            self.inicjuj_liste_opcji()
            flaga_gry = True
            opcje = [1, 0, 0, 0]
            numer = 0
            pozycja = [0, 0]
            ruch_do_gory = [0, 1, 0, 0]
            ruch_w_dol = [0, -1, 0, 0]
            ruch_w_lewo = [-1, 0, 0, 0]
            ruch_w_prawo = [1, 0, 0, 0]
            self.dodaj_opcje(ruch_w_prawo)
            pozycja_robaka = self.generuj_tablice(-10, 10)
            print("Najbliższa pozycja robaka to", pozycja_robaka)
            waz = Waz()
            waz.wyswietl_statystyki()
            while flaga_gry:
                for wydarzenie in pygame.event.get():
                    if wydarzenie.type == pygame.QUIT:
                        flaga_gry = False
                przycisk = pygame.key.get_pressed()
                ostatnia_opcja = self.zwroc_ostatnia_opcje()
                if przycisk[pygame.K_w] and ostatnia_opcja != ruch_w_dol:
                    self.dodaj_opcje(ruch_do_gory)
                if przycisk[pygame.K_s] and ostatnia_opcja != ruch_do_gory:
                    self.dodaj_opcje(ruch_w_dol)
                if przycisk[pygame.K_a] and ostatnia_opcja != ruch_w_prawo:
                    self.dodaj_opcje(ruch_w_lewo)
                if przycisk[pygame.K_d] and ostatnia_opcja != ruch_w_lewo:
                    self.dodaj_opcje(ruch_w_prawo)
                if numer % 300 == 0:
                    if ostatnia_opcja == ruch_do_gory:
                        pozycja[1] += 1
                    if ostatnia_opcja == ruch_w_dol:
                        pozycja[1] -= 1
                    if ostatnia_opcja == ruch_w_prawo:
                        pozycja[0] += 1
                    if ostatnia_opcja == ruch_w_lewo:
                        pozycja[0] -= 1
                    print(pozycja)
                    numer = 0
                if pozycja == pozycja_robaka:
                    print("Zjałem sobie robaka rasówę.")
                    pozycja_robaka = self.generuj_tablice(-10, 10)
                    print("Najbliższa pozycja robaka to", pozycja_robaka)
                    waz.zwieksz_punkty()
                    waz.zwieksz_dlugosc()
                    waz.wyswietl_statystyki()
                numer += 1
                pygame.display.flip()
            pygame.quit()

            return True
        except:
            print("Klasa " + nazwa_klasy + ", ustaw_logike_gry(). \n" +
            "Nie można ustawić logiki gry.")
            return False

    def generuj_tablice(self, poczatek, koniec):
        try:
            pierwszy_element = random.randint(poczatek, koniec)
            drugi_element = random.randint(poczatek, koniec)
            tablica = [pierwszy_element, drugi_element]
            return tablica
        except:
            print("Klasa " + nazwa_klasy + ", metoda generuj_tabice(). \n" +
            "Nie można wygenerować tablicy..")
            return False

    def inicjuj_liste_opcji(self):
        try:
            self.lista_opcji = []
            return True
        except:
            print("Klasa " + nazwa_klasy + ", inicjuj_liste_opcji(). \n" +
            "Nie można zwrócić listy opcji.")
            return False

    def zwroc_liste_opcji(self):
        try:
            return self.lista_opcji
        except:
            print("Klasa " + nazwa_klasy + ", zwroc_liste_opcji(). \n" +
            "Nie można zwrócić listy opcji.")
            return False

    def dodaj_opcje(self, opcja):
        try:
            self.zwroc_liste_opcji().append(opcja)
            return True
        except:
            print("Klasa " + nazwa_klasy + ", dodaj_opcje(). \n" +
            "Nie można dodać opcji.")
            return False

    def zwroc_ostatnia_opcje(self):
        try:
            opcje = self.zwroc_liste_opcji()
            indeks = len(opcje) - 1
            opcja = opcje[indeks]
            return opcja
        except:
            print("Klasa " + nazwa_klasy + ", zwroc_ostatnia_opcje(). \n" +
            "Nie można zwrócić ostatniej opcji.")
            return False
