from pobierz_liste_plikow import *

nazwa_folderu = "folderu/"

lista_plikow = Pobierz_liste_plikow()
pliki = lista_plikow.wykonaj(nazwa_folderu)
print(pliki)
