from sklearn.ensemble import AdaBoostRegressor
from sklearn.naive_bayes import GaussianNB
import numpy as np

class _Gaussian:

    def init(verbose):
        model = GaussianNB(verbose=verbose)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
