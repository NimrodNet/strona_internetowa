from pywpisy import *
from pywpis import *
from pyparser import *
import os

pywpisy = PyWpisy()

pywpisy.zamien_tekst_na_strony()

lista_wpisow = pywpisy.zwroc_liste_artykulow()

for sciezka in lista_wpisow:
    pyparser = PyParser(sciezka)
    pypliki = PyPliki(sciezka)
    tytul = pyparser.zwroc_tytul()
    opis = pyparser.zwroc_opis()
    sciezka = os.path.relpath(sciezka)
    sciezka = sciezka.replace("../../", "")
    pywpis = PyWpis(sciezka, tytul, opis)
    wpis = pywpis.zwroc_wpis()
    wpisy = pywpisy.zwroc_wpisy()
    wpis_istnieje = False
    for wpis_ze_strony in wpisy:
        wpis_ze_strony = "\n" + wpis_ze_strony + "\n"
        wpis_istnieje = wpis == wpis_ze_strony
        if wpis_istnieje:
            break
    dodac_nowy_wpis = not wpis_istnieje
    if dodac_nowy_wpis:
        pywpisy.dodaj_wpis(wpis)
        pywpisy.aktualizuj()
