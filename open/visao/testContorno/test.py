
# import the necessary packages
from __future__ import print_function
import imutils
import cv2
 
# load the Tetris block image, convert it to grayscale, and threshold
# the image
image = cv2.imread("frame.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(3,3),0)

edges = cv2.Canny(blurred,100,200)

thresh = cv2.threshold(edges, 225, 255, cv2.THRESH_BINARY_INV)[1]
(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
print (cnts)
 
# draw the contours on the image
cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)