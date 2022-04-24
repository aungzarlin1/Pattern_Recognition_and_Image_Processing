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