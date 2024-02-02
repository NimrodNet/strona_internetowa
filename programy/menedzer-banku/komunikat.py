class Komunikat:

    def ustaw_nazwe_pliku(self, nazwa_pliku):
        try:
            self.nazwa_pliku = nazwa_pliku
        except:
            self.komunikat_wewnatrz("ustaw_nazwe_pliku()", 
            "Błąd podczas ustawiania nazwy pliku.")

    def ustaw_nazwe_klasy(self, nazwa_klasy):
        try:
            self.nazwa_klasy = nazwa_klasy
        except:
            self.komunikat_wewnatrz("ustaw_nazwe_klasy()",
            "Błąd podczas ustawienia nazwy klasy.")

    def ustaw_nazwe_metody(self, nazwa_metody):
        try:
            self.nazwa_metody = nazwa_metody
        except:
            self.komunikat_wewnatrz("ustaw_nazwe_metody()",
            "Błąd podczas ustawiania nazwy metody.")

    def ustaw_wiadomosc(self, wiadomosc):
        try:
            self.wiadomosc = wiadomosc
        except:
            self.komunikat_wewnatrz("ustaw_wiadomosc()",
            "Błąd podczas ustawiania wiadomości.")

    def zwroc_nazwe_pliku(self):
        try:
            return self.nazwa_pliku
        except:
            self.komunikat_wewnatrz("zwroc_nazwe_pliku()",
            "Nie udało się zwrócić poprawnie nazwy pliku.")
            return ""

    def zwroc_nazwe_klasy(self):
        try:
            return self.nazwa_klasy
        except:
            self.komunikat_wewnatrz("zwroc_nazwe_klasy()",
            "Nie udało się zwrócić nazwy klasy.")

    def zwroc_nazwe_metody(self):
        try:
            return self.nazwa_metody
        except:
            self.komunikat_wewnatrz("zwroc_nazwe_metody()",
            "Nie udało się zwrócić nazwy metody.")

    def zwroc_wiadomosc(self):
        try:
            return self.zwroc_wiadomosc
        except:
            self.komunikat_wewnatrz("zwroc_wiadomosc(),
            "Nie udało się zwrócić wiadomości.")

    def komunikat_wewnatrz(self, metoda, wiadomosc):
        print("Plik komunikat.py, klasa Komunikat, metoda " + 
        metoda + ". " + wiadomosc)
