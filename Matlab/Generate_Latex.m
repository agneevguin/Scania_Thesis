order_3 = ["Drivable", "Non_Drivable", "Background"];
order_9 = ["Asphalt", "Gravel_H", "Gravel_L", "Mud", "Sand", "Water", "Grass", "Snow", "Background"];
order_16 = ["Asphalt", "Gravel_H", "Gravel_L", "Mud", "Sand", "Water", "Grass", "Snow", "Gravel_N", "Mud_N", "Sand_N", "Sky", "Vegetation", "Grass_N", "Snow_N", "Background"];
s = P_9_1364_Gabor;
%s(s==Nan)=0; 
A = string(round(s, 2));

A = [order_9' A];
B = ["CLASSES", order_9; A];
input.data = B; 
latex = latexTable(input);
%%Problem with 16 classes. No snow_n