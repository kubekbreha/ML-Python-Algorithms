#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""


#from IPython import get_ipython
#get_ipython().magic('reset -sf') 

import numpy as np
from sklearn import preprocessing
from sklearn import datasets


boston = datasets.load_boston()
X, y = boston.data, boston.target

print (X[:, :3].mean(axis=0))
print (X[:, :3].std(axis=0))