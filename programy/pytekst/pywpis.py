class PyWpis:

    def __init__(self, sciezka, tytul, opis):
        self.ustaw_tytul(tytul)
        self.ustaw_sciezke(sciezka)
        self.ustaw_opis(opis)

    def ustaw_tytul(self, tytul):
        self.tytul = tytul

    def zwroc_tytul(self):
        return self.tytul

    def ustaw_sciezke(self, sciezka):
        self.sciezka = "\"" +  sciezka + "\""

    def zwroc_sciezke(self):
        return self.sciezka

    def zwroc_sciezke_z_wpisu(self, wpis):
        try:
            znacznik = "href"
            poczatek = wpis.index(znacznik) + len(znacznik) + 2
            koniec = wpis.index(">", poczatek) - 1
            sciezka = wpis[poczatek:koniec]
            return sciezka
        except:
            print("PyWpis, zwroc_sciezke(wpis): nie można zwrócić ścieżki.")

    def ustaw_opis(self, opis):
        self.opis = opis

    def zwroc_opis(self):
        return self.opis

    def zwroc_wpis(self):
        try:
            wpis = """
<wpis>
    <img src="grafika/rrso_glowna.jpeg" alt="RRSO"/>
    <tytul>""" + self.zwroc_tytul() + """</tytul>
    <opis>""" + self.zwroc_opis() + """
    </opis>
    <a class="przycisk" href=""" +  self.zwroc_sciezke() + """>Więcej</a>
</wpis>
"""
            return wpis
        except:
            print("PyWpis, zwroc_wpis(): nie można zwrócić wpisu.")
