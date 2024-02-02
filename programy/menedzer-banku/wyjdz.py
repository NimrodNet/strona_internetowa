class Wyjdz:

    def __init__(self, instancja):
        try:
            instancja.quit()
        except:
            print("Plik wyjdz.py, klasa Wyjdz, metoda __init__(). Nie udało się poprawnie wyjść z aplikacji.")
