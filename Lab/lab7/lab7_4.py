from turtle import done
import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pickle
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('Resources/house_dataset.csv')
df = pd.get_dummies(df, columns=['garage_type', 'city'])
X = df.drop(columns=['sale_price', 'house_number', 'unit_number', 'street_name', 'zip_code'])


y = df['sale_price']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=42)

model = GradientBoostingRegressor(
    n_estimators=3000,
    learning_rate=0.1,
    max_depth=6,
    min_samples_leaf=9,
    max_features=0.1,
    loss='huber',
    random_state=0,
    verbose=True
)

y_pred = model.fit(Xtrain,ytrain).predict(Xtest)
print(mean_absolute_error(ytest, y_pred))

pickle.dump(model,open('otputs/house_trained_model.pkl', 'wb'))