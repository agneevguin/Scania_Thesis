%% Clear Data
% clear all; close all; clc;

%% Input Data
true_dir = '/home/scania/Scania/Agneev/True_Labels_blackened/16-Classes_9548-Images/Test/Labels/';
%true_dir = '/media/scania/iQMatic_2/Agneev_Digits/Datasets/9-Classes_1364-Images/Test/Labels/';
pred_dir = '/home/scania/Scania/Agneev/Download_Models/Previous/Agneev_Model_16_9548_Preliminary-test_With-previous_Gabor_epoch_29.0/Segnet_Labels/';
im_true_all = [];
im_pred_all = [];

%% Orders
% order = [asphalt, gravel_h, gravel_l, mud, sand, water_ponds, grass, snow, gravel_n, mud_n, sand_n, sky, vegetation, grass_n, snow_n, background]
order_3 = ["0 255 0";"255 0 0";"0 0 0"];
order_9 = ["105 105 105";"112 128 144";"192 192 192";"139 69 19";"244 164 96";"106 90 205";"255 255 0";"245 222 179";"0 0 0"];
order_16 = ["105 105 105";"112 128 144";"192 192 192";"139 69 19";"244 164 96";"106 90 205";"255 255 0";"245 222 179";"176 196 222";"210 105 30";"210 180 140";"135 206 235";"0 100 0";"154 205 50";"255 255 224";"0 0 0"];

%% Read multiple files from folder
f_true = dir(strcat(true_dir,'*.bmp'));         % true_dir bmp for 6820 and 9548, else png
for k = 1:size(f_true,1)
    file = strcat(true_dir,f_true(k).name);     % true_dir
    im_true{k} = imread(file);
    im_true{k} = imresize(im_true{k}, 0.5, 'nearest');      % 0.25 for full images, 0.5 for 9548 images, none for 6820
    im_true_all = vertcat(im_true_all, im_true{k});
end

f_pred = dir(strcat(pred_dir,'*.bmp'));           % pred_dir
for k = 1:size(f_pred,1)
    file=strcat(pred_dir,f_pred(k).name);       % pred_dir
    im_pred{k}=imread(file);
    im_pred{k} = imresize(im_pred{k}, 0.5, 'nearest');
    im_pred_all = vertcat(im_pred_all, im_pred{k});
end
clearvars im_true im_pred file f_true f_pred true_dir pred_dir 

%% Read RGB values from image
RGB_true_Vector = reshape(im_true_all,[],3);
RGB_pred_Vector = reshape(im_pred_all,[],3);
RGB_true_Vector = join(string(RGB_true_Vector));
RGB_pred_Vector = join(string(RGB_pred_Vector));
[C_16_9548_Gabor_Prev] = confusionmat(RGB_true_Vector,RGB_pred_Vector, 'order', order_16);

