#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

'''
Set the incorrect color codes in the ground truth to background
'''
from PIL import Image, ImageDraw
import os
import numpy as np

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

DRIVABLE = (0,255,0)
NON_DRIVABLE = (255,0,0)
path = '/media/scania/iQMatic_2/Agneev_Digits/Datasets/3-Classes_6820-Images/Test/Labels/'

for filename in os.listdir(path):
	if not (filename.endswith('.bmp')): continue
	im = Image.open(path + filename)
	rgb_im = im.convert('RGB')
	
	w, h = rgb_im.size #Get the width and hight of the image for iterating over 

	for a in range(w): 
		for b in range(h):
			value = rgb_im.getpixel((a,b))
			if value in (ASPHALT, GRAVEL_H, GRAVEL_L, MUD, SAND, WATER, GRASS, SNOW):
				rgb_im.putpixel((a,b),DRIVABLE)
			elif value in (GRAVEL_N, MUD_N, SAND_N, SKY, VEGETATION, GRASS_N, SNOW_N):
				rgb_im.putpixel((a,b),NON_DRIVABLE)
			else:
				rgb_im.putpixel((a,b),BACKGROUND)
	rgb_im.save(path + filename)
	print filename
