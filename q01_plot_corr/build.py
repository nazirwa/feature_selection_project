# Default imports
import pandas as pd
import matplotlib
matplotlib.use("Agg")
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:

import matplotlib.pyplot as plt
import seaborn as sns

def plot_corr(df,size=11):
    corr = data.corr()

    # plot correlation matrix
    f, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
                square=True, ax=ax)

    return None
# plot_corr(data)
