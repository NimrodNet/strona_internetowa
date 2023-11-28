from pytekst import *

wejscie = "../../tekst/zakladanie-firmy.txt"
wyjscie = "../../tekst/zakladanie-firmy.html"

tekst = Tekst(wejscie, wyjscie)
tekst.ustaw_poczatek_akapitu("<p>")
tekst.zamien()
linie = tekst.zwroc_linie()
print(linie)
