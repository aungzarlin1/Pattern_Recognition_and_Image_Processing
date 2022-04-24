import cv2
import sys
sys.path.append(r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\utils')
from util import displayImages

path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\Lab02\Resources\bahtcoins.png'
img = cv2.imread(path)
orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
D = {'Orig' : orig, 'Gray':gray}
displayImages(D, 1, 2)