import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('test.png',0) #การเลือกภาพที่จะแสดงและโทนสีของภาพ
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) #การซ้อนแกนของแกน X และแกน Y
plt.show()