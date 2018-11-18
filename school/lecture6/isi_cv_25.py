#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd

Division into folds for model validation
"""


#from IPython import get_ipython
#get_ipython().magic('reset -sf')

import numpy as np
from sklearn.datasets import make_regression
from sklearn.cross_validation import KFold


N = 1000
holdout = 200

# priprav syntetickych dat
X, y = make_regression(N, shuffle=True, random_state=None)

# odlozime 200 vzoriek
X_h, y_h = X[:holdout], y[:holdout]
X_t, y_t = X[holdout:], y[holdout:]

kfold = KFold(len(y_t), n_folds=10)

output_string = "Fold: {}, N_train: {}, N_test: {}"

for i, (train, test) in enumerate(kfold):
    print( output_string.format(i, len(y_t[train]), len(y_t[test])))
    clf.fit(X_t[train], y_t[train])
