A = C_9_9548_Gabor;
P_9_9548_Gabor = (A./sum(A))*100;
R_9_9548_Gabor = (diag(1./sum(A,2))*A)*100; 