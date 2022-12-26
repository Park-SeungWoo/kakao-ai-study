from sklearn import datasets, linear_model, model_selection, metrics
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

pri = datasets.load_boston()

# doesn't have any meaning. Just handling for proficiency.
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

# use only one feature
# All datas always should be a matrix shape at every model.
x = data[:, 12:13]  # LSTAT
# same as above
# x = data[:, 12]
# x = x.reshape(-1, 1)
y = label

train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y, test_size=0.3, random_state=42)  # random_state : set random seed (usually use 42)
# print(train_x.shape)  # 354, 1
# print(train_y.shape)
# print(test_x.shape)  # 152, 1
# print(test_y.shape)

model = linear_model.LinearRegression()

# train
model.fit(train_x, train_y)

# print(model.coef_)  # weight
# print(model.intercept_)  # bias

# predict
res = model.predict(test_x)
# print(res)
# print(train_y)

# check difference
# for i in range(len(res)):
#     print(f"{res[i]} {test_y[i]}")

# print(np.sqrt(np.mean((res - test_y) ** 2)))
# print(np.sqrt(metrics.mean_squared_error(test_y, res)))  # same as above

# visualization
plt.figure(figsize=(10, 10))
plt.scatter(test_x, test_y, color='black')
plt.scatter(train_x, train_y, color="red", s=1)
plt.plot(test_x, res, color='blue', linewidth=3)
plt.xlabel('LSTAT')
plt.ylabel('price')
plt.show()