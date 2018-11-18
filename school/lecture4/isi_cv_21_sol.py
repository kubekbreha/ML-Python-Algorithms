#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""


from IPython import get_ipython
get_ipython().magic('reset -sf') 

import numpy as np
from sklearn import preprocessing
from sklearn import datasets


iris = datasets.load_iris()
iris_X = iris.data
masking_array = np.random.binomial(1, .25, 
                    iris_X.shape).astype(bool)
iris_X[masking_array] = np.nan

print (iris_X[:5])

impute = preprocessing.Imputer()
iris_X_prime = impute.fit_transform(iris_X)
print ("Imputovane")
print (iris_X_prime[:5])

print ("Imputovane median")
impute = preprocessing.Imputer(strategy='median')
iris_X_prime = impute.fit_transform(iris_X)
print (iris_X_prime[:5])