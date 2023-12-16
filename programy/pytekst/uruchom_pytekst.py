from pytekst import *

wejscie = "/home/qwerty891/Pulpit/strona_internetowa/tekst/kredyt-w-mbanku.txt"
wyjscie = "/home/qwerty891/Pulpit/strona_internetowa/tekst/kredyt-w-mbanku.html"

tekst = Tekst(wejscie, wyjscie)
tekst.ustaw_poczatek_akapitu("<p>")
tekst.zamien()
linie = tekst.zwroc_linie()
print(linie)
