# TASK -> design model for prediction/classification of given data.
#      -> return y_eval based on X_eval data

import numpy as np

# MAX size 400 items / every item 250
X_public = np.load('X_public.npy')

# MAX size 400 items / every item 1
y_public = np.load('y_public.npy')

# MAX size 410 items / every item 250
X_eval = np.load('X_eval.npy')


# ----- ----- SVC ----- -----
from sklearn.svm import SVC, LinearSVC

# svc = SVC(kernel='linear')
svc = LinearSVC()

# checking NaN/bad data
NaN_X = np.any(np.isnan(X_public))
print('is bad data present in X_public ? ', NaN_X)
if NaN_X:
    np.nan_to_num(X_public)


NaN_y = np.any(np.isnan(y_public))
print('is bad data present in X_public ? ', NaN_y)
if NaN_y:
    np.nan_to_num(y_public)




svc.fit(X_public, y_public)

y_eval = svc.predict(X_eval)

print (accuracy_score(y_eval, y_test))
