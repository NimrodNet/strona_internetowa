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

    def pobierz_galaz_lokalna(self):
        return self.wykonaj("git branch")

    def lista_galezi(self):
        self.wykonaj("git branch")

    def stworz_galaz(self, nazwa):
        self.wykonaj("git checkot -b " + nazwa)

    def przelacz_galaz(self, nazwa):
        self.wykonaj("git checkout " + nazwa)

    def polacz_galezie(self):
        self.wykonaj("git pull")

    def scal_galezie(self, nazwa):
        self.wykonaj("git merge " + nazwa)

    def usun_galaz_zdalna(self, nazwa):
        self.wykonaj("git push origin --delete " + nazwa)

    def usun_galaz_lokalna(self, nazwa):
        self.wykonaj("git branch -d " + nazwa)

    def wczytaj(self):
        self.wykonaj("git push")

    def wykonaj(cls, polecenie):
        os.system(polecenie)

class Automat:

    def wykonaj(cls):
        giter = Giter()
        giter.inicjuj()
        giter.dodaj()
        giter.wiadomosc("Giter_-_aktualizacja")
        giter.wczytaj()

automat = Automat()
automat.wykonaj()
