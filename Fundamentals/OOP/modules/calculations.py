# imported modules need to be in the same directory / folder
from modules import arithmetic
import random
print(arithmetic.add(5,8))
print(arithmetic.subctract(10,5))
print(arithmetic.multiply(12,6))

randomint = random.randint(0,12)
print(randomint)