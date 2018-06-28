#!/usr/bin/python
import cv2
import argparse

# Download the image used for this tutorial from here.
# http://goo.gl/jsYXl8

# Read the image
ap = argparse.ArgumentParser();
ap.add_argument("--ver",        dest="help",    help = "python testarg.py -i1 img.png -i2 img2.png")
ap.add_argument("--img1",       dest="img1",    help = "path to the image file")
ap.add_argument("--img2",       dest="img2",    help = "path to the image file 2")

args = vars(ap.parse_args())

print ap.parse_args()
print args
print type(args['img2'])
if args['img2'] and args['img1']:
 print True
 image = cv2.imread(args["img1"])
 image2 = cv2.imread(args["img2"])
 ##gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 ##gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
 image_copy = image.copy()
 image_copy2 = image2.copy()
 # Display the image
 cv2.imshow("Image", image)
 cv2.imshow("Image2", image2)
 cv2.waitKey(); # The program w
