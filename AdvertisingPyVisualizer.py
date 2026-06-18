import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = pd.read_csv('Advertising.csv')
plt.scatter(x['TV'], x['Sales'])
plt.title('TV vs Sales')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()
plt.scatter(x['Radio'], x['Sales'])
plt.title('Radio vs Sales')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.show()
plt.scatter(x['Newspaper'], x['Sales'])
plt.title('Newspaper vs Sales')
plt.xlabel('Newspaper')
plt.ylabel('Sales')
plt.show()