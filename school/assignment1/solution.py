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


# ---- checking NaN/bad data
NaN_X = np.any(np.isnan(X_public))
print('is bad data present in X_public ? ', NaN_X)
if NaN_X:
    for i, can in enumerate(X_public):
        bo = np.any(np.isnan(can))
        if bo:
            cc = np.nan_to_num(can)
            X_public[i] = cc

    NaN_X = np.any(~np.isnan(X_public))
    print('is data fixed in X_public ? ', NaN_X)


NaN_y = np.any(np.isnan(y_public))
print('is bad data present in y_public ? ', NaN_y)
if NaN_y:
    for i, can in enumerate(y_public):
        bo = np.any(np.isnan(can))
        if bo:
            cc = np.nan_to_num(can)
            y_public[i] = cc

    NaN_y = np.any(~np.isnan(y_public))
    print('is data fixed in y_public ? ', NaN_y)


# ---- spliting data
holdout_percentage = 20
holdout = int((len(X_public)*holdout_percentage)/100)
# 20%
X_public_h, y_public_h = X_public[:holdout], y_public[:holdout]
# 80%
X_public_t, y_public_t = X_public[holdout:], y_public[holdout:]




# ------------------------------------------------------------------------------
# ------------------------------GRIDS-------------------------------------------
# ------------------------------------------------------------------------------

# # ----- ----- GRID random - RandomForestRegressor ----- ------
# # ---- Getting best parameters
# from sklearn.model_selection import RandomizedSearchCV
# from sklearn.ensemble import RandomForestRegressor
#
# n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# max_features = ['auto', 'sqrt']
# max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
# max_depth.append(None)
# min_samples_split = [2, 5, 10]
# min_samples_leaf = [1, 2, 4]
# bootstrap = [True, False]
#
# random_grid = {'n_estimators': n_estimators,
#                'max_features': max_features,
#                'max_depth': max_depth,
#                'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf,
#                'bootstrap': bootstrap}
#
# rf = RandomForestRegressor()
# rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# rf_random.fit(X_public_t, y_public_t)
#
# print('BEST PARAMETERS')
# pprint(rf_random.best_params_)
# # {'bootstrap': True,
# #  'max_depth': 10,
# #  'max_features': 'auto',
# #  'min_samples_leaf': 4,
# #  'min_samples_split': 5,
# #  'n_estimators': 200}

# ---- Using base parameters
# modelBase = RandomForestRegressor(n_estimators = 10, random_state = 42)
# modelBase.fit(X_public_t, y_public_t)
# evaluate(modelBase, X_public_h, y_public_h, 'RandomForrestRegressor', 'base')
#
# # ---- Using best parameters
# modelBest = RandomForestRegressor(bootstrap=True, max_depth=10, max_features='auto',
# min_samples_leaf=4, min_samples_split=5, n_estimators=200)
# modelBest.fit(X_public_t, y_public_t)
# evaluate(modelBest, X_public_h, y_public_h, 'RandomForrestRegressor', 'best')




# ----- ----- GRID search - RandomForestClassifier ----- -----
# ---- Getting best parameters
# from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
#
# n_estimators = [int(x) for x in np.linspace(start = 10, stop = 2000, num = 10)]
# max_features = ['auto', 'sqrt']
# max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
# max_depth.append(None)
# min_samples_split = [2, 5, 10]
# min_samples_leaf = [1, 2, 4]
# bootstrap = [True, False]
# criterion = ["gini", "entropy"]
#
#
# param_grid = {'n_estimators': n_estimators,
#                'max_features': max_features,
#                'max_depth': max_depth,
#                'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf,
#                'bootstrap': bootstrap,
#                'criterion': criterion}
#
# rf = RandomForestClassifier()
# rf_grid =  GridSearchCV(estimator = rf, param_grid = param_grid, cv = 3, verbose=2, n_jobs = -1)
# # rf_grid =  RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
#
# rf_grid.fit(X_public_t, y_public_t)
#
# print('BEST PARAMETERS')
# pprint(rf_grid.best_params_)

# ---- Using base parameters
modelBase = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
modelBase.fit(X_public_t, y_public_t)
evaluate(modelBase, X_public_h, y_public_h, 'RandomForestClassifier', 'base')

# ---- Using best parameters
modelBest = RandomForestClassifier(bootstrap= False, criterion= 'entropy', max_depth= None, max_features= 10, min_samples_split= 3)
modelBest.fit(X_public_t, y_public_t)
evaluate(modelBest, X_public_h, y_public_h, 'RandomForestClassifier', 'best')




# ----- ----- GRID - KNeighborsClassifier ----- -----
# from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
# from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
#
# n_neighbors = [int(x) for x in np.linspace(start = 2, stop = 20, num = 2)]
# weights = ['uniform', 'distance']
# algorithm = ['ball_tree', 'kd_tree', 'brute', 'auto']
# leaf_size = [int(x) for x in np.linspace(start = 10, stop = 70, num = 10)]
# p = [1, 2]
#
# param_grid = {'n_neighbors': n_neighbors,
#                'weights': weights,
#                'algorithm': algorithm,
#                'leaf_size': leaf_size,
#                'p': p}

# rf = KNeighborsClassifier()
# rf_grid =  GridSearchCV(estimator = rf, param_grid = param_grid, cv = 3, verbose=2, n_jobs = -1)
# # rf_grid =  RandomizedSearchCV(estimator = rf, param_distributions = param_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
#
# rf_grid.fit(X_public_t, y_public_t)
#
# print('BEST PARAMETERS')
# pprint(rf_grid.best_params_)
# {'algorithm': 'ball_tree',
#  'leaf_size': 70,
#  'n_neighbors': 20,
#  'p': 1,
#  'weights': 'distance'}


# clf = KNeighborsClassifier()
# # clf = KNeighborsRegressor()
# clf.fit(X_public_t, y_public_t)
# evaluate(clf, X_public_h, y_public_h, 'KNeighborsClassifier', 'best')
