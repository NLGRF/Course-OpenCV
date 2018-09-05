import numpy as np
import cv2

# โหลดรูปภาพ test.png ในโหมดสีพื้นฐาน
img = cv2.imread('test.png',cv2.IMREAD_COLOR)
cv2.imshow('cat',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.namedWindow('cata',cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow('catb',cv2.WINDOW_NORMAL)