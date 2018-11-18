#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd

Design a basic search grid in the parameter space
+Iterate through the grid
 
"""


#from IPython import get_ipython
#get_ipython().magic('reset -sf') 

from sklearn import datasets
import numpy as np
import itertools as it
from sklearn.tree import DecisionTreeClassifier


X, y = datasets.make_classification(n_samples=2000, n_features=10, random_state=59)






















