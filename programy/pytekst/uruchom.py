from pywpisy import *

pywpisy = PyWpisy()

pywpisy.zamien_tekst_na_strony()

wpis = """
<wpis>
wpis
</wpis> 
"""

#pywpisy.dodaj_wpis(wpis)
#pywpisy.aktualizuj()
#pywpisy.wyswietl_strone()

lista_wpisow = pywpisy.zwroc_liste_artykulow()
print(str(lista_wpisow))
