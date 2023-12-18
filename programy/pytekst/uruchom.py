from pytekst import *
from pystrona import *
from pyfragment import *


nazwa = "zielona-zima"
wejscie = nazwa + ".txt"
wyjscie = nazwa + ".html"

tekst = Tekst(wejscie, wyjscie)
tekst.ustaw_poczatek_akapitu("<p>")
tekst.zamien()
linie = tekst.zwroc_linie()

strona = PyStrona(tekst)
naglowek = strona.zwroc_naglowek()
stopka = strona.zwroc_stopke()
print(stopka)
