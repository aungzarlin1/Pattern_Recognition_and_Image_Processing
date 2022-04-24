import cv2
import numpy as np
from scipy.misc import face
from sklearn.covariance import fast_mcd


def emptyFunction():
    pass

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
windowName = 'Trackbars'

cv2.namedWindow(windowName)

cv2.createTrackbar('scaleFactor', windowName, 0, 200, emptyFunction)
cv2.createTrackbar('nimNeighbors', windowName, 0, 30, emptyFunction)

cv2.setTrackbarPos('scaleFactor', windowName, 105)
cv2.setTrackbarPos('nimNeighbors', windowName, 10)

while(True):
    
    scaleFactor = cv2.getTrackbarPos('scaleFactor', windowName)
    nimNeighbors = cv2.getTrackbarPos('nimNeighbors', windowName)

    ret, frame = cap.read()
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frame_gray, scaleFactor/100, nimNeighbors)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow(windowName, frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()