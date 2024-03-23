from pliki.wyswietl_kod_strony import *

strona = "http://www.ilewazy.pl/"
wyswietl = Wyswietl_kod_strony()
kod_strony = wyswietl.wykonaj(strona)
print(kod_strony)
