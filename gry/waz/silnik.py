import pygame

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
            while flaga_gry:
                for wydarzenie in pygame.event.get():
                    if wydarzenie.type == pygame.QUIT:
                        flaga_gry = False
                przycisk = pygame.key.get_pressed()
                if przycisk[pygame.K_w]:
                    self.dodaj_opcje(ruch_do_gory)
                if przycisk[pygame.K_s]:
                    self.dodaj_opcje(ruch_w_dol)
                if przycisk[pygame.K_a]:
                    self.dodaj_opcje(ruch_w_lewo)
                if przycisk[pygame.K_d]:
                    self.dodaj_opcje(ruch_w_prawo)
                if przycisk[pygame.K_q]:
                    print(opcje)
                if numer % 500 == 0:
                    if opcje == ruch_do_gory:
                        pozycja[1] += 1
                    if opcje == ruch_w_dol:
                        pozycja[1] -= 1
                    if opcje == ruch_w_prawo:
                        pozycja[0] += 1
                    if opcje == ruch_w_lewo:
                        pozycja[0] -= 1
                    print(pozycja)
                    numer = 0
                numer += 1
                pygame.display.flip()
            pygame.quit()

            return True
        except:
            print("Klasa " + nazwa_klasy + ", ustaw_logike_gry(). \n" +
            "Nie można ustawić logiki gry.")
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
            indeks = len(self.zwroc_liste_opcji())
            return indeks
        except:
            print("Klasa " + nazwa_klasy + ", zwroc_ostatnia_opcje(). \n" +
            "Nie można zwrócić ostatniej opcji.")
            return False
