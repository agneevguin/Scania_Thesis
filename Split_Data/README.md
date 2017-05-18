### Split data to Training, Validation and Test Data

* Place the images and labels at the following folders respectively:
  * /home/scania/Scania/Agneev/DNN_Split_Data/All_Data/Images
  * /home/scania/Scania/Agneev/DNN_Split_Data/All_Data/Labels
```
python shuffle_split_files.py 0.2 # Splits to 20% data. Defaulted to 10%. Avoid over 25%. 
```
* Output generated at:
  * /home/scania/Scania/Agneev/DNN_Split_Data/Output