from wszystkie_pliki import *

rozszerzenia = {".py"}
sciezka = "/home/qwerty891/Pulpit/"

wszystkie_pliki = Wszystkie_pliki(sciezka)
pliki = wszystkie_pliki.zwroc_wszystkie_pliki(rozszerzenia)
print(pliki)
