# ignore deprecation warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# ------------------------------------------------------------------------------
# TASK -> design model for prediction/classification of given data.
#      -> return y_eval based on X_eval data

# TODO: test on different parts of data, 1/5 -> 2/5 -> 3/5 ...
from pprint import pprint

# ---- Evaluate ressults
def evaluate(model, test_features, test_labels, algorithm, parameters):
    trained = model.predict(test_features)

    # if values are float convert them to integer
    if isinstance(trained[0], float):
        for i, can in enumerate(trained):
            trained[i] = round(trained[i])

    # round(10)
    print( algorithm +' model performance with ' + parameters + ' parameters.')
    print('Accuracy = {:0.2f}%.'.format(accuracy_score(trained, test_labels)*100))
    return 0


import numpy as np
from sklearn.metrics import accuracy_score


# ---- getting data
# MAX size 400 items / every item 250
X_public = np.load('X_public.npy')

# MAX size 400 items / every item 1
y_public = np.load('y_public.npy')

# MAX size 410 items / every item 250
X_eval = np.load('X_eval.npy')

# ---- checking NaN/bad data -> manually
# NaN_X = np.any(np.isnan(X_public))
# print('is bad data present in X_public ? ', NaN_X)
# if NaN_X:
#     for i, can in enumerate(X_public):
#         bo = np.any(np.isnan(can))
#         if bo:
#             cc = np.nan_to_num(can)
#             X_public[i] = cc
#
#     NaN_X = np.any(~np.isnan(X_public))
#     print('is data fixed in X_public ? ', NaN_X)
#
#
# NaN_y = np.any(np.isnan(y_public))
# print('is bad data present in y_public ? ', NaN_y)
# if NaN_y:
#     for i, can in enumerate(y_public):
#         bo = np.any(np.isnan(can))
#         if bo:
#             cc = np.nan_to_num(can)
#             y_public[i] = cc
#
#     NaN_y = np.any(~np.isnan(y_public))
#     print('is data fixed in y_public ? ', NaN_y)

# ---- checking NaN/bad data -> skicit
from sklearn.preprocessing import Imputer, StandardScaler

# fix corrupt data
imp = Imputer(missing_values=np.nan, strategy='most_frequent', copy=False)
imp = imp.fit(X_public)
X_public = imp.transform(X_public)

# scaler data
scaler = StandardScaler().fit(X_public)
scaler.transform(X_public)

# ---- spliting data -> Manually
# holdout_percentage = 15
# holdout = int((len(X_public)*holdout_percentage)/100)
# # 20%
# X_public_h, y_public_h = X_public[:holdout], y_public[:holdout]
# # 80%
# X_public_t, y_public_t = X_public[holdout:], y_public[holdout:]


# ---- spliting data -> sklearn
from sklearn.model_selection import train_test_split

X_public_h, X_public_t, y_public_h, y_public_t = train_test_split(
    X_public, y_public, test_size=0.7, random_state=4)



from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

rng = np.random.RandomState(1)
clf = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=450, random_state=rng)
clf.fit(X_public_t, y_public_t)
evaluate(clf, X_public_h, y_public_h, 'DecisionTreeRegressor', 'base')
