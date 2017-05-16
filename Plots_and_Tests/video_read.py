import numpy as np
import cv2

cap = cv2.VideoCapture('/home/scania/Scania/Glantan_Recordings/2017-03-24_DrivePX2/dw_20170324_115921_0.000000_0.000000/video_front.h264')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()