"""
dictionary = object
{
    name: "Alex"
}
"""

from ast import Delete
from turtle import st


student = {
    "first_name" : "Alex",   #keys also need to be in quotations ""
    "last_name" : "Miller",
    "age" : 25
}

key = "last_name"
print( student["first_name"] )
print( student[key] )

# if key does not exist, KeyError will occur
# l_n = "s"
# print (student[l_n])

students = [ 
    {
    "first_name" : "Alex",   #index 0
    "last_name" : "Miller",
    "age" : 25,
    "languages" : ["JavaScript" , "Python"]
},
{
    "first_name" : "Martha",  #index 1
    "last_name" : "Miller",
    "age" : 22
}]

print ( students[1]["first_name"], students[1][key])

print( students[0]["first_name"], students[0]["languages"][1])
#          Alex                                  Python

#creating a dictionary
capitals =  {} #create empty dictionary
capitals["svk"] = "Bratislava" #key "svk" created and value is set to Bratislava
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print(capitals)

#how to remove values
#1. pop
value_removed = capitals.pop('svk') #removes the key and returns its value
print(capitals)

#2. Delete
del capitals['dnk']
print(capitals)

"""Nested dictionary"""

context = {
    'questions': [ # context [key]
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}