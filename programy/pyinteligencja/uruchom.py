import random

class Uruchom:

    def __init__(self):
        self.liczby = []
        self.znaki = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        jezyk = "polski"
        szukam = "100"
        ciag_znakow = "tak"
        pojedynczo = "tak"
        porownac = "tak"
        iteracyjnie = "tak"
        wiadomosc = "Napisz liczbę sto w formie liczbowej."
        self.szukana_liczba = ""
        self.zwroc_wartosc()

    def zwroc_wartosc(self):
        liczba_znakow = "0"
        liczba_znakow = len(self.znaki)
        for znak in self.znaki:
            print("Znak: " + znak)
            for indeks in range(3):
                aktualny_znak = "0"
                aktualny_znak = znak
                liczba_losowa = random.randint(0, 3)
                print(liczba_losowa)
        print(self.szukana_liczba)

Uruchom()
