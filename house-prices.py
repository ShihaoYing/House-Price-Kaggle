import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


train = pd.read_csv('./house-prices-advanced-regression-techniques/train.csv')
test = pd.read_csv('./house-prices-advanced-regression-techniques/test.csv')

# print(train.head())
# print(test.head())


def sale_distribution():
    sns.displot(train['SalePrice'])
    plt.show()

# print(train['SalePrice'].describe())
# print("偏度: %f" % train['SalePrice'].skew())
# print("峰度: %f" % train['SalePrice'].kurt())


data = train.corr()
print(data['SalePrice'].sort_values())
