#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.
    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

from time import time

from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

from sklearn import svm

clf = svm.SVC()


t = time()
print(clf.fit(features_train, labels_train))
print("training time:", round(time() - t, 3), "s")



t0 = time()
print(clf.predict(features_test))
print("predict time:", round(time() - t0, 3), "s")


print(clf.score(features_test, labels_test))




#########################################################
