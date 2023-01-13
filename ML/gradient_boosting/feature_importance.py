import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error


def show_deviance(hyper_params, clf, x_test, y_test):
    test_scores = np.zeros((hyper_params['n_estimators'], ), dtype=np.float64)

    for idx, y_pred in enumerate(clf.staged_predict(x_test)):
        test_scores[idx] = clf.loss_(y_test, y_pred)

    plt.figure(figsize=(10, 10))
    plt.plot(np.arange(hyper_params['n_estimators']) + 1, clf.train_score_, 'b-', label='train score')
    plt.plot(np.arange(hyper_params['n_estimators']) + 1, test_scores, 'r-', label='test score')
    plt.legend(loc='upper right')
    plt.xlabel('iter')
    plt.ylabel('deviance')

    plt.show()


def show_feature_importance(clf, feature_names):
    feature_importance = clf.feature_importances_  # the importance of each feature
    # print(feature_importance)

    feature_importance = 100.0 * (feature_importance / feature_importance.max())  # to make max value as 1
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[
                        0]) + .5  # (position) to show these as a bar plot, if idx == 0, it will stick to the left side of the figure and some more reasons
    # print(pos)

    plt.figure(figsize=(8, 8))
    plt.title('feature importance')
    plt.barh(pos, feature_importance[sorted_idx], align='center')
    plt.yticks(pos, np.array(feature_names)[sorted_idx])
    plt.xlabel('importance')
    plt.show()


if __name__ == '__main__':
    data = datasets.load_boston()

    # train, test split
    x, y = shuffle(data.data, data.target, random_state=42)

    offset = int(x.shape[0] * 0.9)
    x_train, y_train = x[:offset], y[:offset]
    x_test, y_test = x[offset:], y[offset:]

    # model selection & hyperparameter
    hyper_params = {
        'n_estimators': 500,  # 500 of estimators(weak learners)
        'max_depth': 4,  # to avoid overfitting
        'min_samples_split': 2,
        'verbose': 0,  # show additional information while proceeding this method
        "learning_rate": 0.01,
        "loss": 'ls',  # ls = least squares estimator
    }

    clf = ensemble.GradientBoostingRegressor(**hyper_params)  # clf = classifier = model

    # training & loss
    clf.fit(x_train, y_train)

    mse = mean_squared_error(y_test, clf.predict(x_test))

    # print(mse)

    # visualize(only with regression)

    # print([len(x) for x in clf.staged_predict(x_test)])
    # print(len(list(clf.staged_predict(x_test))))

    # show_deviance(hyper_params, clf, x_test, y_test)

    # feature importance (only with ML, DL cannot find the factor that focused on while predicting)

    show_feature_importance(clf, data.feature_names)