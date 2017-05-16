#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
=========================================================
The Iris Dataset
=========================================================
This data sets consists of 3 different types of irises'
(Setosa, Versicolour, and Virginica) petal and sepal
length, stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being:
Sepal Length, Sepal Width, Petal Length	and Petal Width.

The below plot uses the first two features.
See `here <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.
"""
# print(__doc__)


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from PIL import Image
import os
import numpy as np

# import some data to play with
# iris = datasets.load_iris()
# X = iris.data[:, :2]  # we only take the first two features.
# Y = iris.target
# print X
# print Y
# print len(X)
# print len(Y)

# import classes data
path_pred = '/home/scania/Scania/Agneev/Labels/Saved_Labels/9_Classes_Color_Labels/'
pixels_pred_all = []
pixels_true_all = []
basewidth = 160

for filename_pred in os.listdir(path_pred):
	if not (filename_pred.endswith('.png')): continue # or filename_pred.endswith('20170324_120648_1840.png')): continue # 20170324_120648_1239

	path_true = '/home/scania/Scania/Agneev/Labels/Images/'
	for filename_true in os.listdir(path_true):
		if not filename_true.endswith('.jpg'): continue
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
			pixels_true_all += list(im_true.getdata())


X = pixels_true_all
Y = pixels_pred_all

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

X = np.array(pixels_true_all)[:, :2]
Y = np.array(y_target)

# print X
# print Y
# print len(X)
# print len(Y)

# x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
# y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

# plt.figure(2, figsize=(8, 6))
# plt.clf()

# Plot the training points
# plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
# plt.xlabel('R')
# plt.ylabel('G')

# plt.xlim(x_min, x_max)
# plt.ylim(y_min, y_max)
# plt.xticks(())
# plt.yticks(())

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(np.array(pixels_true_all))
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=Y,
           cmap=plt.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()
