value1 = C_9_682_With;

%% hypothesis information
% x = 1;
% TP = cm(x, x);
% FP = sum(cm(:, x)) - TP;
% FN = sum(cm(x, :), 2) - TP;
% TN = sum(sum(cm)) - FP - FN - TP;
% 
% Sensitivity = TP/(TP + FN); % True Positive Rate
% Specificity = TN/(TN + FP); % True Negative Rate
% Precision = TP/(TP + FP); % Psotive Predicted Value
% Accuracy = (TP + TN)/(TP + FP + FN + TN);
% F_score = 2 * (Precision * Sensitivity)/(Precision + Sensitivity);
% F1_score = 2 * TP/(2 * TP + FP + FN);
% 
% FNR = 1 - Sensitivity;
% FPR = 1 - Specificity;
% 
% Likelihood_ratio_positive = Sensitivity / (1 - Specificity);
% Likelihood_ratio_negative = (1 - Sensitivity) / Specificity;

% %% ROC between TPR in y and FPR in x.

%% confusionmatStats.m

field1 = 'confusionMat';
numOfClasses = size(value1,1);
totalSamples = sum(sum(value1));

[TP,TN,FP,FN,accuracy,sensitivity,specificity,precision,f_score,fpr] = deal(zeros(numOfClasses,1));
for class = 1:numOfClasses
   TP(class) = value1(class,class);
   tempMat = value1;
   tempMat(:,class) = []; % remove column
   tempMat(class,:) = []; % remove row
   TN(class) = sum(sum(tempMat));
   FP(class) = sum(value1(:,class))-TP(class);
   FN(class) = sum(value1(class,:))-TP(class);
end

for class = 1:numOfClasses
    accuracy(class) = (TP(class) + TN(class)) / totalSamples;
    sensitivity(class) = TP(class) / (TP(class) + FN(class));
    specificity(class) = TN(class) / (FP(class) + TN(class));
    precision(class) = TP(class) / (TP(class) + FP(class));
    f_score(class) = 2*TP(class)/(2*TP(class) + FP(class) + FN(class));
    fpr(class) = 1 - specificity(class);
end

field2 = 'accuracy';  value2 = accuracy;
field3 = 'sensitivity';  value3 = sensitivity;
field4 = 'specificity';  value4 = specificity;
field5 = 'precision';  value5 = precision;
field6 = 'recall';  value6 = sensitivity;
field7 = 'Fscore';  value7 = f_score;
field8 = 'FPR'; value8 = fpr;
stats = struct(field1,value1,field2,value2,field3,value3,field4,value4,field5,value5,field6,value6,field7,value7,field8,value8);
if exist('gorder','var')
    stats = struct(field1,value1,field2,value2,field3,value3,field4,value4,field5,value5,field6,value6,field7,value7,field8,value8,'groupOrder',gorder);
end