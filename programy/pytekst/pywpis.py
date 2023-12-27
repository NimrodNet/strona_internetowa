class PyWpis:

    def __init__(self, sciezka, data):
        self.ustaw_sciezke(sciezka)
        self.ustaw_date(data)

    def ustaw_sciezke(self, sciezka):
        self.sciezka = sciezka

    def zwroc_sciezke(self):
        return self.sciezka

    def ustaw_date(self, data):
        self.data = data

    def zwroc_date(self):
        return self.data
