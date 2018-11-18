#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import tree

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

print ("\nPassanger data")
print (titanic_reduced.loc[12])

X_train, X_test, y_train, y_test = train_test_split(titanic_reduced, titanic_y, test_size=0.25, random_state=33)

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3,min_samples_leaf=5)
clf = clf.fit(X_train,y_train)

# porovnat aj s trenovacimi
y_pred=clf.predict(X_train)
print( "\nPresnost trenovacie")
print (metrics.accuracy_score(y_train,y_pred),"\n")

# presnost testovacie data
y_pred_test=clf.predict(X_test)
print ("\nPresnost testovacie")
print (metrics.accuracy_score(y_test,y_pred_test),"\n")










