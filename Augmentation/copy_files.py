#!/usr/bin/env python
__author__ = "Agneev Guin"
__credits__ = ["Mikael Salmen", "Marco Trincavelli", "Christian Smith"]
__version__ = "0.1"
__email__ = "agneev@kth.se"

import os
import shutil

PATH_CURRENT = '/home/scania/Scania/Agneev/Labels/Saved_Labels/Images_Augmented_682/'
PATH_FROM = '/home/scania/Scania/Glantan_Recordings/Repeat_BMP_Videos/'
PATH_TO = '/home/scania/Scania/Agneev/Labels/Saved_Labels/Images_682_New/'

for filename in os.listdir(PATH_CURRENT):
	if not filename.endswith('.jpg') or filename.endswith('_R.jpg'): continue
	if filename.split('.')[0].split('_')[0] == 'output':
		num = int(filename.split('.')[0].split('_')[1])
		if ((num <=14) or (199 <= num <= 207) or (263 <= num <= 271) or (628 <= num <= 636) or (751 <= num <= 769) or (807 <= num <= 815)) and (num != 266) and (num != 268) and (num != 634):
			#print str(num)
			shutil.copy(PATH_FROM+'output_0012/'+filename.split('.')[0]+'.bmp', PATH_TO)
			print PATH_FROM+'output_0012/'+filename.split('.')[0]+'.bmp'
		else:	
			shutil.copy(PATH_FROM+'output_0014/'+filename.split('.')[0]+'.bmp', PATH_TO)
			print PATH_FROM+'output_0014/'+filename.split('.')[0]+'.bmp'
	elif filename.split('.')[0].split('_')[0]:
		folder = filename.split('.')[0].split('_')[0]+'_'+filename.split('.')[0].split('_')[1]
		print PATH_FROM+folder+'/'+filename.split('.')[0]+'.bmp'
		shutil.copy(PATH_FROM+folder+'/'+filename.split('.')[0]+'.bmp', PATH_TO)
