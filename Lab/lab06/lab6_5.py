import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('otputs/simple_house_dataset.csv')

X = df[['num_bedrooms', 'total_sqft']]
y = df['sale_price']

model = LinearRegression()
model.fit(X, y)

print('[x1, x2], b :',model.coef_, model.intercept_)

pred = model.predict([[5, 3051]])
print(pred)