# TASK -> design model for prediction/classification of given data.
#      -> return y_eval based on X_eval data

import numpy as np

# MAX size 400 items / every item 250
X_public = np.load('X_public.npy')

# MAX size 400 items / every item 1
y_public = np.load('y_public.npy')

# MAX size 410 items / every item 250
X_eval = np.load('X_eval.npy')
