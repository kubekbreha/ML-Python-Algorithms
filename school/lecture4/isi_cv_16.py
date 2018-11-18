#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

#  scikit version 19 -  ONE HOT ENCODER WAS CHANGED IN 20 !!!!!!!
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

titanic_data = pd.read_csv('data/titanic.txt')

titanic_y = np.array(titanic_data.survived)

# remove features that seems irelevant
titanic_reduced = titanic_data.drop(columns=["row.names","survived","name","embarked", "home.dest","room", "ticket", "boat"])

print ("Passanger data")
print (titanic_reduced.loc[12])

# imputacia (mozno vykonat aj cez Imputer objekt, je vsak predtym potrebne nahradit 'NA'
# nan typom) -  DOMACA ULOHA

ages=titanic_reduced.iloc[:, 1]   # get age column
ages=np.array(ages)   

mean_age = np.mean(ages[~np.isnan(ages)]) # vypocita mean veku 


ages[np.isnan(ages)]=mean_age    # replace nan with mean age


titanic_reduced["age"]=ages  # repalace data in dataframe

print ("\nPassanger data")
print (titanic_reduced.loc[12])



# konverzia pohlavia male/female na 0/1
enc = LabelEncoder()
label_encoder = enc.fit(titanic_reduced["sex"])

#print "Categorical classes:", label_encoder.classes_
integer_classes = label_encoder.transform(label_encoder.classes_)

#print "Integer classes:", integer_classes
titanic_reduced["sex"]= label_encoder.transform(titanic_reduced["sex"])
#titanic_X[:, 2] = t

print( '\nKodovanie kategorickych hodnot \n',)
print ("Passanger data")
print (titanic_reduced.loc[12])

# ONE HOT ENCODING


# First, convert clases to 0-(N-1) integers using label_encoder
label_encoder = enc.fit(titanic_reduced["pclass"])
integer_classes = label_encoder.transform(label_encoder.classes_)
titanic_reduced["pclass"]= label_encoder.transform(titanic_reduced["pclass"])

print( '\nKodovanie kategorickych hodnot \n',)
print ("Passanger data")
print (titanic_reduced.loc[12])

# Second, create a sparse matrix with three columns, each one indicating if the instance belongs to the class 
ohe = OneHotEncoder()

aa= np.array(titanic_reduced["pclass"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(aa)
ohe_coded=ohe.transform(aa).toarray() # zakodovane hodnoty kategorickeho atributu

titanic_reduced = titanic_reduced.drop(columns=["pclass"])  # povodny atribut uz nepotrebujeme, bud enahradeny zakodovanou hodnotou

titanic_reduced["class 1"] = ohe_coded[:,0]   # pridame nove atributy - kodovane
titanic_reduced["class 2"] = ohe_coded[:,1]
titanic_reduced["class 3"] = ohe_coded[:,2]
#new_features = one_hot_encoder.transform(titanic_reduced["pclass"])
print ("\nPassanger data")
print (titanic_reduced.loc[12])

# STARA VERZIA PRE STARSI SCIKIT
#
#import numpy as np
#import csv
#from sklearn.preprocessing import Imputer
#from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import OneHotEncoder
#
#with open('data/titanic.txt', 'rb') as csvfile:
#    titanic_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#    
#    # Header contains feature names
#    row = titanic_reader.next()
#    feature_names = np.array(row)
#    
#    # Load dataset, and target classes
#    titanic_X, titanic_y = [], []
#    for row in titanic_reader:  
#        titanic_X.append(row)
#        titanic_y.append(row[2]) # The target value is "survived"
#    
#    titanic_X = np.array(titanic_X)
#    titanic_y = np.array(titanic_y)
#    
## manualny  vyber uzitocnych priznakov
#
#titanic_X = titanic_X[:, [1, 4, 10]]
#feature_names = feature_names[[1, 4, 10]]
#
#
## imputacia (mozno vykonat aj cez Imputer objekt, je vsak predtym potrebne nahradit 'NA'
## nan typom) -  DOMACA ULOHA
#
#ages = titanic_X[:, 1]
#mean_age = np.mean(titanic_X[ages != 'NA', 1].astype(np.float))
#titanic_X[titanic_X[:, 1] == 'NA', 1] = mean_age
#
#
## konverzia pohlavia male/female na 0/1
#
#enc = LabelEncoder()
#label_encoder = enc.fit(titanic_X[:, 2])
##print "Categorical classes:", label_encoder.classes_
#integer_classes = label_encoder.transform(label_encoder.classes_)
##print "Integer classes:", integer_classes
#t = label_encoder.transform(titanic_X[:, 2])
#titanic_X[:, 2] = t
#
#print titanic_X[12]
#
## one hot encoding triedy listka z kategorickych hodnot na realne
#
## zacneme tym, ze ako v predch pripade text (triedu cestujuceho) prekodujeme na celociselnu hdonotu
#enc = LabelEncoder()
#label_encoder = enc.fit(titanic_X[:, 0])
#print "Categorical classes:", label_encoder.classes_
#integer_classes = label_encoder.transform(label_encoder.classes_).reshape(3, 1)
#print "Integer classes:", integer_classes
#
#
#enc = OneHotEncoder()
#one_hot_encoder = enc.fit(integer_classes)
#
## First, convert clases to 0-(N-1) integers using label_encoder
#num_of_rows = titanic_X.shape[0]
#t = label_encoder.transform(titanic_X[:, 0]).reshape(num_of_rows, 1)
#
## Second, create a sparse matrix with three columns, each one indicating if the instance belongs to the class
#new_features = one_hot_encoder.transform(t)
#
## Add the new features to titanix_X
#titanic_X = np.concatenate([titanic_X, new_features.toarray()], axis = 1)
##Eliminate converted columns
#titanic_X = np.delete(titanic_X, [0], 1)
## Update feature names
#feature_names = ['age', 'sex', 'first_class', 'second_class', 'third_class']
## Convert to numerical values
#titanic_X = titanic_X.astype(float)
#titanic_y = titanic_y.astype(float) 
#
#
#
#print 'One hot encoding atributu triedy \n',
#print titanic_X[12]
#
#
#
#
#
#
#
#
#


























