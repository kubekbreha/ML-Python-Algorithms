#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""


from IPython import get_ipython
get_ipython().magic('reset -sf') 

from sklearn import datasets
import numpy as np
import itertools as it
from sklearn.tree import DecisionTreeClassifier


X, y = datasets.make_classification(n_samples=2000, n_features=10)


criteria = {'gini', 'entropy'}
max_features = {'auto', 'log2', None}


parameter_space = it.product(criteria, max_features)


train_set = np.random.choice([True, False], size=len(y))

accuracies = {}

for criterion, max_feature in parameter_space:
    dt = DecisionTreeClassifier(criterion=criterion, max_features=max_feature)
    
    dt.fit(X[train_set], y[train_set])
    
    accuracies[(criterion, max_feature)] = (dt.predict(X[~train_set]) == y[~train_set]).mean()    
    
print (accuracies)



from matplotlib import pyplot as plt
from matplotlib import cm
cmap = cm.RdBu_r
f, ax = plt.subplots(figsize=(7, 4))
ax.set_xticklabels([''] + list(criteria))
ax.set_yticklabels([''] + list(max_features))
plot_array = []
for max_feature in max_features:
    m = []
for criterion in criteria:
    m.append(accuracies[(criterion, max_feature)])
    plot_array.append(m)
colors = ax.matshow(plot_array, vmin=np.min(accuracies.values()) - 0.001, vmax=np.max(accuracies.values()) + 0.001, cmap=cmap)
f.colorbar(colors)
















