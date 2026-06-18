import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('Advertising.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)
df['TV_Radio_interaction'] = df['TV'] * df['Radio']
X = df[['TV', 'Radio','TV_Radio_interaction']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_predict = model.predict(X_test)

mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
