class Matematyka:

    def zwroc_srodek(self, punkty):
        try:
            punkty_srodka = []
            for punkt in punkty:
                srodek = punkt / 2
                punkty_srodka.append(srodek)
            return punkty_srodka
        except:
            print("Klasa Matematyka, metoda zwroc_srodek(). \n" +
            "Nie można ustalić i zwrócić punktów środka.")
            return False
