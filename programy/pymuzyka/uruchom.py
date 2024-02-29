import os

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

muzyka = Pymuzyka()
muzyka.ustaw_czestotliwosc("440")
muzyka.ustaw_czas("5")
muzyka.stworz_dzwiek("test.wav")
