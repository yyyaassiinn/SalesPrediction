import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('Advertising.csv')
plt.scatter(df['TV'], df['Sales'])
plt.title('TV vs Sales')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show() #good correlation between TV and Sales, so we will use this feature in our model
plt.scatter(df['Radio'], df['Sales'])
plt.title('Radio vs Sales')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.show() #moderately good correlation between Radio and Sales, so we will use this feature in our model
plt.scatter(df['Newspaper'], df['Sales'])
plt.title('Newspaper vs Sales')
plt.xlabel('Newspaper')
plt.ylabel('Sales')
plt.show() #very weak correlation between Newspaper and Sales, so we will not use this feature in our model
df['TotalBudget'] = df['TV'] + df['Radio'] + df['Newspaper']
plt.scatter(df['TotalBudget'], df['Sales'])
plt.title('Total Budget vs Sales')
plt.xlabel('Total Budget')
plt.ylabel('Sales')
plt.show() #good correlation, but we will not use this feature in our model because it uses newspaper which has no correlation with Sales
df['TV_Radio_interaction'] = df['TV'] * df['Radio']
plt.scatter(df['TV_Radio_interaction'], df['Sales'])
plt.title('TV-Radio Interaction vs Sales')
plt.xlabel('TV-Radio Interaction')
plt.ylabel('Sales')
plt.show() #very strong correlation between TV-Radio interaction and Sales, so we will use this feature in our model
df['TV_Radio_ratio'] = df['TV'] / df['Radio']
plt.scatter(df['TV_Radio_ratio'], df['Sales'])
plt.title('TV-Radio Ratio vs Sales')
plt.xlabel('TV-Radio Ratio')
plt.ylabel('Sales')
plt.show() #no correlation between TV-Radio ratio and Sales, so we will not use this feature in our model
