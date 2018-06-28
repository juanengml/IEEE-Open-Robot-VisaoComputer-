from __future__ import print_function
import numpy as np 
import cv2 
import OpenKNN
import os
import imutils

cap = cv2.VideoCapture("TanqueDeLeite.mp4")
cap.set(3,420)
cap.set(4,420)

img_counter = 5
while(1):
    ret, frame = cap.read()   
    img = cv2.resize(frame,(640,420))  

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
    blurred = cv2.GaussianBlur(gray,(3,3),0)
    edges = cv2.Canny(blurred,100,200)
    thresh = cv2.threshold(gray,255,255,cv2.THRESH_BINARY)[1]

    cv2.imshow('gray',gray)
    cv2.imshow('Bordas',edges)

    
    img_name = "tanqueleite{}.png".format(img_counter)
    #cv2.imwrite(img_name, frame)
    #print("tanqueleite{}.png written!".format(img_name))
    #img1 = "tanqueleite{}.png".format(img_counter)
    #os.system("mv tanqueleite{}.png vazias/".format(img_counter))
    #img_counter += 1
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
