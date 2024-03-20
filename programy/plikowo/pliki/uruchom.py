from pobierz_date_modyfikacji import *
from pobierz_date_utworzenia import *

sciezka = "folder/"
instancja = Pobierz_date_utworzenia()
wynik = instancja.wykonaj(sciezka)
print(wynik)

instancja = Pobierz_date_modyfikacji()
wynik = instancja.wykonaj(sciezka)
print(wynik)
