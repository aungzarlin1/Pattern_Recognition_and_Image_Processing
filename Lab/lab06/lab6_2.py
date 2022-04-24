import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('otputs/simple_house_dataset.csv')

df['sale_price'] = df['sale_price'] / 1000

print(df.describe())

plt.scatter(df['num_bedrooms'], df['sale_price'])
plt.xlabel('num_bedrooms')
plt.ylabel('sale_price')
plt.show()

plt.scatter(df['total_sqft'], df['sale_price'])
plt.xlabel('total_sqft')
plt.ylabel('sale_price')
plt.show()