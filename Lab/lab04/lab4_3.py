import cv2
import numpy as np
from scipy.misc import face
from sklearn.covariance import fast_mcd

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
image = cv2.imread('Resources/set.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.05, 14)  # change 10 to 14
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255,0), 2)


cv2.imshow("result", image)
cv2.waitKey(0)