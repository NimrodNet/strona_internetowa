from pytekst import *
from pystrona import *
from pyfragment import *
from pypliki import *

sciezka = "/home/qwerty891/Pulpit/strona_internetowa/programy/pytekst/"
sciezka_wyjsciowa = "/home/qwerty891/Pulpit/strona_internetowa/programy/pytekst/wyjscie/"
pypliki = PyPliki(sciezka)
rozszerzenia = {".txt"}
pliki = pypliki.zwroc_pliki_z_rozszerzeniami(rozszerzenia)

for plik in pliki:
    wejscie = plik
    pypliki.ustaw_sciezke(wejscie)
    nazwa = pypliki.zwroc_nazwe_pliku_bez_rozszerzenia()
    wyjscie = sciezka_wyjsciowa + nazwa + ".html"
    pytekst = PyTekst(wejscie, wyjscie)
    tekst = pytekst.zwroc_linie()
    pystrona = PyStrona(tekst)
    strona_internetowa = pystrona.zwroc_strone()
    print(wyjscie)
    pypliki.zapisz_plik(strona_internetowa, wyjscie)
