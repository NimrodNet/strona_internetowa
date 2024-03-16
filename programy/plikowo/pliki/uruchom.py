from stworz_plik import *
from czytaj_plik import *
from zapisz_plik import *
from usun_plik import *

stworz = Stworz_plik()
stworz.wykonaj("plik.txt")

zapisz = Zapisz_plik()
zapisz.wykonaj("plik.txt", "Witaj, pliku.")

czytaj = Czytaj_plik()
wiadomosc = czytaj.wykonaj("plik.txt")
print(wiadomosc)

usun = Usun_plik()
usun.wykonaj("plik.txt")
