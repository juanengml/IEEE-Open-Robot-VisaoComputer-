import numpy as np
import cv2
import os
import threading

class KNN(object):

 def __init__(self,img1,img2,value=False): # construtor 
    self.img1 = img1
    self.img2 = cv2.imread(img2)
    self.value = value

 def CompareImage(self): # Comparador de Image
  sift = cv2.xfeatures2d.SURF_create()
  kp1, des1 = sift.detectAndCompute(self.img1, None)
  kp2, des2 = sift.detectAndCompute(self.img2, None)
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

class CompImage(object):
  """docstring for CompImage"""
    #tank = ['tanqueleite1.png', 'tanqueleite2.png', 'tanqueleite3.png', 'tanqueleite.png']
    #troca = ['troca1.png', 'troca2.png', 'troca3.png', 'troca4.png', 'troca.png']
    #vazias = ['vazias1.png', 'vazias2.png', 'vazias3.png', 'vazias.png']
  def __init__(self, img1,value):
    self.img1 =  img1
    self.value = value
  
  def GetImageToCompare(self):   #  Pege imagem pra comparar
    tank = ['tanqueleite1.png']
    troca = ['troca1.png']
    vazias = ['vazias1.png']
    tankPrecisao = []
    trocaPrecisao = []
    vaziasPrecisao = []
    if self.vaOflue==True:       
        for p in range(len(tank)):
             img2 = tank[p]
             match = KNN(self.img1,img2).CompareImage()   
             m = (match[1]).split("/")[0]
             features = [tank[p],match[0],(match[1]).split("/")[0]]
             features.append(features)
             print "Image File: \t",features[0],"\tAccuracy: ",features[2]
             tankPrecisao.append(int(features[2]))
        
        for p in range(len(troca)):
             img2 = troca[p]
             match = KNN(self.img1,img2).CompareImage()   
             m = (match[1]).split("/")[0]
             features = [troca[p],match[0],(match[1]).split("/")[0]]
             features.append(features)
             print "Image File: \t",features[0],"\tAccuracy: ",features[2]
             trocaPrecisao.append(int(features[2]))
        
        for p in range(len(vazias)):
             img2 = vazias[p]
             match = KNN(self.img1,img2).CompareImage()   
             m = (match[1]).split("/")[0]
             features = [vazias[p],match[0],(match[1]).split("/")[0]]
             features.append(features)
             print "Image File: \t",features[0],"\tAccuracy: ",features[2]
             vaziasPrecisao.append(int(features[2])) 

        print tankPrecisao,trocaPrecisao,vaziasPrecisao     
        print "Precisao\nVazias: %i\nTroca: %s\nTank: %s " % (np.mean(vaziasPrecisao),np.mean(trocaPrecisao),np.mean(tankPrecisao))
    else:
         print "Naum e um tanque Leite !" 