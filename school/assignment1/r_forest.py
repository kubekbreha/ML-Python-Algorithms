from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class RandomForest:

    def init():
        model = RandomForestClassifier(max_depth=4)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
