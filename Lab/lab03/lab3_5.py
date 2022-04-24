import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\utils')
from util import displayImages

def emptyFunction():
    pass
path = r'Resources\bahtcoins.png'


orig = cv2.imread(path)
img = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
gray1 = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
blur1 = cv2.GaussianBlur(gray1, (7,7),1)

windowName ="Trackbars"
      
    # window name
cv2.namedWindow(windowName) 
       
    # there trackbars which have the name
    # of trackbars min and max value 
cv2.createTrackbar('CannyLower', windowName, 0, 255, emptyFunction)
cv2.createTrackbar('CannyUpper', windowName, 0, 255, emptyFunction)
       
    # Used to open the window
    # till press the ESC key
while(True):

    CannyLower = cv2.getTrackbarPos('CannyLower', windowName)
    CannyUpper = cv2.getTrackbarPos('CannyUpper', windowName)
    canny = cv2.Canny(blur1, CannyLower, CannyUpper)

    kernel = np.ones((5,5), np.uint8)
    img_dilation = cv2.dilate(canny, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contourImg = orig.copy()
    cv2.drawContours(contourImg, contours,-1, (255, 0,0), 3)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        cv2.drawContours(contourImg, cnt, -1, (255, 0 , 0), 3)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        x, y, w, h = cv2.boundingRect(approx)
        contourImg = cv2.putText(contourImg, str(area), (x+10, y+h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.rectangle(contourImg, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
    
    cv2.imshow("Canny", canny)
    cv2.imshow("Dilation", img_dilation)
    cv2.imshow("Contours",contourImg)
    if cv2.waitKey(1) == 0:
        break
          
        # values of blue, green, red      
        # merge all three color chanels and
        # make the image composites image from rgb   
    # edged1[:] = [CannyLower, CannyUpper]
           
cv2.destroyAllWindows()
