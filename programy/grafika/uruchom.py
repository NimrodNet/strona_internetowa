import sys
from PIL import Image, ImageDraw

tlo = "rgb(255,255,254)"
rozdzielczosc = (300, 300)

proksy = (100, 100)
punkt = "rgb(0,0,0)"

image = Image.new("RGB", rozdzielczosc, tlo)

rysunek = ImageDraw.Draw(image)
rysunek.point(proksy, punkt)


image.save("wyjscie.png")
image.show()
