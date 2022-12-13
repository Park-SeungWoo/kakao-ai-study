import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings

pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
warnings.filterwarnings('ignore')

df = pd.read_csv('./data_analysis/data/cosmetics_.csv')

"""frequency"""
df['gender'] = df['gender'].replace([1, 2], ['male', 'female'])  # replace
# print(df['gender'].value_counts())  # 132, 115 (male, female)
# print(len(df))  # 247

# df['gender'].value_counts().plot(kind='pie')
# df['gender'].value_counts().plot(kind='bar')
# plt.show()

df['marriage'] = df['marriage'].replace([1, 2, 3], ['single', 'married', 'other'])
# df['marriage'].value_counts().plot(kind='pie')
# plt.show()

# print(df['marriage'].value_counts() / len(df) * 100)  # percentage

"""technical statistic"""
# print(df['amount'].max())
# print(df['amount'].min())
# print(df['amount'].sum())
# print(df['amount'].mean())
# print((df['amount'] * df['count']).sum())
# print(df['amount'].var())  # variance
# print(df['amount'].std())  # standard deviation
# print(df['amount'].describe())
# print(df.info())

"""
# skewness and kurtosis
"""

# df['amount'].hist()
# plt.show()