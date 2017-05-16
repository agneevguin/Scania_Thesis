#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

from pandas_ml import ConfusionMatrix
from PIL import Image, ImageDraw
import numpy
import os
import cv2
import matplotlib.pyplot
import pandas_ml.util.testing as tm

path_pred = '/home/scania/Scania/Agneev/Results/1011-014-5-classes-original-images/'

pixels_pred_all = []
pixels_true_all = []
basewidth = 640

for filename_pred in os.listdir(path_pred):
	if not (filename_pred.endswith('.png')): continue # or filename_pred.endswith('20170324_120648_1840.png')): continue # 20170324_120648_1239

	path_true = '/home/scania/Scania/Agneev/Labels/Color_Labels/'
	for filename_true in os.listdir(path_true):
		if not filename_true.endswith('20170324_115428_0635.png'): continue
		if filename_true.split('.')[0] == filename_pred.split('.')[0]:
			print filename_true.split('.')[0]

			im_pred = Image.open(path_pred+filename_pred).convert('RGB')
			im_true = Image.open(path_true+filename_true).convert('RGB')

			
			# Resize images for smaller values
			wpercent = (basewidth/float(im_pred.size[0]))
			hsize = int((float(im_pred.size[1])*float(wpercent)))
			im_pred = im_pred.resize((basewidth,hsize), Image.NEAREST)
			im_pred = im_pred
			wpercent = (basewidth/float(im_true.size[0]))
			hsize = int((float(im_true.size[1])*float(wpercent)))
			im_true = im_true.resize((basewidth,hsize), Image.NEAREST)
			im_true = im_true

			pixels_pred_all += list(im_pred.getdata())
			# pix_val_flat_pred = [x for sets in pix_val_pred for x in sets]

			pixels_true_all += list(im_true.getdata())
			# pix_val_flat_true = [x for sets in pix_val_true for x in sets]

# Print number of pixel count vs the colors
# print im_pred.getcolors()

# pixels_true_all = ['rabbit', 'cat', 'rabbit', 'rabbit', 'cat', 'dog', 'dog', 'rabbit', 'mouse', 'cat', 'dog', 'rabbit']
# pixels_pred_all = ['cat', 'cat', 'rabbit', 'dog', 'cat', 'rabbit', 'dog', 'cat', 'rabbit', 'cat', 'rabbit', 'rabbit']

# Print the confusion matrix
confusion_matrix = ConfusionMatrix(pixels_true_all, pixels_pred_all)
print("\nConfusion matrix:\n%s" % confusion_matrix)
confusion_matrix.plot()
confusion_matrix.plot(backend='seaborn')

with tm.assertRaises(ValueError):
	confusion_matrix.plot(backend='xxx')