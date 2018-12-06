from sklearn.ensemble import AdaBoostRegressor
from sklearn.naive_bayes import GaussianNB
import numpy as np

class Gaussian:

    def init():
        model = GaussianNB()
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
