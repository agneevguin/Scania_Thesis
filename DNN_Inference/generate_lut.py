#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

from PIL import Image, ImageDraw


BACKGROUND = (0,0,0)
ASPHALT = (105,105,105)
GRAVEL_H = (112,128,144)
GRAVEL_L = (192,192,192)
GRAVEL_N = (176,196,222)
MUD = (139,69,19)
MUD_N = (210,105,30)
SAND = (244,164,96)
SAND_N = (210,180,140)
WATER = (106,90,205)
WATER_N = (0,0,255)
SKY = (135,206,235)
VEGETATION = (0,100,0)
GRASS = (255,255,0)
GRASS_N = (154,205,50)
SNOW = (245,222,179)
SNOW_N = (255,255,224)


im = Image.new('RGB', (256, 1))
draw = ImageDraw.Draw(im)

x = 0
def add_one():
	global x
	x += 1
	return x

'''
# 16_Classes
im.putpixel((x,0), BACKGROUND[::-1])
im.putpixel((add_one(),0), ASPHALT[::-1])
im.putpixel((add_one(),0), GRAVEL_H[::-1])
im.putpixel((add_one(),0), GRAVEL_L[::-1])
im.putpixel((add_one(),0), GRAVEL_N[::-1])
im.putpixel((add_one(),0), MUD[::-1])
im.putpixel((add_one(),0), MUD_N[::-1])
im.putpixel((add_one(),0), SAND[::-1])
im.putpixel((add_one(),0), SAND_N[::-1])
im.putpixel((add_one(),0), WATER[::-1])
im.putpixel((add_one(),0), WATER_N[::-1])
im.putpixel((add_one(),0), SKY[::-1])
im.putpixel((add_one(),0), VEGETATION[::-1])
im.putpixel((add_one(),0), GRASS[::-1])
im.putpixel((add_one(),0), GRASS_N[::-1])
im.putpixel((add_one(),0), SNOW[::-1])
im.putpixel((add_one(),0), SNOW_N[::-1])
'''

# 9_Classes
im.putpixel((x,0), BACKGROUND[::-1])
im.putpixel((add_one(),0), ASPHALT[::-1])
im.putpixel((add_one(),0), GRAVEL_H[::-1])
im.putpixel((add_one(),0), GRAVEL_L[::-1])
im.putpixel((add_one(),0), MUD[::-1])
im.putpixel((add_one(),0), SAND[::-1])
im.putpixel((add_one(),0), WATER[::-1]
im.putpixel((add_one(),0), GRASS[::-1])
im.putpixel((add_one(),0), SNOW[::-1])



im.save('lut.png')

im = Image.open('lut.png', 'r')
pix_val = list(im.getdata())
print pix_val