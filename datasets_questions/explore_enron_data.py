#!/usr/bin/python
# coding=utf-8

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
print len(enron_data)
len(enron_data.keys())

# For each person, how many features are available?
len(enron_data.values()[0])
enron_data[enron_data.keys()[0]]
len(enron_data['SKILLING JEFFREY K'])

# How many POIs are there in the E+F dataset
# Example 1:
count = 0
for i in range(len(enron_data)):
    a = enron_data.values()
    if a[i]['poi'] == True:
        count = count + 1
print count

# How Many POIs Exist?
poi_text = '../final_project/poi_names.txt'
poi_names = open(poi_text, 'r')
fr = poi_names.readlines()
print len(fr[2:])
poi_names.close()

# What is the total value of the stock belonging to James Prentice?
print enron_data['PRENTICE JAMES']['total_stock_value']

# How many email messages do we have from Wesley Colwell to persons of interest?
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# Whats the value of stock options exercised by Jeffrey K Skilling?
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


# Sort values
sorted(enron_data.keys())

# How much money did that person get?
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']

# How is an unfilled feature denoted?
print enron_data['FASTOW ANDREW S']['deferral_payments']


# How many folks in this dataset have a quantified salary?
# What about a known email address?
count_salary = 0
count_email = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        count_salary+=1
    if enron_data[key]['email_address'] != 'NaN':
        count_email+=1
print count_salary
print count_email


# How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
# What percentage of people in the dataset as a whole is this?
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        count_NaN_tp+=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())

# How many POIs in the E+F dataset have “NaN” for their total payments?
# What percentage of POI’s as a whole is this?
count_NaN_tp = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == True :
        print
        count_NaN_tp+=1
print count_NaN_tp
print float(count_NaN_tp)/len(enron_data.keys())
