import os, time, datetime

class Pobierz_date_utworzenia:

    def wykonaj(self, sciezka):
        try:
            data = os.path.getctime(sciezka)
            data = datetime.datetime.fromtimestamp(data)
            rok = data.strftime("%Y")
            miesiac = data.strftime("%m")
            dzien = data.strftime("%d")
            godzina = data.strftime("%H")
            minuta = data.strftime("%M")
            sekunda = data.strftime("%S")
            data = dzien + "/" + miesiac + "/" + rok + " "
            data += godzina + ":" + minuta + ":" + sekunda
            return data
        except:
            print("Klasa Pobierz_date_utworzenia, metoda wykonaj(). \n" +
            "Nie można pobrać daty utworzenia pliku.")
            return False
