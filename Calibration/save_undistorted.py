#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

import cv2
import numpy as np
import os

assert float(cv2.__version__.rsplit('.', 1)[0]) >= 3, 'OpenCV version 3 or newer required.'
'''
K = np.array([[  689.21,     0.  ,  1295.56],
              [    0.  ,   690.48,   942.17],
              [    0.  ,     0.  ,     1.  ]])

# zero distortion coefficients work well for this image
D = np.array([0., 0., 0., 0.])

# use Knew to scale the output
Knew = K.copy()
Knew[(0,1), (0,1)] = 0.4 * Knew[(0,1), (0,1)]
'''
K = np.array([[ 532.19749682, 0., 608.45088149],
			[ 0., 531.23991433, 552.83388766],
			[ 0., 0., 1.]])
D = np.array([-0.27918481, 0.065204, 0.00043639, 0.0031953, -0.00600766])
Knew = K.copy()

K = np.array([[ 532.19748493,    0.,          608.45088493],
[   0.,          531.23989078,  552.83389049],
[   0.,            0.,            1.        ]])

D = np.array([-0.27918479,  0.06520399 , 0.00043639 , 0.0031953 , -0.00600766])

# Knew[(0,1), (0,1)] = 0.4 * Knew[(0,1), (0,1)]

w, h = 1080, 1280
path = '/home/scania/Scania/Agneev/Code/Calibration/Labels/16_Classes_Color_Labels_1364/'
#path = '/home/scania/Scania/Agneev/Code/Calibration/calibration_images/'
head , tail = os.path.split(path)

for filename in os.listdir(path):
	if not filename.endswith('.jpg'): continue
	print filename
	img = cv2.imread(path+filename)
	# img_undistorted = cv2.undistort(img, K, D=D, Knew=Knew)

	# newcameramtx, roi = cv2.getOptimalNewCameraMatrix(K, D, (w, h), 1, (w, h))
	img_undistorted = cv2.undistort(img, K, D, None, Knew)
	cv2.imwrite(path+filename.split('.')[0]+'_U.jpg', img_undistorted)
	# cv2.imshow('undistorted', img_undistorted)
	# cv2.waitKey()