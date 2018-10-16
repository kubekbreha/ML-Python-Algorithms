#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

# random forests

# from IPython import get_ipython
# get_ipython().magic('reset -sf')

import numpy as np
from sklearn import datasets

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import train_test_split


from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score

# Create the dataset with 1,000 samples.
X, y = datasets.make_classification(1000)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,
                                                    random_state=0)


# Vyrieste ulohu metodou random forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

print("accuracy: \n", (y_test == rf.predict(X_test)).mean())
print("total correct:", (y_test == rf.predict(X_test)).sum())


# predicted_test = rf.predict(X_test, y_test)
# print(predicted_test[0])

# test_score = accuracy_score(X_test, y_test)
# print(test_score)
