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
X_public_h, X_public_t, y_public_h, y_public_t = DataPreprocessing.splitData(X_public, y_public)


# ------------------------------------------------------------------------------
from representation import Representation
# -----------------------------
# from d_tree import DecisionTree as dt
#
# model = dt.init()
# modelBoosted = dt.initBoost()
#
# model = dt.train(model, X_public_t, y_public_t)
# modelBoosted = dt.train(modelBoosted, X_public_t, y_public_t)
#
# Representation.evaluate(model, X_public_h, y_public_h, "DecisionTree", "")
# Representation.evaluate(modelBoosted, X_public_h, y_public_h, "DecisionTree", "")

# -----------------------------
# from r_forest import RandomForest as rf
#
# model = rf.init()
# model = rf.train(model, X_public_t, y_public_t)
# Representation.evaluate(model, X_public_h, y_public_h, "DecisionTree", "")

# -----------------------------
from gaussian import Gaussian as g

model = g.init()
model = g.train(model, X_public_t, y_public_t)
Representation.evaluate(model, X_public_h, y_public_h, "Gausian", "")
