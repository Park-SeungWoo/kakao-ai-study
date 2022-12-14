import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

# print(df['amount'].skew())
# print(df['amount'].kurtosis())

# df['decision'].hist()  # has negative skewness
# plt.show()

# df['job'].hist()  # has lower kurtosis value
# plt.show()

# print(df['job'].kurtosis())

# print(df.describe())

# all columns
# df.hist(bins=50, figsize=(15, 10))
# plt.show()

df_amount = df['amount']
# df_amount.hist(bins=50, figsize=(15, 10))
# plt.show()

df_count = df['count']
# df_count.hist(bins=50, figsize=(15, 10))
# plt.show()

# print(df[df['count'] > 30])
# print(df[df['amount'] > 3000000])

# sns.distplot(df_amount, rug=True)
# plt.show()

# sns.jointplot(x='amount', y='count', data=df, kind='kde')  # kde : kernel density estimation
# plt.show()


#############remove outlier
# df.boxplot(column='amount')
# plt.show()

# IQR
q1 = df_amount.quantile(0.25)
q3 = df_amount.quantile(0.75)
iqr = q3 - q1
min = q1 - (1.5 * iqr)
max = q3 + (1.5 * iqr)

# print(min)
# print(max)

# find outliers
outliers = df[(df['amount'] > max) | (df['amount'] < min)]  # not necessary (df['amount'] < min)
norm_datas = df[(df['amount'] < max) & (df['amount'] > min)]
# print(outliers)
# print(norm_datas)
# norm_datas.boxplot(column='amount')
# plt.show()

# count iqr
# df.boxplot(column='count')
# plt.show()
# max 10

norm_df = df[(df['count'] < 10) & (df['amount'] < max)]
# print(norm_df)

# norm_df[['amount', 'count']].hist(bins=50)
# df[['amount', 'count']].hist(bins=50)
# plt.show()

# sns.jointplot(x='amount', y='count', data=df)
# sns.jointplot(x='amount', y='count', data=norm_df)
# plt.show()

# feature scaling with log(in count(1~10), amount(10000~) column)
# sns.jointplot(x='amount', y='count', data=norm_df, kind='kde')
# plt.show()

norm_df = norm_df[['count', 'amount']]
norm_df['logamount'] = np.log(norm_df['amount'])
sns.jointplot(x='logamount', y='count', data=norm_df, kind='kde')
plt.show()