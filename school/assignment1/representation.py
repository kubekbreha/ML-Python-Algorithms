from sklearn.metrics import accuracy_score

class Representation:

    def evaluate(model, test_features, test_labels, algorithm, parameters):
        trained = model.predict(test_features)

        if isinstance(trained[0], float):
            for i, can in enumerate(trained):
                trained[i] = round(trained[i])
                
        print( algorithm +' model performance with ' + parameters + ' parameters.')
        print('Accuracy = {:0.2f}%.'.format(accuracy_score(trained, test_labels)*100))
        return 0
