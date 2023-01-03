import numpy as np
import scipy.stats 
import pandas as pd 

# correlation (just R) in numpy

x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
R = np.corrcoef(x, y)
print('R:', R)

# linear regression in scipy 
result = scipy.stats.linregress(x, y)
print('linreg:', result.slope, result.intercept, result.rvalue, result.pvalue, result.stderr)

# correlation in scipy, has pearson, spearman, kendall
print(scipy.stats.pearsonr(x, y))
print(scipy.stats.spearmanr(x, y))
print(scipy.stats.kendalltau(x, y))
