from keras.datasets import cifar10
from keras import models
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization
import time
import datetime
from tensorflow import keras

((trainX, trainY), (testX, testY)) = cifar10.load_data()


# def model():
#     model = models.Sequential