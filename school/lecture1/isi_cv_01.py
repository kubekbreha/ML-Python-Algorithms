#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:33:31 2017

@author: pd
v2: pridane vykreslenie tvary pre predikciu
"""

#from IPython import get_ipython
#get_ipython().magic('reset -sf') # clean workspace if the script is run in the same console

print ("--------------------------------------------------")
print ("Inteligentne systemy v informatike")
print ("--------------------------------------------------")
print ("")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.datasets import fetch_olivetti_faces
from isi_utils import print_faces
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

# fetch the faces data
faces = fetch_olivetti_faces()

print (faces.DESCR)  # dat do zatvpriek

print (faces.keys())
print (faces.images.shape)
print (faces.data.shape)
print (faces.target.shape)

print_faces(faces.images, faces.target, 80)
plt.show()
##### KROK 1 KONIEC ################################
# klasifikacia

svc = SVC(kernel='linear')

X_train, X_test, y_train, y_test = train_test_split(
        faces.data, faces.target, test_size=0.25, random_state=0)

svc.fit(X_train, y_train)

y_predict = svc.predict(X_test)

print (accuracy_score(y_predict, y_test))


#####################3 KROK 2 KONIEC ###############################
# zenim tvar na dvojrozmerny vhodny pre vykreslenie ako image
test_faces = [np.reshape(a, (64, 64)) for a in X_test]

print_faces(test_faces, y_predict, 10)

print_faces(test_faces, y_test, 10)

plt.show()
