from pytekst import *
from pystrona import *
from pyfragment import *

nazwa = "konsolidacja-dlugu"
folder_tekstow = "/home/qwerty891/Pulpit/strona_internetowa/tekst/"
folder_artykulow = "/home/qwerty891/Pulpit/strona_internetowa/artykuly/"
wejscie = folder_tekstow + nazwa + ".txt"
wyjscie = folder_artykulow + nazwa + ".html"

tekst = Tekst(wejscie, wyjscie)
tekst.ustaw_poczatek_akapitu("<p>")
tekst.zamien()
linie = tekst.zwroc_linie()

strona = PyStrona(linie)
strona_internetowa = strona.zwroc_strone()
