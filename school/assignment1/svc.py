from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVC
import numpy as np

class _SVC:

    def init(verbose):
        model = SVC(verbose=verbose)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
