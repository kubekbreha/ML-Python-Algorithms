from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

class _RandomForest:

    def init(verbose):
        model = RandomForestClassifier(max_depth=4, verbose=verbose)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model



    def initGrid(X,y):
        min_samples_split = [2,4,6,8]
        max_depth = [2,4,6,8,10]
        max_features=["auto"]
        class_weight=["balanced", "balanced_subsample"]
        n_estimators=[50]
        min_samples_leaf=[2,4,6,8]

        grid = {
            'min_samples_split':min_samples_split,
            'max_depth': max_depth,
            'max_features':max_features,
            'class_weight':class_weight,
            'n_estimators':n_estimators,
            'min_samples_leaf':min_samples_leaf
        }

        model = RandomForestClassifier();
        search = GridSearchCV(estimator=model, param_grid=grid,  verbose=10, n_jobs=-1)
        search.fit(X,y)
        return search
