from menedzer import *

class Uruchom:

    def __init__(self):
        try:
            MenedzerBanku()
        except:
            print("Plik uruchom.py. Nie udało się uruchomić aplikacji.")

Uruchom()
