#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd

Use 5-fold crossvalidation with arbitrary classifier 

"""


#from IPython import get_ipython
#get_ipython().magic('reset -sf') 

import numpy as np
from sklearn import datasets


X, y = datasets.make_regression(10000, 10, random_state=5)
