#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

# random forests

#from IPython import get_ipython
#get_ipython().magic('reset -sf') 

import numpy as np
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm

# importovana databaza 
boston = load_boston()
print (boston.data.shape)
#print boston.feature_names
#print np.max(boston.target), np.min(boston.target), np.mean(boston.target)
#print boston.DESCR

# ako vyzera jedna vzorka dat
print (boston.data[0])
#print np.max(boston.data), np.min(boston.data), np.mean(boston.data)

X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.25, random_state=33)



x_min, x_max = X_train[:,0].min() - .5, X_train[:, 0].max() + .5
y_min, y_max = y_train.min() - .5, y_train.max() + .5

    
    
clf_svr= svm.SVR(kernel='linear')
clf_svr.fit(X_train, y_train)
print ("Score on train " , clf_svr.score(X_train, y_train))


clf_svr_poly= svm.SVR(kernel='poly',degree=1)
clf_svr_poly.fit(X_train, y_train)
print ("Score on train " , clf_svr_poly.score(X_train, y_train))

clf_svr_rbf= svm.SVR(kernel='rbf')
clf_svr_rbf.fit(X_train, y_train)

print ("Score on train " , clf_svr_rbf.score(X_train, y_train))

























