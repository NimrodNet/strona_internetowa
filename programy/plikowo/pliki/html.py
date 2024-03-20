class Html:

    def paragraf(cls):
        try:
            return "<p>"
        except:
            print("Klasa Html, metoda paragraf(). \n" +
            "Nie można zwrócić paragrafu.")
            return False

    def zakoncz_paragraf(cls):
        try:
            return "</p>"
        except:
            print("Klasa Html, metoda zakoncz_paragraf(). \n" + 
            "Nie można zwrócić zakończenia paragrafu.")
            return False

    def poczatek_html(cls):
        try:
            return "<html>"
        except:
            print("Klasa Html, metoda poczatek_html(). \n" + 
            "Nie można zwrócić początku html.")
            return False

    def koniec_html(cls):
        try:
            return "</html>"
        except:
            print("Klasa Html, metoda koniec_html(). \n" + 
            "Nie można zwrócić zakończenia html.")
            return False

    def poczatek_sekcji_meta(cls):
        try:
            return "<head>"
        except:
            print("Klasa Html, metoda poczatek_sekcji_meta(). \n" + 
            "Nie można zwrócić początku sekcji meta.")
            return False

    def koniec_sekcji_meta(cls):
        try:
            return "</head>"
        except:
            print("Klasa Html, metoda koniec_sekcji_meta(). \n" + 
            "Nie można zwrócić końca sekcji meta.")
            return False

    def poczatek_ciala(cls):
        try:
            return "<body>"
        except:
            print("Klasa Html, metoda poczatek_ciala(). \n" + 
            "Nie można zwrócić początku ciała.")
            return False

    def koniec_ciala(cls):
        try:
            return "</body>"
        except:
            print("Klasa Html, metoda koniec_ciala(). \n" + 
            "Nie można zwrócić końca ciała.")
            return False

    def poczatek_pierwszego_naglowka(cls):
        try:
            return "<h1>"
        except:
            print("Klasa Html, metoda poczatek_pierwszego_naglowka(). \n" + 
            "Nie można zwrócić początku pierwszego nagłówka.")
            return False

    def koniec_pierwszego_naglowka(cls):
        try:
            return "</h1>"
        except:
            print("Klasa Html, metoda koniec_pierwszego_naglowka(). \n" + 
            "Nie można zwrócić końca pierwszego nagłówka.")
            return False

    def poczatek_linku(cls):
        try:
            return "<a>"
        except:
            print("Klasa Html, metoda poczatek_linku(). \n" + 
            "Nie można zwrócić początku linku.")
            return False

    def koniec_linku(cls):
        try:
            return "</a>"
        except:
            print("Klasa Html, metoda koniec_linku(). \n" + 
            "Nie można zwrócić końca linku.")
            return False
