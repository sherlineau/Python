"""
JS
for (var i = 0; i < 10; i++) { for ( variable & start, end, increment)
    //code
}
"""

for x in range (10): #loops 10 times, if you want to increment by something other than 1 you need to include start as well (0 , 10, 2)
    print(x)

# for x in range(0, 10):  #default incremement is 1
#     print(x)            

# #to DECREASE
# for x in range( 10, 0, -1): #for variable in range ( start, end, increment )
#     print(x)

#looping through lists/arrays
numbers = [10,20,30,40,50]

for i in range( 0, len(numbers) ): 
    print(numbers[i])         #this prints the index of numbers

for num in numbers:           #does the same as above
    print(num)


# looping through a string
name = "Alexander"

for letter in name:
    print (letter)

print ("First letter", name[0])


#looping through a dictionary/object
student = {
    "first_name" : "Alex",   #keys also need to be in quotations ""
    "last_name" : "Miller",
    "age" : 25,
    "languages" : ["JavaScript" , "Python"]

}

for key in student:
    print(key, student[key])   #key prints out the key and student[key] prints out the value

for language in student["languages"]:
    print(language)

#while loops
i = 0
while i< len(numbers):
    print(numbers[i])
    i+= 1               #remember to increment
    