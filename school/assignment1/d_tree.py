from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np

class _DecisionTree:

    def init():
        model = DecisionTreeRegressor(max_depth=4)
        return model


    def initBoost():
        rng = np.random.RandomState(2)
        model = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=450, random_state=rng)
        return model


    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model


    def initGrid(X,y):
        min_samples_split = [2,4,6,8]
        max_depth = [2,4,6,8]
        n_estimators=[50,100,150]
        bootstrap=[False, True]
        min_samples_leaf=[2,4,6,8]

        grid = {
            'min_samples_split':min_samples_split,
            'max_depth': max_depth,
            'min_samples_leaf':min_samples_leaf
        }
        model = DecisionTreeRegressor();
        gs = GridSearchCV(estimator=model, param_grid=grid,  verbose=10, n_jobs=-1)
        gs.fit(X,y)
        print(gs.best_params_)
        search = AdaBoostRegressor(gs)
        search.fit(X,y)
        return search



    def initGridClass(X,y):
        min_samples_split = [2,4,6,8]
        max_depth = [2,4,6,8,10]
        max_features=["auto"]
        class_weight=["balanced"]
        min_samples_leaf=[2,4,6,8]

        grid = {
            'min_samples_split':min_samples_split,
            'max_depth': max_depth,
            'max_features':max_features,
            'class_weight':class_weight,
            'min_samples_leaf':min_samples_leaf
        }
        model = DecisionTreeClassifier();
        gs = GridSearchCV(estimator=model, param_grid=grid,  verbose=10, n_jobs=-1)
        gs.fit(X,y)
        print(gs.best_params_)
        return gs
