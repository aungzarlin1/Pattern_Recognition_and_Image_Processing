import cv2
import numpy as np

image1 = cv2.imread('Resources/landscape.jpg',0)
gray = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
# print(image1.shape)
# print(gray.shape)
image2 = cv2.imread('Resources/bahtcoins.png')
# print(image2.shape)

img = cv2.resize(image2,(281, 240))
# print(img.shape)
imgHJoin = np.hstack((gray, img))
cv2.imshow('HJoin', imgHJoin)

img2 = cv2.resize(gray,(281, 240))
imgVJoin = np.vstack((img2, image2))
cv2.imshow('VJoin', imgVJoin)

cv2.waitKey(0)
