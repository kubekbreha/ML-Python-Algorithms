from sklearn.ensemble import AdaBoostRegressor
from sklearn.neural_network import MLPClassifier, MLPRegressor
import numpy as np

class _MLP:

    def initClassifier(verbose):
        model = MLPClassifier(verbose=verbose)
        return model

    def initRegressor(verbose):
        model = MLPRegressor(verbose=verbose)
        return model

    def initBoostRegressor(verbose):
        rng = np.random.RandomState(2)
        model = AdaBoostRegressor(MLPRegressor(verbose=verbose), n_estimators=450, random_state=rng)
        return model

    def train(model, X_public_t, y_public_t):
        model.fit(X_public_t, y_public_t)
        return model
