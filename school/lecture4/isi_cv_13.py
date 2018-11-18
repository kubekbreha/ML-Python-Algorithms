#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""


#from IPython import get_ipython
#get_ipython().magic('reset -sf') 
import pandas as pd
import numpy as np


#datas = pd.DataFrame()

titanic_data = pd.read_csv('data/titanic.txt')

titanic_y = np.array(titanic_data.survived)


# remove features that seems irelevant
titanic_reduced = titanic_data.drop(columns=["row.names","survived","name","embarked", "home.dest","room", "ticket", "boat"])