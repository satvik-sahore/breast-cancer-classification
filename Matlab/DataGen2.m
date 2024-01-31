clc;close all;clear;

srcFilesCnacer = dir('D:\BreastCancerThesis\CodeClassification\DDSM2\cancer\*.png');
srcFilesNormal = dir('D:\BreastCancerThesis\CodeClassification\DDSM2\normal\*.png');
im_data = zeros(length(srcFilesCnacer)+length(srcFilesNormal),128,128);
cancer_len = length(srcFilesCnacer);
normal_len = length(srcFilesNormal);
for i = 1 : cancer_len

    filename_read = strcat('D:\BreastCancerThesis\CodeClassification\DDSM2\cancer\',srcFilesCnacer(i).name);
    im = imread(filename_read);
    im = rgb2gray(im);
    im_data(i,:,:) = im;    
end
for i = cancer_len + 1 : normal_len+cancer_len

    j = i- cancer_len;
    filename_read = strcat('D:\BreastCancerThesis\CodeClassification\DDSM2\normal\',srcFilesNormal(j).name);
    im = imread(filename_read);
    im = rgb2gray(im);
    im_data(i,:,:) = im;    
end




size= cancer_len + normal_len;
y_data = [zeros(1,cancer_len) ones(1,normal_len)]';
per = randperm(size);

y_data = y_data(per,:);
im_data = im_data(per,:,:);

train = size * (0.7);

X_train = im_data(1:train,:,:);
X_test = im_data(train:end,:,:);

y_train = y_data(1:train,:);
y_test = y_data(train:end,:);

save('Dataset_for_CNN2.mat','X_train','X_test','y_train','y_test');