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

def main():
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

	mirror = True
	cam = cv2.VideoCapture(0)
	while True:
		ret_val, img = cam.read()
		if mirror: 
			img = cv2.flip(img, 1)
		# cv2.imshow('Original video', img)

		logging.info('Load image!')
		# input_image_raw = caffe.io.load_image(img)

		input_image = caffe.io.resize_image(img, (input_shape[2],input_shape[3]))
		input_image = input_image*255
		input_image = input_image.transpose((2,0,1))
		input_image = input_image[(2,1,0),:,:]
		input_image = np.asarray([input_image])
		input_image = np.repeat(input_image,input_shape[0],axis=0)

		out = net.forward_all(data=input_image)

		predicted = net.blobs['score'].data		# shape 1 21 1080 1280
		output = np.mean(predicted,axis=0)		# shape 21 1080 1280
		ind = np.argmax(output, axis=0)			# shape 1080 1280

		segmentation_ind_3ch = np.resize(ind,(3,input_shape[2],input_shape[3]))				# 3, 1080, 1280
		segmentation_ind_3ch = segmentation_ind_3ch.transpose(1,2,0).astype(np.uint8)		# 1080, 1280, 3 label numbers
		segmentation_rgb = np.zeros(segmentation_ind_3ch.shape, dtype=np.uint8)				# 1080, 1280, 3

		cv2.LUT(segmentation_ind_3ch,label_colours,segmentation_rgb)

		logging.info('Processed image!')

		
		cv2.imshow('Segmented video', segmentation_rgb)
		if cv2.waitKey(1) == 27: 
			break  # esc to quit
	cv2.destroyAllWindows()
	print 'Success!'

if __name__ == '__main__':
	main()