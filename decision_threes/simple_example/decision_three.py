from __future__ import print_function
from sklearn import tree

X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print(clf.predict([[-2, 2]]))

# --------------------------------------