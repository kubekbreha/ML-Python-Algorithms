#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:41:09 2017

@author: pd
"""
#from IPython import get_ipython
#get_ipython().magic('reset -sf')


import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

X, Y = datasets.make_classification(n_samples=1000,
                                    n_features=3, n_redundant=0)

# print(X, Y)

clf = DecisionTreeClassifier()
clf = clf.fit(X*10, Y*10)

x,y,z = clf.predict([[-2, 2, 0],[-131, -123, -435],[-22, 100, 53]])



#### initial visualization
plt.xlim(0.0, 20.0)
plt.ylim(0.0, 20.0)
# plt.scatter(X, Y, color="b", label="fast")
# plt.scatter(x, y, color="r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
plt.show()
