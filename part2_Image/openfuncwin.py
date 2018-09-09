import numpy as np
import cv2

img1 = cv2.imread('test.png',0)
img2 = cv2.imread('cat_new.png',cv2.IMREAD_COLOR)
cv2.namedWindow('test.png', cv2.WINDOW_AUTOSIZE)
cv2.imshow('test.png',img1)
cv2.namedWindow('cat_new.png', cv2.WINDOW_NORMAL)
cv2.imshow('cat_new.png',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()