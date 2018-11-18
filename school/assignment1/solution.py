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


bo = np.any(np.isnan(X_public))
if bo:
    print('----- bad data')


for i, can in enumerate(X_public):
    bo = np.any(np.isnan(can))
    if bo:
        print('bad data ---- ')
        print(can)
        cc = np.nan_to_num(can)
        X_public[i] = cc
        print(i)



print('-----------------------')
print('-----------------------')
print('-----------------------')
print('-----------------------')
print('-----------------------')
print('-----------------------')
print('-----------------------')

for can in X_public:
    bo = np.any(np.isnan(can))
    if bo:
        print('bad data ---- ')
        print(can)

print(X_public[398])



# ---- checking NaN/bad data
NaN_X = np.any(np.isnan(X_public))
print('is bad data present in X_public ? ', NaN_X)
if NaN_X:
    X_public = np.nan_to_num(X_public)
    # for val in X_public:
    #     np.nan_to_num(val)


NaN_y = np.any(np.isnan(y_public))
print('is bad data present in X_public ? ', NaN_y)
if NaN_y:
    y_public = np.nan_to_num(y_public)

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
