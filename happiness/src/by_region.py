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
data.info()

"""
# can get specific rows
print ('getting info on costa rica')
table = ax.table(cellText = data[data['Country'] == 'Costa Rica'].values,
                 colLabels = data.columns,
                 loc = 'center')
table.scale(2,1)
ax.axis('off')
plt.show()
"""

rows_list = []
# pandas can be used to create new datasets
# for example, this one averaging happiness over regions
for region in data['Region'].unique():
    total_rank = data.loc[data['Region'] == region]['Happiness Score'].sum()
    total_nation = len(data.loc[data['Region'] == region])
    avg = total_rank / total_nation
    dict1 = {'Region': region,
             'Average Happiness by Region': avg,
             'Size of Region': total_nation}
    rows_list.append(dict1)
by_region = pd.DataFrame(rows_list)
by_region.sort_values(['Average Happiness by Region'], ascending = False, inplace = True)
# by_region.info()
table = ax.table(cellText = by_region.values,
                 colLabels = by_region.columns,
                 loc = 'center')
ax.axis('off')
plt.show()
