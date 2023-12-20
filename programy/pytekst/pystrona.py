from moduly.pliki.zapisz_plik import *

class PyStrona:

    def __init__(self, tekst):
        tytul = tekst.splitlines()[1]
        opis = tekst.splitlines()[4]

        self.ustaw_tytul(tytul)
        self.ustaw_opis(opis)
        self.stworz_slowa_kluczowe()
        self.ustaw_tekst(tekst)
        self.stworz_strone()

    def zwroc_naglowek(self):
        return """
<!-- Początek strony html -->
<!DOCTYPE html>
<html>
<!-- Początek sekcji nagłówka -->
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Silniki wyszukiwania -->
<meta name="robots" content="index,follow">
<meta name="googlebot" content="index,follow">
<!-- Favicon -->
<link rel="icon" sizes="192x192" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
<link rel="mask-icon" href="favicon.svg" color="blue">
<!-- Tytuł strony  -->
<title>""" + self.zwroc_tytul() + """</title>
<meta name="description" content=\"""" + self.zwroc_opis() +  """\">
<meta name="keywords" content=\"""" + self.zwroc_slowa_kluczowe() +  """\">
<meta name="author" content="o-autorze.txt">

<!-- Style CSS -->
<link rel="stylesheet" href="../css/stylus/moduly/blog/blog.css">
</head>
<!-- Koniec sekcji nagłówka -->"""

    def zwroc_stopke(self):
        return """<stopka>Copyright ©. Wszelkie praca zastrzeżone.</stopka>"""

    def stworz_slowa_kluczowe(self):
        tytul = self.zwroc_tytul()
        slowa_kluczowe = tytul.split()
        ilosc = len(slowa_kluczowe)
        indeks = 0
        slowa = ""
        while indeks < ilosc:
            slowo = slowa_kluczowe[indeks]
            slowa += slowo.lower()
            if indeks < ilosc - 1:
                slowa += ", "
            indeks += 1
        slowa += ", " + tytul.lower()
        self.slowa_kluczowe = slowa

    def ustaw_tytul(self, tytul):
        self.tytul = tytul

    def ustaw_opis(self, opis):
        self.opis = opis

    def ustaw_slowa_kluczowe(self, slowa_kluczowe):
        self.slowa_kluczowe = slowa_kluczowe

    def ustaw_tekst(self, tekst):
        self.tekst = """
<body>

<naglowek>
<tytul>W przeszłości</tytul>
<opis>Blog</opis>
<naglowek>

<nawigacja>
<a href="../index.html">Strona główna</a>
<a href="../o-nas.html">O nas</a>
<a href="../kontakt.html">Kontakt</a>
<a href="../wsparcie.html">Wsparcie</a>
</nawigacja>

<artykul>
    <img src="../grafika/rrso_artykul.jpeg" alt="RRSO"/>
    <tytul>""" + self.zwroc_tytul() + """</tytul>
    <tekst>
        """ + tekst + """
    </tekst>
</artykul>

""" + self.zwroc_stopke() + """

</body>

</head>
"""

    def stworz_strone(self):
        self.strona = self.zwroc_naglowek() + self.zwroc_tekst()

    def zwroc_strone(self):
        return self.strona

    def zwroc_tytul(self):
        return self.tytul

    def zwroc_opis(self):
        return self.opis

    def zwroc_slowa_kluczowe(self):
        return self.slowa_kluczowe

    def zwroc_tekst(self):
        return self.tekst
