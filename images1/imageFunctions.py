from PIL import Image

# returns a new RGB image of width w, height h, and color c
# color can be a three-tuple or a color name
# Ex: img = makeEmptyPicture(100,200, (255,0,0))
# Ex: img = makeEmptyPicture(100,200, 'red')
def makeEmptyPicture(w, h, c):
    im = Image.new("RGB", (w, h), c)
    return (im)

# opens and returns an Image, given a (local) filename
def makePicture(fName):
    im = Image.open(fName)
    return (im)

# shows an image in its own window within the GUI window
def show(img):
    img.show()

# GET COLORS
# returns the red value of the pixel at x,y of the img
def getRed(img, x, y):
    r = img.getpixel((x,y))[0]
    return (r)
# returns the green value of the pixel at x,y of the img
def getGreen(img, x, y):
    g = img.getpixel((x,y))[1]
    return (g)
# returns the blue value of the pixel at x,y of the img
def getBlue(img, x, y):
    b = img.getpixel((x,y))[2]
    return (b)
# returns the color (a three-tuple) of the pixsl at x,y of the img
def getColor(img, x, y):
    c = img.getPixel((x,y))
    return (c)

# given red, green, blue values, returns a color (a three-tuple)
def makeColor(r, g, b):
    c = (r,g,b)
    return (c)

# SETS COLORS
# set the red value of the pixel at x,y of the img
def setRed(img, x, y, r):
    rgb = img.getpixel((x,y))
    img.putpixel((x,y), (r,rgb[1],rgb[2]))
# set the green value of the pixel at x,y of the img
def setGreen(img, x, y, g):
    rgb = img.getpixel((x,y))
    img.putpixel((x,y), (rgb[0],g,rgb[2]))  
 # set the red value of the pixel at x,y of the img
def setBlue(img, x, y, b):
    rgb = img.getpixel((x,y))
    img.putpixel((x,y), (rgb[0],rgb[1],b))
def setColor(img, x, y, c):
    img.putpixel((x,y),c)

# returns the width of an image
def getWidth(img):
    w = img.size[0]
    return (w)

# returns the height of an image
def getHeight(img):
    h = img.size[1]
    return (h)
