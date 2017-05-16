#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

# Cuts random tiles from pictures 
# 
# This version works with approx. 270 tiles per second on my machine 
# (on 13.5MPx images). So 3 million tiles should take about 3 hours. 

import random, os, time 
from PIL import Image 

IMAGE_PATH = "/home/scania/Scania/Agneev/Labels/Saved_Labels/Images_Augmented_1364/"
LABEL_PATH = "/home/scania/Scania/Agneev/Labels/Saved_Labels/9_Classes_Color_Labels_1364/"
OUT_IMAGE_PATH = "/home/scania/Scania/Agneev/Labels/Saved_Labels/TESTS_RECHECK/Tiles/"
OUT_LABEL_PATH = "/home/scania/Scania/Agneev/Labels/Saved_Labels/TESTS_RECHECK/Tiles_Labels/"
if not os.path.isdir(OUT_IMAGE_PATH):
	os.mkdir(OUT_IMAGE_PATH)
if not os.path.isdir(OUT_LABEL_PATH):
	os.mkdir(OUT_LABEL_PATH)

dx = dy = 256
tilesPerImage = 20

image_files = os.listdir(IMAGE_PATH) 
label_files = os.listdir(LABEL_PATH) 
numOfImages = len(image_files) 

t = time.time() 
for file in image_files: 
	print file
	with Image.open(os.path.join(IMAGE_PATH, file)) as im: 
		for i in range(1, tilesPerImage+1): 
			newname = file.replace('.', '_{:03d}.'.format(i)) 
			w, h = im.size												# 1280x1080
			x = random.randint(w/8, (7*w/8)-dx-1) 						# width values
			y = random.randint(0, h-dy-1)			 					# height values
			z = random.randint(-10, 10)
			print("Cropping {}: {},{} -> {},{}".format(file, x,y, x+dx, y+dy))
			im_2 = im.rotate(z, expand=True)
			im_2 = im_2.crop((x,y, x+dx, y+dy))
			im_2.save(os.path.join(OUT_IMAGE_PATH, newname)) 
			if file in label_files:
				with Image.open(os.path.join(LABEL_PATH, file)) as im_l: 
					im_l = im_l.rotate(z, expand=True)
					im_l = im_l.crop((x,y, x+dx, y+dy))
					im_l.save(os.path.join(OUT_LABEL_PATH, newname)) 

t = time.time()-t 
print("Done {} images in {:.2f}s".format(numOfImages, t)) 
print("({:.1f} images per second)".format(numOfImages/t)) 
print("({:.1f} tiles per second)".format(tilesPerImage*numOfImages/t)) 