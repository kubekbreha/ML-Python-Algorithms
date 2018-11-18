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
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression


X, y = make_classification(1000, n_features=5,
                           random_state=5)

lr = LogisticRegression(class_weight='auto')


#'penalty': ['l1', 'l2'],
#    'C': [1, 2, 3, 4, 5]
















