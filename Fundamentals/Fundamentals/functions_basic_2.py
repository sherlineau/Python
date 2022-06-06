# 1. Countdown
def countdown(list):
    for element in list:
        print(element)

nums = [5,4,3,2,1,0]
countdown(nums)

# 2. Print and Return
def print_and_return(a,b):
    print(a)
    return b

c= print_and_return(5,1)
print(c)

#3. First Plus Length
def first_plus_length(list):
    sum = list[0] + len(list) 
    return sum

print(first_plus_length(nums))

#4 Values greater than second
def greater_than_second(list):
    new_list = []
    if len(list) < 2:
        return False
    else:
        for i in range(0,len(list)):
            if list[i] > list[1]:
                new_list.append(list[i])
        print(len(new_list))
        return new_list
        
numbers = [5,3,2,5,7,8]
output = greater_than_second(numbers)
print(f"There are {len(output)} numbers that are greater than {numbers[1]}\nThose numbers are: ", output)

#5 This Length, That Value
def length_and_value(x, y):
    list_length_value = []
    for i in range(x):
        list_length_value.append(y)
    return list_length_value

output = length_and_value(4,5)
print(output)