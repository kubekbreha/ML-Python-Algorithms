from sklearn.preprocessing import Imputer, StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split

class DataPreprocessing:

    def loadData():
        X_public = np.load('X_public.npy')
        y_public = np.load('y_public.npy')
        X_eval = np.load('X_eval.npy')
        return [X_public, y_public, X_eval]


    def isDataCorupted(data):
        return np.any(np.isnan(data))


    def fixData(data):
        imp = Imputer(missing_values=np.nan, strategy='most_frequent', copy=False)
        imp = imp.fit(data)
        data = imp.transform(data)
        return data


    def scalerData(data):
        scaler = StandardScaler().fit(data)
        scaler.transform(data)
        return data


    def fixDataManually(data):
        NaN = np.any(np.isnan(data))
        print('is bad data present in y_public ? ', NaN)
        if NaN:
            for i, can in enumerate(data):
                bo = np.any(np.isnan(can))
                if bo:
                    cc = np.nan_to_num(can)
                    data[i] = cc
            NaN = np.any(~np.isnan(data))
            print('is data fixed in data ? ', NaN)
        return data


    def splitData(X_public, y_public, amount):
        X_public_h, X_public_t, y_public_h, y_public_t = train_test_split(
            X_public, y_public, test_size=amount)
        return [X_public_h, X_public_t, y_public_h, y_public_t]


    def splitDataManually(X_public, y_public, holdout_percentage):
        holdout = int((len(X_public)*holdout_percentage)/100)
        X_public_h, y_public_h = X_public[:holdout], y_public[:holdout]
        X_public_t, y_public_t = X_public[holdout:], y_public[holdout:]
        return [X_public_h, y_public_h, X_public_t, y_public_t]


    def saveData(mode, data):
        finalPrediction = model.predict(X_eval)

        if isinstance(finalPrediction[0], float):
            for i, can in enumerate(finalPrediction):
                finalPrediction[i] = round(finalPrediction[i])

        np.save("y_predikcia.npy", finalPrediction)

        test = np.load('y_predikcia.npy')
        print(test)
