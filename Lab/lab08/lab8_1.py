import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler
import joblib
from keras.layers import *
from keras.models import Sequential
import time
import datetime

start_time = time.time()

df = pd.read_csv('Resources/house_dataset.csv')
df = pd.get_dummies(df, columns=['garage_type', 'city'])
df = df.drop(columns=['house_number', 'unit_number', 'street_name', 'zip_code'])
X = df.copy()
X.pop('sale_price')
y = df[['sale_price']]
# print(X.shape)
# print(y.shape)

X_scaler = MinMaxScaler(feature_range=(0, 1))
y_scaler = MinMaxScaler(feature_range=(0, 1))

X[X.columns] = X_scaler.fit_transform(X[X.columns])
y = y_scaler.fit_transform(y)
X = X.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(4, activation='relu'))
# model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='SGD')

model.fit(X_train, y_train, epochs=5, batch_size=16, shuffle=True)
model.save('otputs/house_value_model_5epoch.h5')

predictions_train = model.predict(X_train, verbose=0)
mse = mean_absolute_error(y_scaler.inverse_transform(predictions_train), y_scaler.inverse_transform(y_train))
print(f"Trainind Set Mean Absolute Error : {mse:.4f}")

predictions_test = model.predict(X_test, verbose=0)
mse = mean_absolute_error(y_scaler.inverse_transform(predictions_test), y_scaler.inverse_transform(y_test))
print(f"Test Set Mean Absolute Error: {mse:.4f}")

print(f'Done in {datetime.timedelta(seconds=time.time() - start_time)}')