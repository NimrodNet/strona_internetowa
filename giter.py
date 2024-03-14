import os

class Giter:

    def instaluj_na_linuksie(self):
        self.wykonaj("sudo apt-get update")
        self.wykonaj("sudo apt-get install git")

    def wersja(self):
        self.wykonaj("git --version")

    def utworz_klucz_na_linuksie(self, email):
        self.wykonaj("ssh-keygen -t rsa -b 4096 -C " + email)

    def sprawdz_wywolanie(self):
        self.wykonaj("eval \"(ssh-agent -s)\"")

    def archiwum(self):
        self.wykonaj("git archive --format=tar HEAD")

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

    def lista_zdalnych_galezi(self):
        self.wykonaj("git branch -r")

    def lista_wszystkich_galezi(self):
        self.wykonaj("git branch -a")

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

    def status(self):
        self.wykonaj("git status")

    def zmiany(self):
        self.wykonaj("git log")

    def cofnij_zmiany(self):
        self.wykonaj("git checkout .")

    def kopiuj(self, repozytorium):
        self.wykonaj("git clone " + repzytorium)

    def kopiuj_do_folderu(self, repozytorium, folder):
        self.wykonaj("git clone " + repozytorium + " " + folder)

    def kopiuj_tag(self, repozytorium, tag):
        self.wykonaj("git clone --branch " + tag + " " + repozytorium)

    def kopiuj_od_wczytania(self, repozytorium, numer_wiadomosci):
        self.wykonaj("git clone -depth=" + numer_wiadomosci + " " + repozytorium)

    def ustaw_email(self, adres_email):
        self.wykonaj("git config --global user.email " + adres_email)

    def ustaw_uzytkownika(self, uzytkownik):
        self.wykonaj("git config --global user.name " + uzytkownik)

    def ustaw_edytor(self, edytor):
        self.wykonaj("git config --global code.editor " + edytor)

    def ustaw_tag(self, tag):
        self.wykonaj("git tag " + tag)

    def zmiany_pliku(self, nazwa):
        self.wykonaj("git blame " + nazwa)

    def wyczysc(self):
        self.wykonaj("git clean -n")

    def wyczysc_pamiec(self):
        self.wykonaj("git clean -f")

    def na_koniec(self):
        self.wykonaj("git revert HEAD")

    def cofnij_zmiany(self):
        self.wykonaj("git reset")

    def resetuj(self):
        self.wykonaj("git reset --hard")

    def resetuj_i_zapisz(self):
        self.wykonaj("git reset --soft")

    def resetuj_wczytanie(self, wczytanie):
        self.wykonaj("git reset --soft " + wczytanie)

    def usun_wczytanie(self, numer_wczytania_od_gory):
        self.wykonaj("git reset --hard HEAD~" + numer_wczytania_od_gory)

    def usun_plik(self, plik):
        self.wykonaj("git rm " + plik)

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
