import cv2
import numpy as np
# path = '../Resources/bahtcoins.png'

# img = cv2.imread(path)
# blur = cv2.Laplacian(img, cv2.CV_64F)
# print(blur)

# cv2.imshow('image', img)
# cv2.imshow('blur', blur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



cap = cv2.VideoCapture(0)
while(True):
    
    ret, frame = cap.read()
    blur = cv2.Laplacian(frame, cv2.CV_64F)
    x = blur.var()
    if x > 100:
        img = cv2.putText(frame, "Blur:"+str(x), (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
    else:
        img = cv2.putText(frame, " not Blur:"+ str(x), (0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)

    cv2.imshow("Frames", img)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()

cv2.destroyAllWindows()