import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('otputs/simple_house_dataset.csv')

def estimate_home_value(size_in_sqft, num_of_bedrooms):
    value = 100000
    value = value + (num_of_bedrooms * 1.0)
    value = value + (size_in_sqft * 1.0)
    return value

df['my_estimate'] = (100000 + df['num_bedrooms'] * 60000 + df['total_sqft'] * 12)
df['error'] = df['my_estimate'] - df['sale_price']

print(df)