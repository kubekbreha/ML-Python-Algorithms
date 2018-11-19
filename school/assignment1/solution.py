# ignore deprecation warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# ------------------------------------------------------------------------------
# TASK -> design model for prediction/classification of given data.
#      -> return y_eval based on X_eval data

# TODO: test on different parts of data, 1/5 -> 2/5 -> 3/5 ...


# ---- Evaluate ressults
def evaluate(model, test_features, test_labels):
    trained = model.predict(test_features)
    print('Model Performance')
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



# # ----- ----- SVC ----- -----
# from sklearn.svm import SVC, LinearSVC, SVR
#
# svc = SVC()
# # svc = LinearSVC(random_state=0, tol=1e-5)
# # svc = SVR(kernel='poly',degree=1)
#
# svc.fit(X_public_t, y_public_t)
# trained = svc.predict(X_public_h)
# print(accuracy_score(trained, y_public_h))
#

#
# # ----- ----- DecisionTree ----- -----
# from sklearn.tree import DecisionTreeClassifier
#
# dt = DecisionTreeClassifier(max_depth=5)
#
# dt.fit(X_public_t, y_public_t)
# trained = dt.predict(X_public_h)
# print(accuracy_score(trained, y_public_h))
#


# ----- ----- Random forest ----- -----
# from sklearn.ensemble import RandomForestClassifier
#
# # 85% succes
# dt = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
#
# dt.fit(X_public_t, y_public_t)
# trained = dt.predict(X_public_h)
# evaluate(dt, X_public_h, y_public_h)


# # ----- ----- MLP ----- -----
# from sklearn.neural_network import MLPClassifier
#
# svc = MLPClassifier(verbose=True)
#
# svc.fit(X_public_t, y_public_t)
# trained = svc.predict(X_public_h)
# print(accuracy_score(trained, y_public_h))




# ----- ----- GRID ----- ------
from pprint import pprint
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor

# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

pprint(random_grid)


# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()

# current parameters
pprint(rf.get_params())

# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
rf_random.fit(X_public_t, y_public_t)

print('BEST PARAMETERS')
pprint(rf_random.best_params_)
