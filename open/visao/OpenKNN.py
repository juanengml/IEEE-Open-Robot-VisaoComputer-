import numpy as np
import cv2
import os
import threading


def CompareImage(img1,img2):
 sift = cv2.xfeatures2d.SURF_create()
 kp1, des1 = sift.detectAndCompute(img1, None)
 kp2, des2 = sift.detectAndCompute(img2, None)
 FLANN_INDEX_KDTREE = 0
 index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
 search_params = dict(checks=50)
 
 flann = cv2.FlannBasedMatcher(index_params, search_params)
 matches = flann.knnMatch(des1, des2, k=2)
 FLANN_INDEX_KDTREE = 0
 MIN_MATCH_COUNT = 10
 index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
 search_params = dict(checks=50)
 flann = cv2.FlannBasedMatcher(index_params, search_params)
 matches = flann.knnMatch(des1, des2, k=2)
 good = []
 for m, n in matches:
    if m.distance < 0.6 * n.distance:
        good.append(m)

 if len(good) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()
    return  [True,"%d/%d" % (len(good), MIN_MATCH_COUNT)]
 else:
    matchesMask = None
    return  [False,"%d/%d" % (len(good), MIN_MATCH_COUNT)]

def GetImageToCompare(img1,value):
    basic = os.popen("ls *.png").read().split("\n")       
    img1 = cv2.imread(img1,0)
    tank = ['tanqueleite1.png']
    #tank = ['tanqueleite1.png', 'tanqueleite2.png', 'tanqueleite3.png', 'tanqueleite.png']
    troca = ['troca1.png']
    #troca = ['troca1.png', 'troca2.png', 'troca3.png', 'troca4.png', 'troca.png']
    vazias = ['vazias1.png']
    #vazias = ['vazias1.png', 'vazias2.png', 'vazias3.png', 'vazias.png']
    tankPrecisao = []
    trocaPrecisao = []
    vaziasPrecisao = []
    if value==True:       
        for p in range(len(tank)):
             img2 = cv2.imread(tank[p],0)
             match = CompareImage(img1,img2)   
             m = (match[1]).split("/")[0]
             features = [tank[p],match[0],(match[1]).split("/")[0]]
             features.append(features)
             print "Image File: \t",features[0],"\tAccuracy: ",features[2]
             tankPrecisao.append(int(features[2]))
        for p in range(len(troca)):
             img2 = cv2.imread(troca[p],0)
             match = CompareImage(img1,img2)       
             m = (match[1]).split("/")[0]
             features = [troca[p],match[0],(match[1]).split("/")[0]]
             features.append(features)
             print "Image File: \t",features[0],"\tAccuracy: ",features[2]
             trocaPrecisao.append(int(features[2]))
        for p in range(len(vazias)):
             img2 = cv2.imread(vazias[p],0)
             match = CompareImage(img1,img2)       
             m = (match[1]).split("/")[0]
             features = [vazias[p],match[0],(match[1]).split("/")[0]]
             features.append(features)
             print "Image File: \t",features[0],"\tAccuracy: ",features[2]
             vaziasPrecisao.append(int(features[2])) 

        print tankPrecisao,trocaPrecisao,vaziasPrecisao     
        print "Precisao\nVazias: %i\nTroca: %s\nTank: %s " % (np.mean(vaziasPrecisao),np.mean(trocaPrecisao),np.mean(tankPrecisao))
    else:
         print "Naum e um tanque Leite !" 