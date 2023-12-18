class PyStrona:

    def __init__(self, tekst):
        tytul = "Szablon"
        opis = "Szablon"
        slowa_kluczowe = "szablon, html, szablon html"
        self.ustaw_tytul(tytul)
        self.ustaw_opis(opis)
        self.ustaw_slowa_kluczowe(slowa_kluczowe)
        self.ustaw_tekst(tekst)

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


    def ustaw_tytul(self, tytul):
        self.tytul = tytul

    def ustaw_opis(self, opis):
        self.opis = opis

    def ustaw_slowa_kluczowe(self, slowa_kluczowe):
        self.slowa_kluczowe = slowa_kluczowe

    def ustaw_tekst(self, tekst):
        self.tekst = tekst

    def zwroc_tytul(self):
        return self.tytul

    def zwroc_opis(self):
        return self.opis

    def zwroc_slowa_kluczowe(self):
        return self.slowa_kluczowe
