#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"
# Reference for color script
# http://pillow-wiredfool.readthedocs.io/en/latest/_modules/PIL/ImageColor.html


from PIL import Image, ImageDraw
from xml.dom import minidom

import os
path = '/home/scania/Scania/Agneev/Labels/XMLs'
for filename in os.listdir(path):
	if not filename.endswith('.xml'): continue
	#print filename

	xmldoc = minidom.parse(path+'/'+filename)
	im = Image.new('L', (1280, 1080))
	draw = ImageDraw.Draw(im)

	objectlist = xmldoc.getElementsByTagName('object')
	#print(len(objectlist)) # number of segments in image
	if len(objectlist) > 0:
		#print ((objectlist[0].childNodes[0].firstChild.nodeValue))  # name of object, mud
		#print (len(objectlist[0].childNodes[8].childNodes)-1) # number of points in polygon (removing the username)
		#print ((objectlist[0].childNodes[8].childNodes[1].childNodes[0].firstChild.nodeValue)) # x value
		#print ((objectlist[0].childNodes[8].childNodes[1].childNodes[1].firstChild.nodeValue)) # y value

		object_count = 0
		polygon_point_count = 1 # as we ignore the username attribute
		points = ()

		while object_count < len(objectlist):
			while (polygon_point_count < len(objectlist[object_count].childNodes[8].childNodes)):
				points += int(objectlist[object_count].childNodes[8].childNodes[polygon_point_count].childNodes[0].firstChild.nodeValue), int(objectlist[object_count].childNodes[8].childNodes[polygon_point_count].childNodes[1].firstChild.nodeValue)
				polygon_point_count += 1
			#print points
			class_val = objectlist[object_count].childNodes[0].firstChild.nodeValue
			if class_val == 'snow':
				draw.polygon(points, outline=13, fill=13)
			elif class_val == 'grass':
				draw.polygon(points, outline=12, fill=12)
			elif class_val == 'asphalt':
				draw.polygon(points, outline=11, fill=11)	
			elif class_val == 'mud':
				draw.polygon(points, outline=10, fill=10)
			elif class_val == 'sand':
				draw.polygon(points, outline=9, fill=9)
			elif class_val == 'gravel':
				draw.polygon(points, outline=8, fill=8)
			elif class_val == 'vegetation':
				draw.polygon(points, outline=7, fill=7)
			elif class_val == 'sky':
				draw.polygon(points, outline=6, fill=6)
			elif class_val == 'bus':
				draw.polygon(points, outline=5, fill=5)
			elif class_val == 'water':
				draw.polygon(points, outline=4, fill=4)
			elif class_val == 'fence':
				draw.polygon(points, outline=3, fill=3)
			elif class_val == 'building':
				draw.polygon(points, outline=2, fill=2)
			elif class_val == 'truck':
				draw.polygon(points, outline=1, fill=1) # same as bus
			polygon_point_count = 1
			points = ()
			object_count += 1

		filename = os.path.splitext(filename)[0]
		print filename
		im.save(filename+'.png')
