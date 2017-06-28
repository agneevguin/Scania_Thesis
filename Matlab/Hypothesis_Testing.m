cm = C_3_682_With;
x = 1;
TP = cm(x, x);
FP = sum(cm(:, x)) - TP;
FN = sum(cm(x, :), 2) - TP;
TN = sum(sum(cm)) - FP - FN - TP;

Sesitivity = TP/(TP + FN);
Specificity = TN/(TN + FP);
Precision = TP/(TP + FP);
Accuracy = (TP + TN)/(TP + FP + FN + TN);
F1_score = 2 * TP/(2 * TP + FP + FN);

FPR = 1 - Specificity;