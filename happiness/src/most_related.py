import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')
data = pd.read_csv('../data/2015.csv')
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')

# print(by_region)
""" Question: What is most important for happiness score? """
rank = []
for col in data.columns[5:10]:
    series = data[col].to_numpy()
    happy = data['Happiness Score'].to_numpy()
    reg = sp.stats.linregress(series, happy)
    row = {'Criterion' : col, 'Correlation' : reg.rvalue, 
           '(Slope, Intercept)' : (reg.slope, reg.intercept)}
    rank.append(row)

df = pd.DataFrame(rank)
df.sort_values(['Correlation'], ascending = False, inplace = True)
table = ax.table(cellText = df.values,
                 colLabels = df.columns,
                 loc = 'center')
ax.axis('off')
plt.show()
