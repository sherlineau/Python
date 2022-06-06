#functions are declared using def 

def add(a,b):	# function name: 'add', parameters: a and b 
    x = a + b	# process
    return x	# return value: x

#call function
new_val = add(3,4)
print(new_val)

print(add(1,4))

def say_hi(name):
    return "Hi " + name

greeting = say_hi('Michael')  #assigns return of function to greeting
print(greeting)

def add_two_numbers ( num1, num2):
    total = num1 + num2
    return total

x = 20
y = 30
result = add_two_numbers( x, y )

def print_grades( grade1 = 0.0, grade2 = 0.0 , grade3 = 0.0): #default parameters are set to 0.0, if nothing is sent to grade3 it will be set to 0.0 by default instead of getting an error
    print("Grade 1 ", grade1)
    print("Grade 2 ", grade2)
    print("Grade 3 ", grade3)

print_grades( 9.2 , 9.3 )
print_grades() #function still runs and prints with default values

# parameters are DEFINED when creating function
# arguments are sent INTO the function
# named agruments
print_grades(grade2 = 9.2)

#passing in a list
def some_function ( list ):
    print( list )
    total = 0
    for element in list:
        total += element
    return total

nums = [1,2,3,4,5,6,7,8,9,10]
total = some_function( nums )
print( "Expecting a 55", f"Got a {total}")