for x in range(151):
    print(x)

for x in range(5,1001):
    if( x % 5 == 0 ):
        print(x)

for x in range(1,101):
    if ( x % 10 == 0):
        print('Coding Dojo')
    elif ( x % 5 == 0):
        print('Coding')
    else:
        print(x)

sum = 0
x = 0
while ( x < 500000):
    sum = sum + x
    x+=1

print(sum)

for x in range (2018,0,-4):
    print(x)

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum,highNum+1):
    if (x % mult == 0 ):
        print(x)