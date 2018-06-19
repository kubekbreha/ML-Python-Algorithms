#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project
    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score


features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = svm.SVC(kernel="rbf", C=11000)
t0 = time()
clf.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

t1 = time()
prediction = clf.predict(features_test)
print "Prediction: ", prediction
print "Prediction time:", round(time()-t1, 3), "s"

print accuracy_score(prediction, labels_test)

chris = []
for i in prediction:
    if i == 1:
        chris.append(i)

print len(chris)
