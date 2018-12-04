# ignore deprecation warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# ------------------------------------------------------------------------------
from data_preprocessing import DataPreprocessing
from representation import Representation

# load data
X_public, y_public, X_eval = DataPreprocessing.loadData()

# fix data
X_public = DataPreprocessing.fixData(X_public)
# y_public = DataPreprocessing.fixData(y_public)
X_eval = DataPreprocessing.fixData(X_eval)

# scale data
X_public = DataPreprocessing.scalerData(X_public)
X_eval = DataPreprocessing.scalerData(X_eval)

# split data
X_public_h, y_public_h, X_public_t, y_public_t = DataPreprocessing.splitData(X_public, y_public)

print(X_public_h)




# from sklearn.ensemble import AdaBoostRegressor
# from sklearn.tree import DecisionTreeRegressor
#
#
# rng = np.random.RandomState(1)
# clf = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=450, random_state=rng)
# clf.fit(X_public_t, y_public_t)
# evaluate(clf, X_public_h, y_public_h, 'DecisionTreeRegressor', 'base')
