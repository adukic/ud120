#!/usr/bin/python

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

print "data points:", len(enron_data)
print "SKILLING JEFFREY K:", enron_data["SKILLING JEFFREY K"]
print "features:", len(enron_data["SKILLING JEFFREY K"])

counts_poi=0
for key, d in enron_data.iteritems():
   if d['poi'] == True:
        counts_poi += 1

print "POIs: ", counts_poi

print "PRENTICE JAMES[total_stock_value]:", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "COLWELL WESLEY[from_this_person_to_poi]:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "SKILLING JEFFREY K[exercised_stock_options]:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "SKILLING JEFFREY K:", enron_data["SKILLING JEFFREY K"]
print "LAY KENNETH L:", enron_data["LAY KENNETH L"]
print "FASTOW ANDREW S:", enron_data["FASTOW ANDREW S"]
print "SKILLING JEFFREY K[total_payments]:", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "LAY KENNETH L[total_payments]:", enron_data["LAY KENNETH L"]["total_payments"]
print "FASTOW ANDREW S[total_payments]:", enron_data["FASTOW ANDREW S"]["total_payments"]

salary=0
email=0
for key, d in enron_data.iteritems():
    if d['salary'] != 'NaN':
        salary += 1
    if d['email_address'] != 'NaN':
        email += 1

print "salary:", salary
print "email:", email

pois=0
total_payments=0
for key, d in enron_data.iteritems():
    if d['poi'] == True:
        pois += 1
        if d['total_payments'] == 'NaN':
            total_payments += 1

print "pois:", pois
print "total_payments:", total_payments

print total_payments*100.0 / len(enron_data)