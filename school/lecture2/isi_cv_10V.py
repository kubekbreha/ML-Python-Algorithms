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
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import metrics

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
#fig=plt.figure()
#fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# Two subplots, unpack the axes array immediately
#fig, axes = plt.subplots(1,5)
#fig.set_size_inches(12,12)

#for i in range(5):
  #  axes[i].set_aspect('equal')
#    axes[i].set_title('Feature ' + str(i))
#    axes[i].set_xlabel('Feature')
#    axes[i].set_ylabel('Median house value')
#    axes[i].set_xlim(x_min, x_max)
#    axes[i].set_ylim(y_min, y_max)

#    plt.sca(axes[i])
#    plt.scatter(X_train[:,i],y_train)


clf_svr= svm.SVR(kernel='linear')
clf_svr.fit(X_train, y_train)
print ("Score on train " , clf_svr.score(X_train, y_train))


y_pred=clf_svr.predict(X_test)
#    if show_accuracy:
#        print "Accuracy:{0:.3f}".format(metrics.accuracy_score(y,y_pred)),"\n"

print ("Classification report")
print( "Coefficient of determination:{0:.3f}".format(metrics.r2_score(y_test,y_pred)),"\n")