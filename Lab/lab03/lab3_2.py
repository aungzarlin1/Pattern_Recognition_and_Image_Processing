import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\utils')
from util import displayImages


path = r'Resources\lab3_1.jpg'
orig = cv2.imread(path)
img = cv2.cvtColor(orig, cv2.COLOR_BGR2RGB)

gray1 = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)

edged1 = cv2.Canny(gray1, 30, 200)

contours, hierarchy = cv2.findContours(edged1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

contour = cv2.drawContours(orig, contours, -1, (0, 255, 0), 3)


gray = cv2.cvtColor(gray1, cv2.COLOR_GRAY2RGB)
edged = cv2.cvtColor(edged1, cv2.COLOR_GRAY2RGB)

D = {'Orig' : img, 'Gray':gray, 'Canny' : edged, 'contour':contour}

displayImages(D, 2, 2)
