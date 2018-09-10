import numpy as np
import cv2

img = cv2.imread('C:\\Users\\non19\\Desktop\\OpenCV\\part2_Image\\test.png',cv2.IMREAD_COLOR)
cv2.imshow('cat',img)
key = cv2.waitKey(0)
if key == 27: # wait for ESC key to exit
    cv2.destroyAllWindows()
elif key == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('cat_new.png',img)
    cv2.destroyAllWindows()
