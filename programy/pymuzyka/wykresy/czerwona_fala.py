import os

class Czerwona_fala:

    def uruchom(self, wejscie, wyjscie = "wykres.png"):
        polecenie = "ffmpeg -i " + wejscie + " -filter_complex showwavespic -frames:v 1 " + wyjscie
        os.system(polecenie)
