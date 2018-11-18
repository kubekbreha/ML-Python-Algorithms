#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:41:09 2017

@author: pd
"""
from IPython import get_ipython
get_ipython().magic('reset -sf') 


from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.make_classification(n_samples=1000, n_features=3, n_redundant=0)

dt = DecisionTreeClassifier()

dt.fit(X, y)
y_predict = dt.predict(X)

print( (y_predict == y).mean())

