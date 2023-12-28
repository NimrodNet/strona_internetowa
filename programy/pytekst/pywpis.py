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
        self.sciezka = sciezka

    def zwroc_sciezke(self):
        return self.sciezka

    def ustaw_opis(self, opis):
        self.opis = opis

    def zwroc_opis(self):
        return self.opis

    def zwroc_wpis(self):
        wpis = """
<wpis>
    <img src="grafika/boze-narodzenie-2023.jpeg" alt="Boże Narodzenie 2023"/>
    <tytul>""" + self.zwroc_tytul() + """</tytul>
    <opis>""" + self.zwroc_opis() + """
    </opis>
    <a class="przycisk" href=""" + "\"" + self.zwroc_sciezke() + "\"" + """>Więcej</a>
</wpis>
"""
        return wpis
