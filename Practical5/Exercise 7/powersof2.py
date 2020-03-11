# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:32:44 2020

@author: 10139
"""
# Get the function ceil
from math import ceil

# Give x is a value
x=1750
# Add a string variable
s=str(x)+" is "
# Find n which makes 2^n is closest number to x and smaller than x.
for n in range (0, ceil(x**0.5)+1) :
    if (2**n < x)==True and (2**(n+1) > x)==True:
        break
# The primitive number minus 2^n, write the string
x=x-2**n
s=s+"2**"+str(n)
# Find the sum of powers of 2
while x!=0 and n>0:
    n=n-1
    if (2**n < x)==True:
       x=x-2**n
       s=s+" +2**"+str(n)
# Print the outcome
print (s)       
    
    