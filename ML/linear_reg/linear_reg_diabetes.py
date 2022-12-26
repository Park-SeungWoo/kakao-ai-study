import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import model_selection, datasets, linear_model, ensemble
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

diabetes = datasets.load_diabetes()

data = diabetes['data']
label = diabetes['target']

# print(diabetes.DESCR)

df = pd.DataFrame(data=data, columns=diabetes.feature_names)
# print(df.head(5))
# print(sum(df['age'].values ** 2))  # all data was sclaed by the std (sum of squared them is 1)

label = label.reshape(-1, 1)
# print(data.shape)
# print(label.shape)

# select feature (bmi)
# data = data[:, 2]
# data = data.reshape(-1, 1)

train_x, test_x, train_y, test_y = model_selection.train_test_split(data, label, test_size=0.3, random_state=42)

# print(train_x.shape)  # 309, 1
# print(test_x.shape)  # 133, 1
# print(train_y.shape)  # 309, 1
# print(test_y.shape)  # 133, 1

# model select
# model = linear_model.LinearRegression()
model = ensemble.GradientBoostingRegressor(learning_rate=0.01)

# train
model.fit(train_x, train_y)
# print(model.coef_)
# print(model.intercept_)

res = model.predict(test_x)

# for i in range(len(res)):
#     print(f'{res[i]}, {test_y[i]}')

mse = mean_squared_error(test_y, res)
print(f"training mse : {np.sqrt(mean_squared_error(train_y, model.predict(train_x)))}")
print(f"test mse : {np.sqrt(mse)}")

# visualization

# with all features and visualize with one feature
# plt.figure(figsize=(10, 10))
# plt.scatter([x[0] for x in test_x], res, color='black')
# plt.scatter([x[0] for x in test_x], test_y, color='red')
# plt.plot([x[0] for x in test_x], res, color="blue", linewidth=3)
# plt.show()

# plt.figure(figsize=(10, 10))
# plt.scatter(test_x, test_y, color='black')
# plt.scatter(train_x, train_y, color='red', s=1)
# plt.plot(test_x, res, color='blue', linewidth=3)
# plt.show()

