# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:02:46 2020

@author: 10139
"""
# Give n a value
n = 56
print ("Primitive number:", n)
# Use a as a count for repeating the following code
a = 0
# Set a goal of ending, n=1
while n!=1:
# Judge whether n is even or not
    if n%2 == 0:
        n = n/2
    else:
        n = n*3+1
# Record the count
    a = a + 1
# Print the outcome spontaneously
    print ("Round", a, ":", n)
    