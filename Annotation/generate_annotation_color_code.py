#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"
# Reference for color script
# http://pillow-wiredfool.readthedocs.io/en/latest/_modules/PIL/ImageColor.html
# Http://www.rapidtables.com/web/color/RGB_Color.htm........................................LINE 2 VALUES

from PIL import Image, ImageDraw
from xml.dom import minidom

import os
from pathlib2 import Path
XML_PATH = '/home/scania/Scania/Agneev/Labels/XMLs/'
SAVE_COLOR_LABEL_PATH = '/home/scania/Scania/Agneev/Labels/Color_Labels/'
AUGMENTED_IMAGES_PATH = '/home/scania/Scania/Agneev/Labels/Images_Augmented/'
INCORRECT_FILES = ['output_0008.xml', '20170324_112630_0046.xml']

# Color for each class
ASPHALT = 'rgb(105,105,105)'
GRAVEL_H = 'rgb(112,128,144)'
GRAVEL_L = 'rgb(192,192,192)'
GRAVEL_N = 'rgb(176,196,222)'
MUD = 'rgb(139,69,19)'
MUD_N = 'rgb(210,105,30)'
SAND = 'rgb(244,164,96)'
SAND_N = 'rgb(210,180,140)'
WATER = 'rgb(106,90,205)'
WATER_N = 'rgb(0,0,255)'
SKY = 'rgb(135,206,235)'
VEGETATION = 'rgb(0,100,0)'
GRASS = 'rgb(255,255,0)'
GRASS_N = 'rgb(154,205,50)'
SNOW = 'rgb(245,222,179)'
SNOW_N = 'rgb(255,255,224)'
BACKGROUND = 'rgb(0,0,0)'


for filename in os.listdir(XML_PATH):
	if not filename.endswith('.xml'): continue

	xmldoc = minidom.parse(XML_PATH+filename)
	im = Image.new('RGB', (1280, 1080))
	draw = ImageDraw.Draw(im)

	objectlist = xmldoc.getElementsByTagName('object')
	object_count = 0
	polygon_point_count = 1 # Ignore the username attribute
	points = ()
	if len(objectlist) > 0 and (filename not in INCORRECT_FILES) and ('(copy)' not in filename):
		im = Image.new('RGB', (1280, 1080))
		draw = ImageDraw.Draw(im)
		while object_count < len(objectlist):
		
			while (polygon_point_count < len(objectlist[object_count].childNodes[8].childNodes)):
				points += int(objectlist[object_count].childNodes[8].childNodes[polygon_point_count].childNodes[0].firstChild.nodeValue), int(objectlist[object_count].childNodes[8].childNodes[polygon_point_count].childNodes[1].firstChild.nodeValue)
				polygon_point_count += 1

			class_val = objectlist[object_count].childNodes[0].firstChild.nodeValue

			'''
			### FINAL PREFERRED COLORS
			if class_val == 'asphalt':
				draw.polygon(points, fill=ASPHALT)
			elif class_val == 'gravel_h' or class_val == 'gravel_d':
				draw.polygon(points, fill=GRAVEL_H)
			elif class_val == 'gravel_l' or class_val == 'gravel':
				draw.polygon(points, fill=GRAVEL_L)
			elif class_val == 'gravel_n':
				draw.polygon(points, fill=GRAVEL_N)	
			elif class_val == 'mud':
				draw.polygon(points, fill=MUD)
			elif class_val == 'mud_n':
				draw.polygon(points, fill=MUD_N)
			elif class_val == 'sand':
				draw.polygon(points, fill=SAND)
			elif class_val == 'sand_n':
				draw.polygon(points, fill=SAND_N)
			elif class_val == 'water':
				draw.polygon(points, fill=WATER)
			elif class_val == 'water_n':
				draw.polygon(points, fill=WATER_N)
			elif class_val == 'sky':
				draw.polygon(points, fill=SKY)
			elif class_val == 'vegetation':
				draw.polygon(points, fill=VEGETATION)
			elif class_val == 'grass':
				draw.polygon(points, fill=GRASS)
			elif class_val == 'grass_n':
				draw.polygon(points, fill=GRASS_N)
			elif class_val == 'snow':
				draw.polygon(points, fill=SNOW)
			elif class_val == 'snow_n':
				draw.polygon(points, fill=SNOW_N)
			else:
				draw.polygon(points, fill=BACKGROUND)
			### UNTIL HERE
			
			
			# 7 classes 1ST TRY
			if class_val == 'asphalt':
				draw.polygon(points, fill=GRASS)
			elif class_val == 'gravel_l' or class_val == 'gravel':
				draw.polygon(points, fill='rgb(0,64,0)')
			elif class_val == 'grass' or class_val == 'grass_n':
				draw.polygon(points, fill='rgb(0,255,0)')
			elif class_val == 'gravel_h' or class_val == 'gravel_d':
				draw.polygon(points, fill='rgb(255,0,0)')	
			elif class_val == 'sand' or class_val == 'sand_n':
				draw.polygon(points, fill='rgb(127,127,0)')
			elif class_val == 'mud' or class_val == 'mud_n':
				draw.polygon(points, fill='rgb(127,0,0)')
			else:
				draw.polygon(points, fill=BACKGROUND)
			'''
			# 9 classes : Drivable
			if class_val == 'asphalt':
				draw.polygon(points, fill=ASPHALT)
			elif class_val == 'gravel_h' or class_val == 'gravel_d':
				draw.polygon(points, fill=GRAVEL_H)
			elif class_val == 'gravel_l' or class_val == 'gravel':
				draw.polygon(points, fill=GRAVEL_L)
			elif class_val == 'mud':
				draw.polygon(points, fill=MUD)
			elif class_val == 'sand':
				draw.polygon(points, fill=SAND)
			elif class_val == 'water':
				draw.polygon(points, fill=WATER)
			elif class_val == 'grass':
				draw.polygon(points, fill=GRASS)
			elif class_val == 'snow':
				draw.polygon(points, fill=SNOW)
			else:
				draw.polygon(points, fill=BACKGROUND)
			'''
			# Combined: All gravel; mud + water; 10 class
			if class_val == 'asphalt':
				draw.polygon(points, fill=ASPHALT)
			elif class_val == 'gravel_l' or class_val == 'gravel' or class_val == 'gravel_h' or class_val == 'gravel_d':
				draw.polygon(points, fill=GRAVEL_L)
			elif class_val == 'gravel_n':
				draw.polygon(points, fill=GRAVEL_N)
			elif class_val == 'mud' or class_val == 'mud_n' or class_val == 'water' or class_val == 'water_n':
				draw.polygon(points, fill=MUD)
			elif class_val == 'sand' or class_val == 'sand_n':
				draw.polygon(points, fill=SAND)
			elif class_val == 'sky':
				draw.polygon(points, fill=SKY)
			elif class_val == 'vegetation':
				draw.polygon(points, fill=VEGETATION)
			elif class_val == 'grass' or class_val == 'grass_n':
				draw.polygon(points, fill=GRASS)
			elif class_val == 'snow' or class_val == 'snow_n':
				draw.polygon(points, fill=SNOW)
			else:
				draw.polygon(points, fill=BACKGROUND)
			
			
			# Only Road: All gravel; mud + water; Grass + sand; 5 class
			if class_val == 'asphalt':
				draw.polygon(points, fill=ASPHALT)
			elif class_val == 'gravel_l' or class_val == 'gravel' or class_val == 'gravel_h' or class_val == 'gravel_d' or class_val == 'gravel_n':
				draw.polygon(points, fill=GRAVEL_L)
			elif class_val == 'mud' or class_val == 'mud_n' or class_val == 'water' or class_val == 'water_n':
				draw.polygon(points, fill=MUD)
			elif class_val == 'grass' or class_val == 'grass_n' or class_val == 'sand' or class_val == 'sand_n':
				draw.polygon(points, fill=GRASS)
			else:
				draw.polygon(points, fill=BACKGROUND)
			
			'''

			polygon_point_count = 1
			points = ()
			object_count += 1

		filename = os.path.splitext(filename)[0]
		print filename
		im.save(SAVE_COLOR_LABEL_PATH+filename+'.jpg')

		# Check for augmented files with corresponding names. Mostly +-2 or +-4
		# zfill(4) to convert int(15) to str(0015)
		if filename not in ['output_0634']:
			test_file = Path(AUGMENTED_IMAGES_PATH+filename[:-4]+str(int(filename[-4:])+2).zfill(4) +'.jpg')
			if test_file.exists():
				im.save(SAVE_COLOR_LABEL_PATH+filename[:-4]+str(int(filename[-4:])+2).zfill(4)+'.jpg')
				#print test_file + 'Then'
			test_file = Path(AUGMENTED_IMAGES_PATH+filename[:-4]+str(int(filename[-4:])-2).zfill(4)+'.jpg')
			if test_file.exists():
				im.save(SAVE_COLOR_LABEL_PATH+filename[:-4]+str(int(filename[-4:])-2).zfill(4)+'.jpg')

			test_file = Path(AUGMENTED_IMAGES_PATH+filename[:-4]+str(int(filename[-4:])+4).zfill(4)+'.jpg')
			if test_file.exists():
				im.save(SAVE_COLOR_LABEL_PATH+filename[:-4]+str(int(filename[-4:])+4).zfill(4)+'.jpg')

			test_file = Path(AUGMENTED_IMAGES_PATH+filename[:-4]+str(int(filename[-4:])-4).zfill(4)+'.jpg')
			if test_file.exists():
				im.save(SAVE_COLOR_LABEL_PATH+filename[:-4]+str(int(filename[-4:])-4).zfill(4)+'.jpg')
		'''
		if class_val == 'snow':
			draw.polygon(points, outline='linen', fill='linen')
		elif class_val == 'grass':
			draw.polygon(points, outline='lightgreen', fill='lightgreen')
		elif class_val == 'sky' or class_val == 'sky_':
			draw.polygon(points, outline='lightskyblue', fill='lightskyblue')
		elif class_val == 'asphalt':
			draw.polygon(points, outline='gray', fill='gray')	
		elif class_val == 'vegetation':
			draw.polygon(points, outline='darkgreen', fill='darkgreen')
		elif class_val == 'mud':
			draw.polygon(points, outline='brown', fill='brown')
		elif class_val == 'gravel':
			draw.polygon(points, outline='darkslategray', fill='darkslategray')
		elif class_val == 'sand':
			draw.polygon(points, outline='yellow', fill='yellow')
		elif class_val == 'bus':
			draw.polygon(points, outline='red', fill='red')
		elif class_val == 'water':
			draw.polygon(points, outline='darkblue', fill='darkblue')
		elif class_val == 'fence':
			draw.polygon(points, outline='maroon', fill='maroon')
		elif class_val == 'building' or class_val == 'bulding':
			draw.polygon(points, outline='pink', fill='pink')
		elif class_val == 'truck':
			draw.polygon(points, outline='red', fill='red') # same as bus
		'''
		'''
		if class_val == 'snow':
			draw.polygon(points, fill='rgb(102,0,0)')
		elif class_val == 'grass':
			draw.polygon(points, fill='rgb(102,51,0)')
		elif class_val == 'sky' or class_val == 'sky_':
			draw.polygon(points, fill='rgb(102,102,0)')
		elif class_val == 'asphalt':
			draw.polygon(points, fill='rgb(51,102,0)')	
		elif class_val == 'vegetation':
			draw.polygon(points, fill='rgb(0,102,0)')
		elif class_val == 'mud':
			draw.polygon(points, fill='rgb(0,102,51)')
		elif class_val == 'gravel':
			draw.polygon(points, fill='rgb(0,102,102)')
		elif class_val == 'sand':
			draw.polygon(points, fill='rgb(0,51,102)')
		#elif class_val == 'bus':
		#	draw.polygon(points, fill='rgb(0,0,102)')
		elif class_val == 'water':
			draw.polygon(points, fill='rgb(51,0,102)')
		#elif class_val == 'fence':
		#	draw.polygon(points, fill='rgb(102,0,102)')
		#elif class_val == 'building' or class_val == 'bulding':
		#	draw.polygon(points, fill='rgb(102,0,51)')
		#elif class_val == 'truck':
		#	draw.polygon(points, fill='rgb(32,32,32)') # same as bus

		'''