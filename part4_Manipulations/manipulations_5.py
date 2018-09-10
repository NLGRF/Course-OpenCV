# import the necessary packages
import numpy as np
import cv2

# load the image and show it
image = cv2.imread('C:\\Users\\non19\\Desktop\\OpenCV\\part4_Manipulations\\jurassic-park-tour-jeep.jpg',cv2.IMREAD_COLOR)

# crop the image using array slices -- it's a NumPy array
# after all!
cropped = image[70:170, 440:540]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)

# write the cropped image to disk in PNG format
cv2.imwrite("thumbnail.png", cropped)