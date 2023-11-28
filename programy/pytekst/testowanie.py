from pytekst import *

wejscie = "../../tekst/porady.txt"
wyjscie = "../../tekst/porady.html"

tekst = Tekst(wejscie, wyjscie)
tekst.ustaw_poczatek_akapitu("<p>")
tekst.zamien()
linie = tekst.zwroc_linie()
print(linie)
