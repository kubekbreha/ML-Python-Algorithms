import numpy as linear_model

train = np.array([[-1, -1], [0, 0], [1, 1], [2, 2]])


clf = linear_model.LinearRegression()
clf.fit(train)

print(clf.coef_)
