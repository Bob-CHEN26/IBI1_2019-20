# What does this piece of code do?
# Answer: Find a random prime number ranging 1 to 100.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
# Assume n is a prime number
    p=True
    n = randint(1,100)
    u = ceil(n**(0.5))
# Judge whether n can be divided exactly by other numbers [2,n^0.5) except itself and 1.
    for i in range(2,u+1):
# When n is not a prime number:
        if n%i == 0:
            p=False


     
print(n)
