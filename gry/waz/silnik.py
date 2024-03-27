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
            flaga_gry = True

            while flaga_gry:
                for wydarzenie in pygame.event.get():
                    if wydarzenie.type == pygame.QUIT:
                        flaga_gry = False
                pygame.display.flip()
            pygame.quit()

            return True
        except:
            print("Klasa " + nazwa_klasy + ", ustaw_logike_gry(). \n" +
            "Nie można ustawić logiki gry.")
            return False
