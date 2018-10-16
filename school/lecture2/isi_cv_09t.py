#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

# random forests

# from IPython import get_ipython
# get_ipython().magic('reset -sf')

# take look omn this
# http://scikit-learn.org/stable/modules/grid_search.html

import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn import svm
import pandas as pd
import matplotlib.pyplot as plt

X_train= np.load('X_train.npy')
X_test = np.load('X_test.npy')
y_train = np.load('y_train.npy')
y_test = np.load('y_test.npy')


param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
 ]

rf =  svm.SVC(param_grid)

rf.fit(X_train, y_train)

print("accuracy: \n", (y_test == rf.predict(X_test)).mean())
print("total correct:", (y_test == rf.predict(X_test)).sum())
