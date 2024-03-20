import requests

class Wyswietl_kod_strony:

    def wykonaj(self, link):
        try:
            strona = requests.get(link)
            kod = strona.text
            return kod
        except:
            print("Klasa Wyswietl_kod_strony, metoda wykonaj. \n" +
            "Nie można pobrać kodu strony internetowej.")
            return False
