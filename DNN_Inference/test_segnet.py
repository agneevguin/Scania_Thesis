#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

import numpy as np
import os.path
import scipy
import argparse
import scipy.io as sio
import matplotlib
import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.pyplot as plt
import cv2
import sys
import logging

# Make sure that caffe is on the python path:
caffe_root = '/home/scania/Scania/Deep_Learning/caffe-segnet-cudnn5' 			# Change this to the absolute directoy to SegNet Caffe
sys.path.insert(0, caffe_root + 'python')

import caffe

# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--colours', type=str, required=True)
parser.add_argument('--data', type=str, required=True)
args = parser.parse_args()

caffe.set_mode_gpu()

net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)

input_shape = net.blobs['data'].data.shape

label_colours = cv2.imread(args.colours).astype(np.uint8)

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt='%Y-%m-%d,%H:%M:%S', level=logging.INFO)

with open(args.data) as f:
    for line in f:
    	input_image_file = line.split()
    	# print input_image_file[0]
    
	logging.info('Load image!')
	input_image_raw = caffe.io.load_image(input_image_file[0])

	input_image = caffe.io.resize_image(input_image_raw, (input_shape[2],input_shape[3]))
	input_image = input_image*255
	input_image = input_image.transpose((2,0,1))
	input_image = input_image[(2,1,0),:,:]
	input_image = np.asarray([input_image])
	input_image = np.repeat(input_image,input_shape[0],axis=0)
	print input_image.shape

	out = net.forward_all(data=input_image)

	predicted = net.blobs['score'].data		# shape 1 21 1080 1280
	print predicted[0][20][1079][1279]

	output = np.mean(predicted,axis=0)		# shape 21 1080 1280
	# uncertainty = np.var(predicted,axis=0)
	ind = np.argmax(output, axis=0)			# shape 1080 1280
	# for x in xrange(600, 601):
	#     for y in xrange(600, 601):
	#     	for z in xrange(0,20):
	#     		print output[z][x][y]
	#     print "\n"
	#     print "\n"



	segmentation_ind_3ch = np.resize(ind,(3,input_shape[2],input_shape[3]))				# 3, 1080, 1280
	segmentation_ind_3ch = segmentation_ind_3ch.transpose(1,2,0).astype(np.uint8)		# 1080, 1280, 3 label numbers
	segmentation_rgb = np.zeros(segmentation_ind_3ch.shape, dtype=np.uint8)				# 1080, 1280, 3
	# print (segmentation_ind_3ch)
	cv2.LUT(segmentation_ind_3ch,label_colours,segmentation_rgb)
	
	# uncertainty = np.transpose(uncertainty, (1,2,0))

	# average_unc = np.mean(uncertainty,axis=2)
	# min_average_unc = np.min(average_unc)
	# max_average_unc = np.max(average_unc)
	# max_unc = np.max(uncertainty)
	logging.info('Processed image!')
	# plt.imshow(input_image_raw,vmin=0, vmax=255)
	# plt.figure()


	#plt.imshow(segmentation_rgb,vmin=0, vmax=255)
	#plt.figure()
	# plt.imshow(gt_rgb,vmin=0, vmax=255)
	# plt.set_cmap('bone_r')
	# plt.figure()
	# plt.imshow(average_unc,vmin=0, vmax=max_average_unc)
	#plt.show()

	# uncomment to save results
	# print input_image_file
	head , tail = os.path.split(input_image_file[0])
	# print head 					 							# current folder path
	# print os.path.split(head)[0] 								# base folder path
	# print os.path.split(head)[1] 								# current folder name
	# print tail												# filename with extension
	scipy.misc.toimage(segmentation_rgb, cmin=0.0, cmax=255.0).save(head+'/Segnet_Labels/'+tail)
	# scipy.misc.toimage(segmentation_rgb, cmin=0.0, cmax=255.0).save(input_image_file[0]+'_segnet_segmentation.png')
	# cm = matplotlib.pyplot.get_cmap('bone_r') 
	# matplotlib.image.imsave(input_image_file[0]+'_segnet_uncertainty.png',average_unc,cmap=cm, vmin=0, vmax=max_average_unc)

	print 'Processed: ', input_image_file

print 'Success!'


