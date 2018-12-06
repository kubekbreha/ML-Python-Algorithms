from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
import numpy as np

class DecisionTree:

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
