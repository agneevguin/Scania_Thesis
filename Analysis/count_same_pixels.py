#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

from PIL import Image, ImageDraw
import os

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

path = '/media/scania/iQMatic_2/Agneev_Digits/Datasets/16-Classes_9548-Images/Train/Labels/'

asp = 0
grh = 0
grl = 0
grn = 0
mdd = 0
mdn = 0
sad = 0
san = 0
wat = 0
skk = 0
veg = 0
gra = 0
grn = 0
sno = 0
snn = 0
bkk = 0
bad = 0


for filename in os.listdir(path):
	if not (filename.endswith('.bmp')): continue
	im = Image.open(path + filename)
	print filename
	for class_val in im.getdata():
		if class_val == ASPHALT:
			asp += 1
		elif class_val == GRAVEL_H:
			grh += 1
		elif class_val == GRAVEL_L:
			grl += 1
		elif class_val == GRAVEL_N:
			grn += 1
		elif class_val == MUD:
			mdd += 1
		elif class_val == MUD_N:
			mdn += 1
		elif class_val == SAND:
			sad += 1
		elif class_val == SAND_N:
			san += 1
		elif class_val == WATER:
			wat += 1
		elif class_val == SKY:
			skk += 1
		elif class_val == VEGETATION:
			veg += 1
		elif class_val == GRASS:
			gra += 1
		elif class_val == GRASS_N:
			grn += 1
		elif class_val == SNOW:
			sno += 1
		elif class_val == SNOW_N:
			snn += 1
		elif class_val == BACKGROUND:
			bkk += 1
		else:
			bad += 1

print path
print '---'
print asp
print grh
print grl
print mdd
print sad
print wat
print gra
print sno
print '---NON---'
print grn
print mdn
print san
print skk
print veg
print grn
print snn
print '---BKK---'
print bkk
print bad
print '---'