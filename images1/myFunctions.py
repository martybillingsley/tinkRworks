
from imgFunctions import *

img = makePicture('flower.jpg')
pixels = img.load()
for y in range(getHeight(img)):
    for x in range(getWidth(img)):
        setRed(img,x,y,0)
show(img)
