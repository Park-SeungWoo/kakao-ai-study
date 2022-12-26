import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn import model_selection, datasets, linear_model
from sklearn.metrics import mean_squared_error, accuracy_score, roc_curve, auc

import warnings
warnings.filterwarnings('ignore')


pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# load dataset
boston = datasets.load_boston()

# preprocessing dataset
data = boston['data']
target = boston['target'].reshape(-1, 1)
label = np.array([1 if x > (sum(target) / len(target)) else 0 for x in target]).reshape(-1, 1)  # convert two class 0, 1 that over the mean or not.

# print(data.shape)
# print(target.shape)
# print(label.shape)

data_df = pd.DataFrame(data=data, columns=boston['feature_names'])
label_df = pd.DataFrame({'price': target.reshape(-1), 'label': label.reshape(-1)})
# print(data_df.head(10))
# print(label_df.head(10))

# x = data[:, (5, 12)]  # use two features
x = data[:, 5:13]  # more features
y = label

train_x, test_x, train_y, test_y = model_selection.train_test_split(x, y, test_size=0.3, random_state=42)
# print(train_x.shape)
# print(test_x.shape)
# print(train_y.shape)
# print(test_y.shape)

# create model
model = linear_model.LogisticRegression()

# train
model.fit(train_x, train_y)

# predict
pred = model.predict(test_x)
pred_proba = model.predict_proba(test_x)

# check results
print(f'acc : {accuracy_score(test_y, pred) * 100}%')  # accuracy_score => classification only

# visualization of ROC curve
fpr, tpr, _ = roc_curve(y_true=test_y, y_score=pred_proba[:, 1])

auc_val = auc(fpr, tpr)
print(f'auc : {auc_val}')  # totally different with accuracy score

plt.figure(figsize=(10, 10))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % auc_val)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.legend(loc='lower right')
plt.title('ROC curve')
plt.show()