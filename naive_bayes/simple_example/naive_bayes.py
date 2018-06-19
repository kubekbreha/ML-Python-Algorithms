import numpy as np

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

Xtest = np.array([[-1, -0.5], [-1.5, -1], [-2.5, -2], [0.5, 1], [1.7, 1], [3, 2]])
Ytest = np.array([0, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
GaussianNB()


print(clf.predict([[3, 2],[0,0]]))
print(clf.score(Xtest,Ytest))
