import numpy as np
import cv2
import argparse
from OpenKNN import CompareImage

# argumentos para comparar
ap = argparse.ArgumentParser();
ap.add_argument("--ver",        dest="help",    help = "python testarg.py -i1 img.png -i2 img2.png")
ap.add_argument("--img1",       dest="img1",    help = "path to the image file")
ap.add_argument("--img2",       dest="img2",    help = "path to the image file 2")
args = vars(ap.parse_args())

#print args
#print ap.parse_args()

try: 
 if args['img1'] and args['img2']:
  img1 = cv2.imread(args["img1"],0)
  img2 = cv2.imread(args["img2"],0)
  
  match = CompareImage(img1,img2)
  #print match  
  if match[0] == True:
  	 print "[Img1: ",args['img1'],"] | [Img2: ",args["img2"],"] | [Acuraccy Images: ",match[1],"]"
  if match[0] == False:
  	 print match[1]
except:
  print "Fail Compare Images"