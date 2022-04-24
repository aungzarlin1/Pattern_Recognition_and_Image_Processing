import cv2
import matplotlib.pyplot as plt

# image path
path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\Lab02\Resources\bahtcoins.png'
img = plt.imread(path)
# orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
images = [img, img]
title = ['Orig', 'Gray']
plt.rcParams['figure.autolayout'] = True
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.axis('off')
plt.show()