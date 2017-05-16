# Scania_Thesis

## Code for Semantic Segmentation

### Analysis
* Contribution to the understanding of the inference and evaluate the results
* Inference and visualization for the Digits
* Compute PCA and confusion matrix

### Annotation 
* Generate labels from XML files using hard-coded color codes

### Augmentation
* Generate randomly cropped and rotated images 

### DNN Inference
* Caffe model inference without the use of Digits

### Plots and Tests
* Old tests used for analysis


## Steps To Remember

### Drivenet Example
```
cd /usr/local/driveworks-0.2.1/bin/
./sample_drivenet --input-type=video --video=/media/nvidia/iQMatic_2/Scania_truck_recording/2017-03-10_DrivePX2_HDL32E_Gläntan_Etc/20170310_Camera/scania_0005.h264
./sample_camera_gmsl --input-type=camera --camera-type=c-ov10640-b1 --csi-port=ab --camera-index=0
./sample_lidar_replay --device=VELO_HDL32E --ip=192.168.1.60 --port=2368 --scan-frequency=10

cd /usr/local/driveworks-0.2.1/tools
sudo ./recorder --config-file=../data/tools/glantan.json

./replayer --folder=../data/recordings/dw_20170316_110745_0.000000_0.000000
```

### Recording for Bus
Update JSON file
```
sudo ./recorder --config-file=../data/tools/glantan_ssd.json
```

### Set IP for lidar
```
ip l
sudo ifconfig eth0 192.168.1.60
sudo ifconfig eth0 down
sudo ifconfig eth0 up
```

###  Feature Extraction
```
./sample_camera_tracker --video=/home/scania/Scania/Glantan_Recordings/2017-03-24_DrivePX2/dw_20170324_115428_0.000000_0.000000/video_front.h264
cd /Scania/Opencv/samples/python
python video_gabor_read.py
```

### CAFFE NET
```
cd /home/scania/Scania/Deep_Learning/caffe-segnet-cudnn5/build/tools/
./caffe train -gpu 0 -solver /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/segnet_solver.prototxt  # This will begin training SegNet on GPU 0
./caffe train -gpu 0 -solver /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/segnet_basic_solver.prototxt  # This will begin training SegNet-Basic on GPU 1
./caffe train -gpu 0 -solver /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/segnet_solver.prototxt -weights /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/VGG_ILSVRC_16_layers.caffemodel  # This will begin training SegNet on GPU 0 with a pretrained encoder

python /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Scripts/compute_bn_statistics.py /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/segnet_train.prototxt /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/Training/segnet_iter_1000.caffemodel /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/Inference/ 

python /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Scripts/test_segmentation_camvid.py --model /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/segnet_inference.prototxt --weights /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/Inference/test_weights_segnet_2.caffemodel --iter 10

python /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Scripts/test_segmentation_camvid.py --model /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/segnet_basic_inference.prototxt --weights /home/scania/Scania/Deep_Learning/SegNet-Tutorial/Models/Inference/test_weights_segnet_basic_2.caffemodel --iter 10  # Test SegNetBasic

https://gist.github.com/weiliu89/2ed6e13bfd5b57cf81d6
https://gist.github.com/weiliu89/45e9e8de2c13af6476ca#file-readme-md
train --solver=/home/scania/Scania/Deep_Learning/digits/digits/jobs/20170406-093958-021f/solver.prototxt --gpu=0 --weights=/home/scania/Scania/Deep_Learning/digits/examples/semantic-segmentation/VGG_ILSVRC_16_layers_fc_reduced.caffemodel"
```

### Get Images From Video
```
ffmpeg -i scania_0001.raw qscale:v 2 output_%04.jpg
avconv -i video_front.h264 20170324_113202_%04d.jpg
avconv -i video_front.raw -vcodec copy -acodec copy output_front.h264  //FAILED
ffmpeg -r 5 -start_number 1001 -i 20170324_115428_%04d.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p out.mp4				# Images to video
```

### Resize Image
```
sudo apt-get install imagemagick
convert  -resize 50% source.png dest.jpg
convert  -resize 1024X768  source.png dest.jpg

mogrify -resize 50% *png      											# keep image aspect ratio
mogrify -resize 480x360 *jpg  											# keep image aspect ratio
mogrify -resize 480x360! *png 											# don't keep image aspect ratio
mogrify -resize x240 *png     											# don't keep image aspect ratio
mogrify -resize 320x *png     											# don't keep image aspect ratio
mogrify -format png *.jpg	  											# convert jpg to png type
mogrify -format jpg *.png	  											# convert png to jpg type
mogrify -flop -write *_R.png  											# flop the image
convert *.jpg -flop -set filename:new "%t_R" "%[filename:new].jpg"   	# Rotate image and save with _R
```


### Presentation 4 April
```
cd /usr/local/driveworks-0.2.1/tools

# Scania gate to Glantan gate vertical stand
./replayer --folder=/home/scania/Scania/Glantan_Recordings/2017-03-24_DrivePX2/dw_20170324_114545_0.000000_0.000000

# Gravel pile
./replayer --folder=/home/scania/Scania/Glantan_Recordings/2017-03-24_DrivePX2/dw_20170324_120648_0.000000_0.000000

# Return to Scania horizontal
./replayer --folder=/home/scania/Scania/Glantan_Recordings/2017-03-24_DrivePX2/dw_20170324_114545_0.000000_0.000000

# Replay video 11
cd /usr/local/driveworks-0.2.1/bin
./sample_camera_replay --video=/home/scania/Scania/Glantan_Recordings/2017-03-10_Camera/output_0011.h264
./sample_lidar_replay --file=/home/scania/Scania/Glantan_Recordings/2017-03-10_Camera/scania_0011.bin
```

### Inference
```
cd Scania/Deep_Learning/digits/digits/tools/
python inference_agneev.py /home/scania/Scania/Deep_Learning/DataSets/Test_Data/scania_sample/image-test-inference.txt /home/scania/Scania/Deep_Learning/DataSets/Test_Data/scania_sample/Inference 20170406-131719-c009
python inference_agneev.py /home/scania/Scania/Glantan_Recordings/2017-03-24_DrivePX2/dw_20170324_115921_0.000000_0.000000/video_front.h264 /home/scania/Scania/Deep_Learning/DataSets/Test_Data/scania_sample/Inference 20170406-131719-c009
```



### TO DO
Confusion matrix
https://github.com/pandas-ml/pandas-ml
http://pandas-ml.readthedocs.io/en/stable/conf_mat.html
http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py


### Overnight Test
```
Remove +30 options
python inference_agneev.py /home/scania/Scania/Glantan_Recordings/2017-04-07_DrivePX2/20170405_124731/video_front.h264 /home/scania/Scania/Deep_Learning/DataSets/Test_Data/scania_sample/Inference 20170419-213931-6881
python inference_agneev.py /home/scania/Scania/Agneev/Labels/Images_List.txt /home/scania/Scania/Deep_Learning/DataSets/Test_Data/scania_sample/Inference 20170425-115817-66fd
/home/scania/Scania/Glantan_Recordings/2017-04-07_DrivePX2/dw_20170405_123343_0.000000_0.000000/video_front.h264
```

### Job Numbers

CLASSES 					|DATASET								|MODELS
 --- | --- | --- |
7 classes: 					|20170419-152029-5e0d					|20170419-153352-2f2f
16 classes: 				|20170419-213812-86a7					|20170419-213931-6881
9 classes:					|20170426-114517-ceba					|20170426-114600-520a
10 classes: 				|20170426-144243-3e52					|20170426-144433-798d
5 classes: 					|20170426-150630-756f					|20170426-150713-36b9
							|										|
16 classes_682				|20170503-010848-a41c					|20170503-011008-dc7d
9 classes_682				|20170503-044312-aa42					|20170503-045532-da28
							|										|
16 classes_1364				|										|
9 classes_1364				|20170515-155318-1a09					|
```

### Digits Inference
```
cd Scania/Deep_Learning/digits/digits/tools/
python inference_agneev.py /home/scania/Scania/Agneev/Labels/Images_List.txt /home/scania/Scania/Deep_Learning/DataSets/Test_Data/scania_sample/Inference 20170503-045532-da28
```



### Build DriveNet example
```
cd /usr/local/driveworks-0.2.1/samples/build
sudo cmake -DCMAKE_BUILD_TYPE=Release /usr/local/driveworks-0.2.1/samples/src/dnn/sample_object_detector
```

### Object Detector Test
```
cd /usr/local/driveworks-0.2.1/samples/src/dnn/sample_object_detector
./sample_object_detector --caffe_model=/home/scania/Scania/Agneev/DNN_Data/Agneev_16/snapshot_iter_16380.caffemodel --caffe_prototxt=/home/scania/Scania/Agneev/DNN_Data/Agneev_16/deploy.prototxt --video=/home/scania/Scania/Glantan_Recordings/2017-04-07_DrivePX2/dw_20170405_124107_0.000000_0.000000/video_front.h264
```

### Python Segnet Test
```
cd ~/Scania/Agneev/Code/DNN_Inference
python test_segnet.py --model=/home/scania/Scania/Agneev/DNN_Data/Agneev_16/deploy.prototxt --weights=/home/scania/Scania/Agneev/DNN_Data/Agneev_16/snapshot_iter_16380.caffemodel --colours=/home/scania/Scania/Agneev/Code/DNN_Inference/lut_16.png --data=/home/scania/Scania/Agneev/Code/DNN_Inference/Images/Images.txt
```

### Segnet Presentation for Demo 
```
~/Scania/Agneev/Results/Half_Time_Presentation_Videos
python test_segnet.py --model=Agneev_16/deploy.prototxt --weights=Agneev_16/snapshot_iter_16380.caffemodel --colours=Agneev_16/lut_16.png --data=Video_Set_4/Images_List.txt
python test_segnet.py --model=Agneev_16/deploy.prototxt --weights=Agneev_16/snapshot_iter_16380.caffemodel --colours=Agneev_16/lut_16.png --data=Video_Set_4/Images_List_with_mask.txt
```
