import os
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', palette='muted')
from scipy import stats
from scipy.stats import norm
from scipy.stats import skew


def load_data():
    train = pd.read_csv('./house-prices-advanced-regression-techniques/train.csv')
    test = pd.read_csv('./house-prices-advanced-regression-techniques/test.csv')
    
    print(train.head())
    print(test.head())
    return train, test


load_data()