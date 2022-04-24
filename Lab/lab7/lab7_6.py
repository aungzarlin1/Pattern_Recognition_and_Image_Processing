from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

model = GradientBoostingRegressor()
param_grid = {
    'n_estimators':[500, 1000, 3000],
    'max_depth' : [4, 6],
    'min_samples_leaf':[3, 5, 9, 17],
    'learning_rate':[0.1, 0.05, 0.02, 0.01],
    'max_features':[1.0,0.3,0.1],
    'loss':['squared_error', 'lad', 'huber'],
    'verbose':[True]}

model = GridSearchCV(model, param_grid, n_jobs=4)

df = pd.read_csv('otputs/1000_rows_house_dataset.csv')
df = pd.get_dummies(df, columns=['garage_type', 'city'])
X = df.drop(columns=['sale_price', 'house_number', 'unit_number', 'street_name', 'zip_code'])


y = df['sale_price']
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=42)

model.fit()

print(model.best_params_)