import random
import sys
import os
import zlib
import PIL

from PIL import Image

im = Image.open("Photos\\photo.jpg")
pix = im.load()
print(im.size)
print(pix[899, 899])

for y in range(0, im.height):
   for x in range(0, im.width):
        print(pix[x, y], "Pixel located at ", x, ",", y)
        if pix[x,y] == (65, 95, 85):
            print(pix[x, y])


