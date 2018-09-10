# import the necessary packages
import numpy as np
import cv2

# load the image and show it
image = cv2.imread('C:\\Users\\non19\\Desktop\\OpenCV\\part4_Manipulations\\jurassic-park-tour-jeep.jpg',cv2.IMREAD_COLOR)
cv2.imshow('original', image)
print (image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()