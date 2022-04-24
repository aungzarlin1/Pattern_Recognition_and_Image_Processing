import pandas as pd

df = pd.read_csv('Resources/house_dataset.csv')

new_data = df[:1000]

new_data.to_csv('otputs/1000_rows_house_dataset.csv', index=False)