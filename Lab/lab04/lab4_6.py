import time 
import os
import cv2
import numpy as np
from utils import createRunningFolder 

import cv2
import numpy as np
from scipy.misc import face
from sklearn.covariance import fast_mcd


faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("Resources/haarcascade_smile.xml")
cap = cv2.VideoCapture(0)
dir = createRunningFolder('otputs', 'selfie')
os.chdir(dir)
while(True):

    ret, frame = cap.read()
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(frame_gray, 1.06, 10)

    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = frame_gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smileCascade.detectMultiScale(roi_gray, 1.5, 20)
 
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
            start = time.time()
            cv2.imwrite(f'{start}.png', frame)


    cv2.imshow("selfie", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()