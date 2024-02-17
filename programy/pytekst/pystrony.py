from pytekst import *
from pystrona import *
from pyfragment import *
from pypliki import *

class PyStrony:

    def __init__(self, wejscie, wyjscie):
        self.zamien_tekst_na_strony(wejscie, wyjscie)

    def zamien_tekst_na_strony(self, wejscie, wyjscie):
        sciezka = wejscie
        sciezka_wyjsciowa = wyjscie
        pypliki = PyPliki(sciezka)
        rozszerzenia = {".txt"}
        pliki = pypliki.zwroc_pliki_z_rozszerzeniami(rozszerzenia)
        for plik in pliki:
            wejscie = str(plik)
            pypliki.ustaw_sciezke(wejscie)
            nazwa = pypliki.zwroc_nazwe_pliku_bez_rozszerzenia()
            wyjscie = sciezka_wyjsciowa + nazwa + ".html"
            pytekst = PyTekst(wejscie, wyjscie)
            tekst = pytekst.zwroc_linie()
            pystrona = PyStrona(tekst)
            strona_internetowa = pystrona.zwroc_strone()
            pypliki.ustaw_sciezke(wyjscie)
            strona_nie_istnieje = not pypliki.plik_istnieje()
            if strona_nie_istnieje:
                pypliki.zapisz_plik(strona_internetowa)
