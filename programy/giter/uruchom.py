import os

class Giter:

    def inicjuj(self):
        self.wykonaj("git init")

    def dodaj(self):
        self.wykonaj("git add .")

    def wiadomosc(self, informacja):
        self.wykonaj("git commit -m " + str(informacja))

    def dodaj_z_wiadomoscia(self, informacja):
        self.wykonaj("git commit -a -m " + str(informacja))

    def wczytaj(self):
        self.wykonaj("git push origin master")

    def wykonaj(cls, polecenie):
        os.system(polecenie)
