class Tekst:

    def zwroc(self, indeks):
        try:
            tekst = ["Nowa gra", "Autorzy", "Wyjdź"]
            return tekst[indeks]
        except:
            print("Klasa Tekst, metoda zwroc(). \n" +
            "Nie można zwrócić tekstu.")

    def zwroc_autorow(self):
        try:
            return "Gra Wąż."
        except:
            print("Klasa Tekst, metoda zwroc_autorow(). \n" +
            "Nie można zwrócić autorów.")
            return False
