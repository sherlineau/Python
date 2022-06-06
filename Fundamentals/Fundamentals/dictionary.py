"""
dictionary = object
{
    name: "Alex"
}
"""

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