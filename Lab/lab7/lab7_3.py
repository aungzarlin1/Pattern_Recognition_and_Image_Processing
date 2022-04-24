import numpy as np
import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import matplotlib.pyplot as plt



# df = pd.read_csv('Resources/house_dataset.csv')
df = pd.read_csv('otputs/1000_rows_house_dataset.csv')
print(df.shape)

df = df.drop(columns=['house_number', 'unit_number', 'street_name', 'zip_code'])
print(df.shape)


df = pd.get_dummies(df, columns=['garage_type', 'city'])

X = df.copy()
y = X.pop('sale_price')
discrete_features = X.dtypes ==int

def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

mi_scores = make_mi_scores(X, y, discrete_features)
print(mi_scores[::3])


def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores)
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")
    plt.show()


plt.figure(dpi=100, figsize=(8, 5))
plot_mi_scores(mi_scores[:20])
