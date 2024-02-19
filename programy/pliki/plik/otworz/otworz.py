class Otworz:

    def __init__(self, lokalizacja):
        try:
            self.lokalizacja = lokalizacja
        except:
            print("Nie można otworzyć pliku " + lokalizacja)
