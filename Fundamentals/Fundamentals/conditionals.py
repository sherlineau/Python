""" 
* / %
+ -
<  >  >=  <=  !=  ==
and
or
not
=
++ increment does not exist in python 
"""
num = 10

if num == 10 or num==20:              #condition ends with colon
    print("It is a 10")               #indents are important!!
    print("This is inside the if")
elif num < 10:                        #else if
    print("It is less than 10")
else: 
    print("It is greater than 10")

print("This is always printed")