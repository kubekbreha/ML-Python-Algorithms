#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

# from IPython import get_ipython
# get_ipython().magic('reset -sf')

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import LinearSVC, SVC

from itertools import product
from collections import namedtuple

X, y = datasets.make_blobs(n_features=2, centers=2)
svm = SVC(kernel='linear')
#svm = LinearSVC()
svm.fit(X, y)

Point = namedtuple('Point', ['x', 'y', 'outcome'])

decision_boundery = []

xmin, xmax = np.percentile(X[:, 0], [0, 100])
ymin, ymax = np.percentile(X[:, 1], [0, 100])

for xpt, ypt in product(np.linspace(xmin-2.5, xmax+2.5, 20), np.linspace(ymin-2.5, ymax+2.5, 20)):

    p = Point(xpt, ypt, svm.predict(np.array([xpt, ypt]).reshape(1, -1) ))

    decision_boundery.append(p)


f, ax = plt.subplots(figsize=(7, 5))
colors = np.array(['r', 'b'])

for xpt, ypt, pt in decision_boundery:
    ax.scatter(xpt, ypt, color=colors[pt[0]], alpha=.15)


ax.scatter(X[:, 0], X[:, 1], color=colors[y], s=30)

ax.set_ylim(ymin, ymax)
ax.set_xlim(xmin, xmax)
plt.show()
