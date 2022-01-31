import cv2
import matplotlib.pyplot as plt

def displayImages(dic, nrows, ncols):
    """
    dic = A dictionary { key : value} where key is for title of the plot and value is the image
    nrows, ncols are for the plotting the image
    """
    plt.rcParams['figure.autolayout'] = True
    for i, title in enumerate(dic):   # i ->  0,1, ..   # title -> dic.keys()
        plt.subplot(nrows, ncols, i+1)
        plt.imshow(dic[title])
        plt.title(title)
        plt.axis('Off')
    plt.show()

path = r'C:\Users\Aung Zar Lin\OneDrive\Desktop\Pattern Recognition and Image Processing\Lab\Lab02\Resources\bahtcoins.png'
img = cv2.imread(path)
orig = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
D = {'Orig' : orig, 'Gray':gray}
displayImages(D, 1, 2)