import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import ensemble, datasets
from sklearn.metrics import accuracy_score, roc_curve, auc, classification_report
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance


# load and check dataset
cancer = datasets.load_breast_cancer()
x, y = cancer.data, cancer.target

xdf = pd.DataFrame(x)
ydf = pd.DataFrame(y)

# split datas
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1, random_state=42)

# create model
params = {
    'n_estimators': 1000,
    'max_depth': 4,  # to avoid overfitting
    'min_samples_split': 2,
    'verbose': 0,  # show additional information while proceeding this method
    "learning_rate": 0.01,
}

clf = ensemble.GradientBoostingClassifier(**params)

# train
clf.fit(train_x, train_y)

# predict
predict = clf.predict(test_x)

# scoring
acc = accuracy_score(test_y, predict)

# print(clf.score(test_x, test_y))  # same as acc

# visualizing
# train_score = np.zeros((params['n_estimators'],))
# for idx, pred in enumerate(clf.staged_predict(train_x)):
#     train_score[idx] = accuracy_score(train_y, pred)
#
# test_score = np.zeros((params['n_estimators'],))
# for idx, pred in enumerate(clf.staged_predict(test_x)):
#     test_score[idx] = accuracy_score(test_y, pred)
#
# fig = plt.figure(figsize=(8, 8))
# plt.subplot(1, 1, 1)
# plt.plot(np.arange(params['n_estimators']) + 1, train_score, 'b-', label='train')
# plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-', label='test')
# plt.legend(loc='upper right')
# plt.xlabel('epoch')
# plt.ylabel('accuracy')
# fig.tight_layout()
# plt.show()

# feature importance
# fi = clf.feature_importances_
# sorted_idx = np.argsort(fi)
# pos = np.arange(sorted_idx.shape[0]) + .5
#
# ffig = plt.figure(figsize=(8,8))
# plt.barh(pos, fi[sorted_idx], align='center')
# plt.yticks(pos, np.array(cancer.feature_names)[sorted_idx])
# plt.show()

# by permutation importance
# res = permutation_importance(clf, test_x, test_y, n_repeats=10, n_jobs=2, random_state=42)  # n_jobs => parallel computing
#
# sorted_idx = res.importances_mean.argsort()
#
# plt.boxplot(res.importances[sorted_idx].T, vert=False, labels=np.array(cancer.feature_names)[sorted_idx])
# plt.title('permutation importance')
#
# plt.tight_layout()
# plt.show()

# ROC curve
# fpr, tpr, _ = roc_curve(y_true=test_y, y_score=clf.predict_proba(test_x)[:, 1])
# roc_auc = auc(fpr, tpr)
#
# plt.figure(figsize=(8, 8))
# plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area={roc_auc:.3f})')
# plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
# plt.xlim([0, 1])
# plt.ylim([0, 1.05])
# plt.xlabel('false positive')
# plt.ylabel('true positive')
# plt.legend(loc='lower right')
# plt.show()

# classification report
pred = clf.predict(test_x)
cr = classification_report(test_y, pred)
print(cr)
print(clf.score(train_x, train_y))
print(clf.score(test_x, test_y))