import cv2
import matplotlib.pyplot as plt

path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\Lab01\Resources\landscape.jpg'
img =  plt.imread(path)

fig, axs = plt.subplots(2, 2)

# plt.subplot(2, 2, 1)
# plt.imshow(img)
# plt.title("One")
# plt.axis('off')

# plt.subplot(2, 2, 2)
# plt.imshow(img)
# plt.title("Two")
# plt.axis('off')

# plt.subplot(2, 2, 3)
# plt.imshow(img)
# plt.title("Three")
# plt.axis('off')

# plt.subplot(2, 2, 4)
# plt.imshow(img)
# plt.title("Four")
# plt.axis("off")

# plt.show()

title = ['One', 'Two', 'Three', 'Four']
for i in range(1,5):
    plt.subplot(2,2,i)
    plt.imshow(img)
    plt.title(title[i-1])
    plt.axis('off')
plt.show()