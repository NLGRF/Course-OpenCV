# import the necessary packages
import numpy as np
import cv2

# load the image and show it
image = cv2.imread('C:\\Users\\non19\\Desktop\\OpenCV\\part4_Manipulations\\jurassic-park-tour-jeep.jpg',cv2.IMREAD_COLOR)

# grab the dimensions of the image and calculate the center
# of the image
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
 
# rotate the image by 180 degrees
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)