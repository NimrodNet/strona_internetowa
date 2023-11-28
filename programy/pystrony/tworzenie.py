from strona import *

indeks = Strona("index")
nazwa = indeks.zwroc_nazwe()

indeks.ustaw_tytul("Strona główna")
indeks.dodaj_css("glowny.css")
indeks.dodaj_css("dodatkowy.css")

tresc = """<tresc>
        <h1>To jest prosty generator stron</h1>
        </tresc>
        """
stopka = "<stopka>Stopka</stopka>"

indeks.ustaw_tresc(tresc)
indeks.ustaw_stopke(stopka)

indeks.generuj()

strona_html = indeks.zwroc_strone()

print(strona_html)

indeks.zapisz("index")
