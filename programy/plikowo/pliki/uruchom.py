from stworz_folder import *
from usun_folder import *

from stworz_plik import *
from czytaj_plik import *
from zapisz_plik import *
from usun_plik import *

nazwa_folderu = "folder/"
nazwa_pliku = "plik.txt"

sciezka_pliku = nazwa_folderu + nazwa_pliku

stworz_folder = Stworz_folder()
stworz_folder.wykonaj(nazwa_folderu)

stworz = Stworz_plik()
stworz.wykonaj(sciezka_pliku)

zapisz = Zapisz_plik()
zapisz.wykonaj(sciezka_pliku, "Witaj, pliku.")

czytaj = Czytaj_plik()
wiadomosc = czytaj.wykonaj(sciezka_pliku)
print(wiadomosc)

#usun = Usun_plik()
#usun.wykonaj("plik.txt")

usun_folder = Usun_folder()
usun_folder.wykonaj("folder")
