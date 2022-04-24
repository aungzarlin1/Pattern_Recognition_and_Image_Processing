import pandas as pd

df = pd.read_csv('Resources/house_dataset.csv')
# print('features:', df.columns)
# ['year_built', 'stories', 'num_bedrooms', 'full_bathrooms',
#        'half_bathrooms', 'livable_sqft', 'total_sqft', 'garage_type',
#        'garage_sqft', 'carport_sqft', 'has_fireplace', 'has_pool',
#        'has_central_heating', 'has_central_cooling', 'house_number',
#        'street_name', 'unit_number', 'city', 'zip_code', 'sale_price']

df = df[df['zip_code'] == 11682]

data = df[['num_bedrooms', 'total_sqft', 'sale_price']]
print(data.shape)

print(data)
data.to_csv('otputs/simple_house_dataset.csv')
