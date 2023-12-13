from datetime import datetime
from datetime import date

teraz = datetime.now()

teraz = teraz.strftime("%H:%M:%S")

dzis = date.today()
dzis = dzis.strftime("%d.%m.%y")

print("Dziś jest " + dzis + ", godz. " + teraz + "." )
