#!/usr/bin/env python3


from PIL import Image
import pytesseract as pt


def picture_1():
    picture = Image.open('picture_1.jpg')
    print(picture.mode,picture.size,picture.format)
    width = picture.size[0]
    height = picture.size[1]
    picture = picture.convert('RGB')
    array = []
    for i in range(width):
        for j in range(height):
            r,g,b = picture.getpixel((i,j))
            rgb = (r,g,b)
            array.append(rgb)
    print(array)



def picture_2():
    image = Image.open('img.png')
    #picture.show()
    pixdata = image.load()
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if pixdata[x, y][0] > 30 or pixdata[x, y][1] > 30 or pixdata[x, y][2] > 30 or pixdata[x, y][3] == 0:
                pixdata[x, y] = (255, 255, 255, 255)

    image.show()
picture_2()

