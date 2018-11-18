# TASK -> design model for prediction/classification of given data.
#      -> return y_eval based on X_eval data

import numpy as np
from sklearn.metrics import accuracy_score

# ---- getting data
# MAX size 400 items / every item 250
X_public = np.load('X_public.npy')

# MAX size 400 items / every item 1
y_public = np.load('y_public.npy')

# MAX size 410 items / every item 250
X_eval = np.load('X_eval.npy')


# ---- checking NaN/bad data
NaN_X = np.any(np.isnan(X_public))
print('is bad data present in X_public ? ', NaN_X)
if NaN_X:
    for i, can in enumerate(X_public):
        bo = np.any(np.isnan(can))
        if bo:
            cc = np.nan_to_num(can)
            X_public[i] = cc

    NaN_X = np.any(~np.isnan(X_public))
    print('is data fixed in X_public ? ', NaN_X)


NaN_y = np.any(np.isnan(y_public))
print('is bad data present in y_public ? ', NaN_y)
if NaN_y:
    for i, can in enumerate(y_public):
        bo = np.any(np.isnan(can))
        if bo:
            cc = np.nan_to_num(can)
            y_public[i] = cc

    NaN_y = np.any(~np.isnan(y_public))
    print('is data fixed in y_public ? ', NaN_y)


# ---- spliting data
holdout = 20
# 20
X_public_h, y_public_h = X_public[:holdout], y_public[:holdout]
# 380
X_public_t, y_public_t = X_public[holdout:], y_public[holdout:]





# ----- ----- SVC ----- -----
from sklearn.svm import SVC, LinearSVC
# svc = SVC(kernel='linear')
svc = LinearSVC()

# svc.fit(X_public_h, y_public_h)
# y_eval = svc.predict(X_eval)
# print (accuracy_score(y_eval, y_public))
