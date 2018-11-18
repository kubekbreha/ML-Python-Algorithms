#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:04:18 2017

@author: pd
"""
#from IPython import get_ipython
#get_ipython().magic('reset -sf') 

import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

n_features=200
X, y = datasets.make_classification(750, n_features=n_features, n_informative=5, random_state=29)



X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0)

accuracies = []

for x in np.arange(1, n_features+1,5):
    dt = DecisionTreeClassifier(max_depth=x)
    
    dt.fit(X_train, y_train)
    
    preds = dt.predict(X_test)
    
    accuracies.append((preds == y_test).mean())
    

f, ax = plt.subplots(figsize=(7, 5))

ax.plot(range(1, n_features+1,5), accuracies, 'ko')
#ax.plot(range(1, n_features+1)[:12], accuracies[:12], color='k')

ax.set_title("Decision Tree Accuracy")
ax.set_ylabel("% Correct")
ax.set_xlabel("Max Depth")
plt.show()