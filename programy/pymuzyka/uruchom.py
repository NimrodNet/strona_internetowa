import os
from gamy.gamy_podstawowe import *
from wykresy.czerwona_fala import *

class Pymuzyka:

    def ustaw_czestotliwosc(self, czestotliwosc):
        self.czestotliwosc = czestotliwosc

    def ustaw_czas(self, czas):
        self.czas = czas

    def zwroc_czestotliwosc(self):
        return self.czestotliwosc

    def zwroc_czas(self):
        return self.czas

    def stworz_dzwiek(self, wyjscie):
        czestotliwosc = self.zwroc_czestotliwosc()
        czas = self.zwroc_czas()
        polecenie = "ffmpeg -f lavfi -i \"sine=frequency=" + czestotliwosc + ":duration=" + czas + "\" " + wyjscie
        os.system(polecenie)

class Mikser:

    def __init__(self):
        self.muzyka = Pymuzyka()

    def stworz_dzwiek(self, czestotliwosc, czas, nazwa):
        muzyka = self.muzyka
        muzyka.ustaw_czestotliwosc(czestotliwosc)
        muzyka.ustaw_czas(czas)
        muzyka.stworz_dzwiek(nazwa)

class Mikser_dzwiekow:

    def stworz_dzwiek(self, nazwa, czestotliwosc):
        mikser = Mikser()
        czas_dzwieku = "1"
        folder = "doremi/"
        mikser.stworz_dzwiek(czestotliwosc, czas_dzwieku, folder + nazwa)

    def polacz_dzwieki(self, plik, nazwa):
        komenda = "ffmpeg -f concat -safe 0 -i " + plik + " -c copy " + nazwa
        os.system(komenda)

gamy = Gamy_podstawowe()
mikser = Mikser_dzwiekow()

#mikser.stworz_dzwiek("gama_ch4.wav", gamy.Ch4())
#mikser.stworz_dzwiek("gama_d4.wav", gamy.D4())
#mikser.stworz_dzwiek("gama_dh4.wav", gamy.Dh4())
#mikser.stworz_dzwiek("gama_e4.wav", gamy.E4())
#mikser.stworz_dzwiek("gama_f4.wav", gamy.F4())
#mikser.stworz_dzwiek("gama_fh4.wav", gamy.Fh4())
#mikser.stworz_dzwiek("gama_g4.wav", gamy.G4())
#mikser.stworz_dzwiek("gama_gh4.wav", gamy.Gh4())

mikser.polacz_dzwieki("doremi/doremi.txt", "doremi.wav")

#fala = Czerwona_fala()
#fala.uruchom("test.wav")
