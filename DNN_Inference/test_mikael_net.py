
# Load all images in directory and
# change dimensions of input images to blob dimensions
# inspired by https://github.com/alexgkendall/SegNet-Tutorial/blob/master/Scripts/test_bayesian_segnet.py

import numpy as np
import caffe
import cv2
import os	# concatenate path and file name correctly for all operating systems
import glob	# find files of certain type in directory
from collections import OrderedDict
import logging
import PIL.Image
import sys

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = 'Mikael/deploy.prototxt'
PRETRAINED = 'Mikael/train_iter_460000.caffemodel' #'Agneev/snapshot_iter_16380.caffemodel' #'Mikael/train_iter_460000.caffemodel'

MEAN_FILE = 'Mikael/out.npy'

if __name__ == '__main__':
        
    # desired input data dimensions
    batchSize = 1
    channels = 3
    imageWidth = 640 # 640
    imageHeight = 400 # 400

    # load list of jpg file names in directory
    path = "Images/"
    fileNames = glob.glob(os.path.join(path, '*.bmp'))

    net = caffe.Net(MODEL_FILE,     # defines the structure of the model
                    PRETRAINED,     # contains the trained weights
                    caffe.TEST)     # use test mode (e.g., don't perform dropout)

    caffe.set_mode_gpu()

    mu = np.load(MEAN_FILE)
    mu = mu.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values

    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))      # move image channels to outermost dimension
    transformer.set_mean('data', mu)                # subtract the dataset-mean value in each channel
    transformer.set_raw_scale('data', 255)          # rescale from [0, 1] to [0, 255]
    transformer.set_channel_swap('data', (2,1,0))   # swap channels from RGB to BGR

    # iterate over all image files
    for fileName in fileNames:

        # load and resize input image
        image = caffe.io.load_image(fileName)
        image = caffe.io.resize_image(image, (imageHeight, imageWidth))
        
        transformed_image = transformer.preprocess('data', image)
        print transformed_image

        # copy the image data into the memory allocated for the net
        net.blobs['data'].data[...] = transformed_image

        ### perform classification
        o = net.forward()
        
        # order outputs in prototxt order
        output = OrderedDict()
        for blob in net.blobs.keys():
            if blob in o:
                output[blob] = o[blob]

        # loop through output and check the probabillity of the road class for each pixel
        for row in range(0, imageHeight):
            for col in range (0, imageWidth):
                if output[blob][0][1][row][col] > 0.8:
                    image[row, col, 2] = image[row, col, 1]*(1-output[blob][0][1][row][col])/0.1 #Red
                    image[row, col, 1] = image[row, col, 1]*output[blob][0][1][row][col] #Green
                    image[row, col, 0] = 0 #Blue
        cv2.imshow('GRAVEL ROAD!!!!', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

