import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance

from feature_importance import show_deviance, show_feature_importance

# permutation importance is more recommended that feature importance

# load data
diabetes = datasets.load_diabetes()
x, y = diabetes.data, diabetes.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

# model selection & fit
hyper_params = {
    'n_estimators': 500,
    'max_depth': 4,
    'min_samples_split': 2,
    # 'verbose': 0,
    "learning_rate": 0.01,
    "loss": 'ls'
}

model = ensemble.GradientBoostingRegressor(**hyper_params)

model.fit(x_train, y_train)

# loss
mse = mean_squared_error(y_test, model.predict(x_test))
# print(mse)

# deviance
# show_deviance(hyper_params, model, x_test, y_test)

# feature importance
# show_feature_importance (model, diabetes.feature_names)

# permutation importance (better than feature importance, but there are some models that cannot see this, then use feature importance)
plt.figure(figsize=(8, 8))

res = permutation_importance(model, x_test, y_test, n_repeats=10, n_jobs=2, random_state=42)
print(res)
# importances_mean : the mean of each feature's res
# importances_std : the std of each feature's res
# importances : results of each fearute
# scoring ->

sorted_idx = res.importances_mean.argsort()
# print(sorted_idx)
# print(res.importances)

plt.boxplot(res.importances[sorted_idx].T, vert=False, labels=np.array(diabetes.feature_names)[sorted_idx])
plt.title('permutation importance')

plt.tight_layout()
plt.show()