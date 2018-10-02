#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:41:09 2017

@author: pd
"""
# from IPython import get_ipython
# get_ipython().magic('reset -sf')

import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split


X, y = datasets.make_classification(n_samples=750, n_features=200,
                                    n_informative=5, random_state=29)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25,
                                                    random_state=0)

dt = DecisionTreeClassifier()


dt.fit(X_train, y_train)

preds = dt.predict(X_test)

print ((y_test == preds).mean())

# TASK: try out parameters









#### initial visualization

import matplotlib.pyplot as plt

plt.xlim(0.0, 20.0)
plt.ylim(0.0, 20.0)
# plt.scatter(X_train, y_train, color="b")
# plt.scatter(X_test, y_test, color="r")
plt.legend()
plt.show()
