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
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt

# Create the dataset with 1,000 samples.
X, y = datasets.make_classification(1000)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0)


rf = RandomForestClassifier()
rf.fit(X_train, y_train)

print ("Accuracy:\t", (y_test == rf.predict(X_test)).mean())
print ("Total Correct:\t", (y_test == rf.predict(X_test)).sum())



probs = rf.predict_proba(X_test)
probs_df = pd.DataFrame(probs, columns=['0', '1'])
probs_df['was_correct'] = rf.predict(X_test) == y_test



f, ax = plt.subplots(figsize=(7, 5))

probs_df.groupby('0').was_correct.mean().plot(kind='bar', ax=ax)
ax.set_title("Accuracy at 0 class probability")
ax.set_ylabel("% Correct")
ax.set_xlabel("% trees for 0")
plt.show()
