from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class _RandomForest:

    def init(verbose):
        model = RandomForestClassifier(max_depth=4, verbose=verbose)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
