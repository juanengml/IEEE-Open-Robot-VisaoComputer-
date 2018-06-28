#-*- coding: utf-8 -*-
import cv2
import time
import numpy as np

encontrado = 0

MORPH = 7
CANNY = 250

width  = 620.0
height = 420.0
margin = 0.0


video_capture = cv2.VideoCapture("TanqueDeLeite.mp4")
corners = np.array([[[margin, margin]],[[margin, height + margin  ]], [[ width + margin,height + margin  ]],
        [[width + margin, margin]],])

pts_dst = np.array( corners, np.float32 )
while True:
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
                if (len(approx)==4):
                    encontrado = 1
                    M = cv2.moments( cont )
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    cv2.putText(rgb, ".", (cX,cY),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255),3)
                    pts_src = np.array(approx,np.float32)
                    h, status = cv2.findHomography(pts_src,pts_dst)
                    image_final = cv2.warpPerspective(rgb,h,(int(width + margin*2),int(height+ margin*2)))
                    cv2.drawContours(rgb,[approx],-1,(255,0,0),2)
                else: pass
        
        cv2.imshow('rgb',rgb)
        cv2.imshow('edges',edges)
        if encontrado:
            cv2.imshow('out',image_final)
            pass 
        if cv2.waitKey(27) & 0xFF == ord('q') or cv2.waitKey(99) & 0xFF == ord('c'):
            break
        time.sleep(0.02)
    else:
        print "Stopped"
        break

video_capture.release()
cv2.destroyAllWindows()

# end
    #    cv2.namedWindow( 'out', cv2.CV_WINDOW_AUTOSIZE )
    #    cv2.imshow( 'closed', closed )
    #    cv2.imshow( 'gray', gray )
    #    cv2.namedWindow( 'edges', cv2.CV_WINDOW_AUTOSIZE )
    #    cv2.namedWindow( 'rgb', cv2.CV_WINDOW_AUTOSIZE )
