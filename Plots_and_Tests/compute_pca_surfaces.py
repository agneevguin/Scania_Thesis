#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
PCA example with Iris Data-set
=========================================================

Principal Component Analysis applied to the Iris dataset.

See `here <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.

"""
# print(__doc__)


# Code source: Gaël Varoquaux
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image, ImageDraw
import os

from sklearn import decomposition
from sklearn import datasets

np.random.seed(5)

# centers = [[1, 1], [-1, -1], [1, -1]]
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
# print type(X)
# print type(y)

path_pred = '/home/scania/Scania/Agneev/Results/1006_008-16-classes_original-images/'
pixels_pred_all = []
pixels_true_all = []
basewidth = 320

for filename_pred in os.listdir(path_pred):
	if not (filename_pred.endswith('.png')): continue # or filename_pred.endswith('20170324_120648_1840.png')): continue # 20170324_120648_1239

	path_true = '/home/scania/Scania/Agneev/Labels/Color_Labels/'
	for filename_true in os.listdir(path_true):
		if not filename_true.endswith('.png'): continue
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

y_target = pixels_pred_all
for index, item in enumerate(y_target):
	# print item
    if (item == (105,105,105)):
        y_target[index] = 0
    elif (item == (112,128,144)):
        y_target[index] = 1
    elif (item == (192,192,192)):
        y_target[index] = 2
    elif (item == (176,196,222)):
        y_target[index] = 3
    elif (item == (139,69,19)):
        y_target[index] = 4
    elif (item == (210,105,30)):
        y_target[index] = 5
    elif (item == (244,164,96)):
        y_target[index] = 6
    elif (item == (210,180,140)):
        y_target[index] = 7
    elif (item == (106,90,205)):
        y_target[index] = 8
    elif (item == (0,0,255)):
        y_target[index] = 9
    elif (item == (35,206,235)):
        y_target[index] = 10
    elif (item == (0,100,0)):
        y_target[index] = 11
    elif (item == (255,255,0)):
        y_target[index] = 12
    elif (item == (154,205,50)):
        y_target[index] = 13
    elif (item == (245,222,179)):
        y_target[index] = 14
    elif (item == (255,255,224)):
        y_target[index] = 15
    else:
        y_target[index] = 16

y = np.array(y_target)
X = np.array(pixels_true_all)

# if class_val == 'asphalt':
# 	draw.polygon(points, fill='rgb(105,105,105)')
# elif class_val == 'gravel_h' or class_val == 'gravel_d':
# 	draw.polygon(points, fill='rgb(112,128,144)')
# elif class_val == 'gravel_l' or class_val == 'gravel':
# 	draw.polygon(points, fill='rgb(192,192,192)')
# elif class_val == 'gravel_n':
# 	draw.polygon(points, fill='rgb(176,196,222)')	
# elif class_val == 'mud':
# 	draw.polygon(points, fill='rgb(139,69,19)')
# elif class_val == 'mud_n':
# 	draw.polygon(points, fill='rgb(210,105,30)')
# elif class_val == 'sand':
# 	draw.polygon(points, fill='rgb(244,164,96)')
# elif class_val == 'sand_n':
# 	draw.polygon(points, fill='rgb(210,180,140)')
# elif class_val == 'water':
# 	draw.polygon(points, fill='rgb(106,90,205)')
# elif class_val == 'water_n':
# 	draw.polygon(points, fill='rgb(0,0,255)')
# elif class_val == 'sky':
# 	draw.polygon(points, fill='rgb(135,206,235)')
# elif class_val == 'vegetation':
# 	draw.polygon(points, fill='rgb(0,100,0)')
# elif class_val == 'grass':
# 	draw.polygon(points, fill='rgb(255,255,0)')
# elif class_val == 'grass_n':
# 	draw.polygon(points, fill='rgb(154,205,50)')
# elif class_val == 'snow':
# 	draw.polygon(points, fill='rgb(245,222,179)')
# elif class_val == 'snow_n':
# 	draw.polygon(points, fill='rgb(255,255,224)')
# else:
# 	draw.polygon(points, fill='rgb(0,0,0)')



print y

fig = plt.figure(1, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
print X
for name, label in [((105,105,105), 0), ((112,128,144), 1), ((192,192,192), 2)]:
    ax.text3D(X[y == label, 0].mean(),
              X[y == label, 1].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
print 'End For'

# Reorder the labels to have colors matching the cluster results
# y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.spectral)

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
print 'End Scatter'

plt.show()
print 'End'