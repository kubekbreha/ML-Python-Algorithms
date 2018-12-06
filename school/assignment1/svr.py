from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR
import numpy as np

class _SVR:

    def init(verbose):
        model = SVR(kernel='poly',degree=1, verbose=verbose)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
