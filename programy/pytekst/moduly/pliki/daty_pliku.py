import os.path, time

class Daty_pliku:

    def __init__(self, sciezka):
        self.sciezka = sciezka

    def zwroc_date_utworzenia(self):
        return str(time.ctime(os.path.getctime(self.sciezka)))

    def zwroc_date_modyfikacji(self):
        return str(time.ctime(os.path.getmtime(self.sciezka)))
