import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv('data/LinearRegressionData.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
for i in range(100, 1001, 100):
    sr = SGDRegressor(max_iter=i, eta0=0.0001, random_state=0)
    sr.fit(X_train, y_train)

    score = sr.score(X_train, y_train)
    print(f'iter={i}, score={score}')