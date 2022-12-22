from sklearn import datasets, linear_model, model_selection, metrics
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

pri = datasets.load_boston()

# deosn't have any meaning. Just handling for proficiency.
# data_df = pd.DataFrame(data=pri.data, columns=pri.feature_names)
# print(data_df['CHAS'].value_counts())
# print(data_df['RAD'].value_counts(sort=False))
# targ_df = pd.DataFrame(data=pri.target, columns=['MEDV'])
# df = pd.concat([data_df, targ_df], axis=1)
# print(df.describe())

data = pri.data
label = pri.target

# print(data.shape)
# print(label.shape)
label = label.reshape(-1, 1)

x = data[:, 12:13]  # LSTAT
# print(x)
y = label

