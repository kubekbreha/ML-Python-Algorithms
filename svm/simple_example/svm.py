from sklearn import svm
from time import time

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()

t0 = time()
clf.fit(X, y)
print("predict time:", round(time() - t0, 3), "s")

print(clf.predict([[2., 2.], [-3., -5.]]))





### multi class
X2 = [[0], [1], [2], [3]]
Y2 = [0, 1, 2, 3]
clf2 = svm.SVC(decision_function_shape='ovo')
clf2.fit(X2, Y2)




dec = clf2.decision_function([[1]])
print(dec.shape[1])  # 4 classes: 4*3/2 = 6

clf2.decision_function_shape = "ovr"
dec = clf2.decision_function([[1]])
print(dec.shape[1])  # 4 classes







lin_clf = svm.LinearSVC()
lin_clf.fit(X2, Y2)

dec = lin_clf.decision_function([[1]])
print(dec.shape[1])
