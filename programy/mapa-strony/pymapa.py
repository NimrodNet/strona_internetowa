import os
from moduly.pliki.zapisz_plik import *
from moduly.pliki.wszystkie_pliki import *

class PyMapa:

    def __init__(self, domena, sciezka):
        self.ustaw_domene(domena)
        self.sciezka = str(sciezka)
        self.mapa_strony = str("")
        self.ustaw_poczatek_sciezki(sciezka)
        self.pobierz_pliki()
        self.konstruuj_linki()
        self.konstruuj_mape()

    def ustaw_domene(self, domena):
        self.domena = str(domena)

    def ustaw_poczatek_sciezki(self, poczatek):
        self.poczatek_sciezki = str(poczatek)

    def pobierz_pliki(self):
        rozszerzenia = {".html", ".mp4", ".txt"}
        wszystkie_pliki = Wszystkie_pliki(self.sciezka)
        pliki = wszystkie_pliki.zwroc_pliki(rozszerzenia)
        self.pliki = []
        for sciezki in pliki:
            for sciezka in sciezki:
                self.pliki.append(sciezka)

    def pobierz_plik(self, indeks):
        return self.pliki[indeks]

    def konstruuj_linki(self):
        self.linki = []
        sciezki = self.pliki
        for sciezka in sciezki:
            link = self.konstruuj_link(sciezka)
            link = link.replace(self.poczatek_sciezki, "")
            self.linki.append(link)

    def konstruuj_link(self, sciezka):
        return str(self.domena) + str(sciezka)

    def konstruuj_mape(self):
        mapa = ""
        poczatek = self.zwroc_poczatek_mapy_strony()
        koniec = self.zwroc_koniec_mapy_strony()
        mapa += poczatek + "\n"
        for link in self.linki:
            parametry = {str(link)}
            element = self.konstruuj_element(link)
            mapa += str(element)
        mapa += koniec + "\n"
        self.mapa_strony = mapa
        
    def konstruuj_element(cls, link):
        element = str("<url><loc>") + link + str("</loc></url>\n")
        return element

    def zwroc_poczatek_mapy_strony(cls):
        mapa_strony = str("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
        mapa_strony += str("<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">")
        return mapa_strony

    def zwroc_koniec_mapy_strony(cls):
        mapa_strony = str("</urlset>")
        return mapa_strony

    def zapisz_mape_strony(self):
        zapisywanie = Zapisz_plik(self.sciezka + "/mapa-strony.xml")
        mapa_strony = str(self.mapa_strony)
        zapisywanie.zapisz(mapa_strony)

domena = input("Podaj nazwę domeny: ")
sciezka = input("Podaj ścieżkę: ")

mapa_strony = PyMapa(domena, sciezka)
mapa_strony.zapisz_mape_strony()