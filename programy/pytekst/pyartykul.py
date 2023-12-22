import pathlib
import datetime
import os
import platform

class PyArtykul:

    def __init__(self, sciezka):
        self.ustaw_sciezke(sciezka)

    def ustaw_sciezke(self, sciezka):
        self.sciezka = sciezka

    def zwroc_sciezke(self):
        return self.sciezka
    
    def zwroc_date_modyfikacji(self):
        try:
            sciezka = self.zwroc_sciezke()
            sciezka_pliku = pathlib.Path(sciezka)
            data_modyfikacji = sciezka_pliku.stat().st_mtime
            data = datetime.datetime.fromtimestamp(data_modyfikacji)
            return data
        except:
            print("PyArtykul, zwroc_date_modyfikacji(): nie można zwrócić daty modyfikacji.")
            return ""
