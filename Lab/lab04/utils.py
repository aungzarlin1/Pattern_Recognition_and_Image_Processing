import numpy as np
import cv2
import py_linq
from py_linq import Enumerable
import time
import os


def stackImages(dic, numCols, scale=1.0):
    imgs = list(dic.values())
    count = len(imgs)
    remain = count % numCols
    if (remain > 0):
        imgBlack = np.zeros_like(imgs[0])
        lack = numCols - remain
        for i in range(lack):
            imgs.append(imgBlack)

    imgs = Enumerable(imgs).select(lambda x : x if len(x.shape) > 2 else cv2.cvtColor(x, cv2.COLOR_GRAY2BGR)).to_list()
    w = int(imgs[0].shape[1] * scale)
    h = int(imgs[0].shape[0] * scale)
    imgs = Enumerable(imgs).select(lambda x : cv2.resize(x, (w, h))).to_list()

    lblArea = np.zeros((20, w, 3), np.uint8)
    lblArea[:] = 255, 255, 255
    imgs = Enumerable(imgs).select(lambda x: np.vstack([lblArea, x])).to_list()
    keys = list(dic.keys())
    for i, (img, key) in enumerate(zip(imgs, keys)):
        cv2.putText(img, key, (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0), 1)

    ver = Enumerable(np.array_split(imgs, len(imgs) // numCols)).select(lambda x:np.hstack(x))
    return np.vstack(ver)


def createRunningFolder(rootFolder, runFolder):
    count = 0
    while os.path.exists(f'{rootFolder}/{runFolder}-{count}'):
        count +=1
    path = f'{rootFolder}/{runFolder}-{count}'
    os.makedirs(path)
    return path
    


