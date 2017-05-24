#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

import sys, random, os
import shutil
'''
Usage: 
python shuffle_split_files.py # for 10% split
python shuffle_split_files.py 0.2 # for 20% split
'''
data_images = '/home/scania/Scania/Agneev/DNN_Split_Data/All_Data/Images/'
data_labels = '/home/scania/Scania/Agneev/DNN_Split_Data/All_Data/Labels/'
output = '/home/scania/Scania/Agneev/DNN_Split_Data/Output/'
images = 'Images/'
labels = 'Labels/'
dir1 = output + 'Train/'
dir2 = output + 'Val/'
dir3 = output + 'Test/'
ratio = 0.1

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        ratio = float(sys.argv[1])
    if len(sys.argv) == 4:
        data_images = str(sys.argv[2]+'/')
        data_labels = str(sys.argv[3]+'/')
    image_files = []
    label_files = []
    for file in os.listdir(data_images):
        if not (file.endswith('.bmp')): continue        # change to bmp
        image_files.append(data_images+file)

    shuffled = image_files[:]
    random.shuffle(shuffled)
    num = round(len(shuffled) * ratio)

    set1 = int(len(shuffled)-num*2)
    set2 = int(len(shuffled)-num)

    to_dir1, to_dir2, to_dir3 = shuffled[:set1], shuffled[set1:set2], shuffled[set2:]
    shutil.rmtree(output)
    for d in dir1, dir2, dir3:
        if not os.path.exists(output):
            os.mkdir(output)
        if not os.path.exists(d):
            os.mkdir(d)
            os.mkdir(d+images)
            os.mkdir(d+labels)
        
    for file in to_dir1:
        print file
        file = os.path.split(file)[1].split('.')[0]
        print 'Train:', file
        shutil.copy(data_images+file+'.bmp', dir1+images)
        shutil.copy(data_labels+file+'.bmp', dir1+labels)
    for file in to_dir2:
        file = os.path.split(file)[1].split('.')[0]
        print 'Val:', file
        shutil.copy(data_images+file+'.bmp', dir2+images)
        shutil.copy(data_labels+file+'.bmp', dir2+labels)
    for file in to_dir3:
        file = os.path.split(file)[1].split('.')[0]
        print 'Test:', file
        shutil.copy(data_images+file+'.bmp', dir3+images)
        shutil.copy(data_labels+file+'.bmp', dir3+labels)
