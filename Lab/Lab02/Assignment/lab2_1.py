import cv2

# image path
path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\Lab02\Resources\bahtcoins.png'

# Reading an image
img = cv2.imread(path)

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Orig",img)
cv2.imshow("Gray", image)
cv2.waitKey()
