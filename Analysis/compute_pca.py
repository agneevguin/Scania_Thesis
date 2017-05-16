#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

from PIL import Image
from numpy import *
from pylab import *
import pca
import os

imlist = []
path = '/home/scania/Scania/Agneev/Labels/Saved_Labels/16_Classes_Color_Labels/'
for filename in os.listdir(path):
    if not filename.endswith('.png'): continue
    imlist.append(path + filename)

im = array(Image.open(imlist[0])) # open one image to get size
m,n = im.shape[0:2] # get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten()
              for im in imlist],'f')


# perform PCA
V,S,immean = pca.pca(immatrix)

print V
print S
# show some images (mean and 7 first modes)
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n,3))
for i in range(7):
  subplot(2,4,i+2)
  imshow(V[i].reshape(m,n,3))

show()