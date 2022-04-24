from turtle import done, shape
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import joblib
from sklearn.metrics import mean_absolute_error
import pickle

model = pickle.load(open('otputs/house_trained_model.pkl', 'rb'))

df1 = pd.DataFrame([[2006, 1, 4, 3, 0, 2200, 2350, 0, 0, True, False, True, True, 0, 0 , 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0, 0]])
df2 = pd.DataFrame([[2006, 1, 4, 3, 0, 2200, 2350, 0, 0, True, False, True, True, 0, 0 , 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0, 0]])
df3 = pd.DataFrame([[2006, 1, 4, 3, 0, 2200, 2350, 0, 0, True, False, True, True, 0, 0 , 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0, 0]])

y1 = model.predict(df1)
y2 = model.predict(df2)
y3 = model.predict(df3)
print(y1)
print(y2)
print(y3)
