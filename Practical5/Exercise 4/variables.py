# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:42:45 2020

@author: 10139
"""
# 4.1 Some simple math
a = 123
b = 123123
print (b%7)
c = b/7
d = c/11
e = d/13
print ("a is", a, "and e is", e, ".")
print ("Is a greater than e?", a>e)

# 4.2 Booleans
X = True
Y = False
if X == True and Y == False:
    Z = True
elif X == False and Y == True:
    Z = True
else:
    Z = False

W = (X!=Y)
print ("W is", W, "and Z is", Z)
print ("Is W same as Z?", W==Z)

