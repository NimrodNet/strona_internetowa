from pytekst import *

wejscie = input("Podaj plik wejściowy: ")
wyjscie = input("Podaj plik wyjściowy: ")

tekst = Tekst(wejscie, wyjscie)
tekst.ustaw_poczatek_akapitu("<p>")
tekst.zamien()
linie = tekst.zwroc_linie()
print(linie)
