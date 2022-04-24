import cv2 

path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab01\Resources\landscape.jpg'
img = cv2.imread(path)
while(True):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cv2.waitKey()
