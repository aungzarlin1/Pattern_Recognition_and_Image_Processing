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
edged1 = cv2.Canny(blur1, 131, 253)
kernel = np.ones((5,5), np.uint8)
dilation1= cv2.dilate(edged1, kernel, iterations=1)


contours, hierarchy = cv2.findContours(edged1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contourImg = img.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)
    cv2.drawContours(contourImg, cnt, -1, (0, 0 , 255), 3)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
    x, y, w, h = cv2.boundingRect(approx)
    
    if 6000 >= area > 5000:
        coilName='10B'
    elif 5000 > area > 4000:
        coilName='5B'
    elif 4000 > area > 3500:
        coilName='2B'
    elif 3500 > area > 2600:
        coilName='1B'
    elif 2600 > area >= 2500:
        coilName='0.5B'
    elif 2500 > area > 2000:
        coilName='0.25B'
    else :
        coilName='1B'
    
    print(area, coilName)
    contourImg = cv2.putText(contourImg, coilName, (x+10, y+h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.rectangle(contourImg, (x,y), (x+w, y+h), (0, 255, 0), 2)

# changing color to matplotlib format
gray = cv2.cvtColor(gray1, cv2.COLOR_GRAY2RGB)
blur = cv2.cvtColor(blur1, cv2.COLOR_GRAY2RGB)
canny = cv2.cvtColor(edged1, cv2.COLOR_GRAY2RGB)
dilation = cv2.cvtColor(dilation1, cv2.COLOR_GRAY2RGB)


D = {'Orig' : img, 'Gray':gray, "Blur": blur, "Canny":canny, "dilation":dilation, 'contours':contourImg}

displayImages(D, 2, 3)


# 2540.0 0.5B
# 2022.0 0.25B
# 2024.0 0.25B
# 2552.5 0.5B
# 3112.0 1B
# 3651.0 2B
# 4572.5 5B
# 3657.5 2B
# 4547.5 5B


# 0.0 0.25B
# 54.5 0.25B
# 2022.0 0.25B
# 2024.0 0.25B
