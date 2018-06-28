#-*- coding: utf-8 -*-
import cv2
import time
import numpy as np
from openknn import KNN 

DELAY = 0.001
USE_CAM = 1
IS_FOUND = 0

MORPH = 7
CANNY = 250

_width  = 620.0
_height = 420.0
_margin = 0.0

dataset = ['tanqueleite1.png', 'troca1.png', 'vazias1.png']
result = []
nameImage = ''

if USE_CAM:
 video_capture = cv2.VideoCapture("TanqueDeLeite.mp4")
corners = np.array([[[_margin, _margin]],[[_margin, _height + _margin  ]], [[ _width + _margin, _height + _margin  ]],
        [[_width + _margin, _margin]],])

pts_dst = np.array( corners, np.float32 )
while True:
    if USE_CAM:
        ret, rgb = video_capture.read()
        rgb = cv2.resize(rgb,(620,360))
    if (ret):
        gray = cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray,1,10,120)
        edges  = cv2.Canny(gray,10,CANNY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(MORPH,MORPH))
        closed = cv2.morphologyEx(edges,cv2.MORPH_CLOSE,kernel)
        n ,contours, h = cv2.findContours(closed,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for cont in contours:
            if cv2.contourArea(cont) > 5000:
                arc_len = cv2.arcLength(cont,True)
                approx = cv2.approxPolyDP( cont, 0.1 * arc_len, True )
                if ( len( approx ) == 4 ):
                    IS_FOUND = 1
                    M = cv2.moments(cont)
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.putText(rgb,".",(cX,cY),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255),3)
                    pts_src = np.array( approx, np.float32 )
                    h, status = cv2.findHomography( pts_src, pts_dst )
                    out = cv2.warpPerspective( rgb, h, (int(_width + _margin * 2 ), int( _height + _margin * 2 ) ) )
                    cv2.imwrite("out.png",out)                    
                    for p in range(len(dataset)):
                     k = KNN(out,dataset[p])
                     m = k.CompareImage()
                     m = [dataset[p],m[1],m[2]]
                     
                     result = m
                     if result[1] == True:
                        if result[1] > res
                          nameImage = result[0]
                    print nameImage,result 
                    cv2.drawContours(rgb,[approx],-1,(255,0,0),2)
                else:pass
        
        cv2.imshow('rgb',rgb)    
        cv2.imshow('edges',edges)    
        if IS_FOUND:    
            cv2.imshow('out',out)
            pass 
        if cv2.waitKey(27) & 0xFF == ord('q') :
            break
        
        time.sleep(DELAY)
    else :
        print "Stopped"
        break
if USE_CAM : video_capture.release()
cv2.destroyAllWindows()

# end