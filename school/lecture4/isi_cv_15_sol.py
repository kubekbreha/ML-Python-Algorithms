#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:05:06 2017

@author: pd
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

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















