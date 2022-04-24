import time 
import os
import cv2
import numpy as np
from utils import createRunningFolder 

import cv2
import numpy as np
from scipy.misc import face
from sklearn.covariance import fast_mcd


# faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# smileCascade = cv2.CascadeClassifier("Resources/haarcascade_smile.xml")
cap = cv2.VideoCapture(0)
dir1 = createRunningFolder('otputs', 'Compass/p')
dir2 = createRunningFolder('otputs', 'Compass/n')
os.chdir(dir1)

count_blur = 0
count_noblur = 0

while(True):

    ret, frame = cap.read()
    blur = cv2.Laplacian(frame, cv2.CV_64F)
    x = blur.var()
    if x > 100 and count_blur < 101:
        os.chdir('../p')
        count_blur += 1
        img = cv2.putText(frame, "Total saved: " +str(count_blur)+"Blur:"+str(x), (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
        dim = (160, 120)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        # if count_blur < 101:
        cv2.imwrite(f'p{count_blur}.png', resized)
    
    elif x < 100 and count_noblur<151:
        os.chdir('../n')
        count_noblur += 1
        img = cv2.putText(frame, "Total saved: " +str(count_noblur)+" not Blur:"+str(x), (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
        dim = (160, 120)
        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        # if count_noblur < 151:
        cv2.imwrite(f'p{count_noblur}.png', resized)

    
    # frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(frame_gray, 1.06, 10)

    # for (x, y, w, h) in faces:
    #     # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     roi_gray = frame_gray[y:y + h, x:x + w]
    #     roi_color = frame[y:y + h, x:x + w]
    #     smiles = smileCascade.detectMultiScale(roi_gray, 1.5, 20)
 
    #     for (sx, sy, sw, sh) in smiles:
    #         cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    #         start = time.time()
    #         cv2.imwrite(f'{start}.png', frame)


    cv2.imshow("2", img)
        
    if cv2.waitKey(1) & 0xFF == ord('q') or (count_blur<101 & count_noblur<151):
            break

cap.release()

cv2.destroyAllWindows()