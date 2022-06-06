"""
JS - Data types
number
boolean true/false
string
null
undefined

"""

# floats and integers are considered different data types in python
grade = 8.8  #this is a float 
age = 25 #this is an integer

# Print console in JS is console.log("message");
print ( age ) 
print (type(age))   #type() returns the data type of the variable
print (type(grade))

#python true/false needs to be capital True/False
flag = True
print ( flag )

#snake case naming convention is the standard for python
first_name = "Michael"

print(first_name)

# to store empty value in python = None ,  js null = None
middle_name = None

#Arrays in python are called Lists
numbers = [ 10, 20, 30, 40, 50 ] 
#not good practice to change types of arrays to another num -> string, just declare a new variable

print (numbers)
print ("value at index 1 is:", numbers[1])

#array length numbers.length
print( "Length of numbers:", len(numbers) ) #comma, does not coconate prints string and then prints numbers right after in the same line
print( "Length of numbers:" + str(len(numbers))) #casts length of numbers as a str string
print( f"Length of numbers: \n{len(numbers)}") #FORMAT -> f in front ,variable in curly brackets as part of string  \n = new line

#tuples -> same as array but values CANNOT be changed
numbers_tuple = ( 10,20,30,40,50 )
print( numbers_tuple )

"""
numbers_tuple[0] = 15 # error will occur because tuples cannot be changed
PUSH/append  POP WILL NOT WORK EITHER

"""
numbers.append(60)
print(numbers)
numbers.pop(3) #pop index 3
print(numbers)

