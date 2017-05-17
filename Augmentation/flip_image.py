#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

# Flips pictures left to right and save with _R

import random, os, time 
from PIL import Image 

IMAGE_PATH = "/home/scania/Scania/Agneev/Labels/Color_Labels/"

image_files = os.listdir(IMAGE_PATH) 

t = time.time() 
for file in image_files: 
	print file
	with Image.open(os.path.join(IMAGE_PATH, file)) as im: 
		im2 = im.transpose(Image.FLIP_LEFT_RIGHT)
		im2.save(IMAGE_PATH + file.split('.')[0] + '_R.png') 

t = time.time()-t 
print("Done")