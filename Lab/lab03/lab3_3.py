import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\utils')
from util import displayImages


path = r'Resources\bahtcoins.png'


orig = cv2.imread(path)
img = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)
gray1 = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
blur1 = cv2.GaussianBlur(gray1, (7,7),1)
edged1 = cv2.Canny(blur1, 50, 100)


contours, hierarchy = cv2.findContours(edged1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contourImg = img.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500:
        continue
    cv2.drawContours(contourImg, cnt, -1, (0, 0 , 255), 3)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    contourImg = cv2.putText(contourImg, str(area), (x+10, y+h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.rectangle(contourImg, (x,y), (x+w, y+h), (0, 255, 0), 2)

# changing color to matplotlib format
gray = cv2.cvtColor(gray1, cv2.COLOR_GRAY2RGB)
blur = cv2.cvtColor(blur1, cv2.COLOR_GRAY2RGB)
canny = cv2.cvtColor(edged1, cv2.COLOR_GRAY2RGB)


D = {'Orig' : img, 'Gray':gray, "Blur": blur, "Canny":canny, 'contours':contourImg, "": np.ones_like(img)*255}

displayImages(D, 2, 3)


