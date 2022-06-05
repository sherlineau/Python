#variable declaration
num1 = 42  #numbers
num2 = 2.3  #numbers
boolean = True  #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #array of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #object person
fruit = ('blueberry', 'strawberry', 'banana')


print(type(fruit)) #type check
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #add value to toppings
print(person['name']) #logs value in person with key name
person['name'] = 'George' #changes person key name's value to "George"
person['eye_color'] = 'blue' #changes key eye_color's value to "blue"
print(fruit[2]) #logs value in fruit with index of 2 -> bananas

if num1 > 45: #conditional statement
    print("It's greater") #prints it's greater if num1 is greater than 45
else:
    print("It's lower") #prints its lower if num1 is not greater than 45

if len(string) < 5:   #len gets the length of string
    print("It's a short word!") #conditional prints it's a short word if string length is less than 5
elif len(string) > 15:
    print("It's a long word!")  #conditional prints it's a long word if string length is greater than 15
else:
    print("Just right!") # conditional prints just right! if string length is between 6-14 strings

for x in range(5): #runs for 5 iterations
    print(x)
for x in range(2,5): #starts at 2, ends at 5
    print(x)
for x in range(2,10,3): #starts at 2, ends at 10, increments by 3
    print(x)
x = 0
while(x < 5): #runs while x is less than 5
    print(x)  #logs x
    x += 1    #incrememnts x by 1

pizza_toppings.pop() #removes last index Olives
pizza_toppings.pop(1) #removes value at index 1 Sausage

print(person) #prints {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
person.pop('eye_color') #prints value -> 'blue'
print(person) #prints {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: #NameError: name 'pizza_toppings' is not defined
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():  #defines function
    for num in range(10):
        print('Hello')

print_hello_ten_times()  #calls function

def print_hello_x_times(x):  #x = parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #(4) is argument that is passed into function

def print_hello_x_or_ten_times(x = 10):  #function prints hello with parameter input x
    for num in range(x):                  #loop x = iteratations    
        print('Hello')                    # print hello ^ number of times

print_hello_x_or_ten_times()              # x = 10 at default so prints hello 10 times
print_hello_x_or_ten_times(4)             # argument 4 passed into function -> prints hello four times


"""
Bonus section
"""

# print(num3) #NameError: name 'num3' is not defined because this is called above the variable declaration
# num3 = 72 #variable declaration
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment 
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean) unexpected indent
# fruit.append('raspberry')  AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  AttributeError: 'tuple' object has no attribute 'pop'