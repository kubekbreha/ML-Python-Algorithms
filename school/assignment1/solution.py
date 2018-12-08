# ignore deprecation warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# ------------------------------------------------------------------------------
from data_preprocessing import DataPreprocessing
from representation import Representation
from sklearn.model_selection import GridSearchCV
import numpy as np

# load data
X_public, y_public, X_eval = DataPreprocessing.loadData()

# split data
X_public_h, X_public_t, y_public_h, y_public_t = DataPreprocessing.splitData(X_public, y_public, 0.70)

# fix data
X_public_t = DataPreprocessing.fixData(X_public_t)
X_public_h = DataPreprocessing.fixData(X_public_h)

# scale data
X_public_t = DataPreprocessing.scalerData(X_public_t)


# ------------------------------------------------------------------------------
from representation import Representation
from d_tree import _DecisionTree as dt

model = dt.initGrid(X_public_t, y_public_t)
Representation.evaluate(model, X_public_h, y_public_h, "DecisionTreeBoosted", "")


# ------------------------------------------------------------------------------
X_eval = DataPreprocessing.scalerData(X_eval)
DataPreprocessing.saveData(model, X_eval)
