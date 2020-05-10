# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:51:58 2020

@author: 10139
"""

import itertools
import fractions
import sys

x=input('''Please input numbers to compute 24 (use ',' to devide them): ''') # Imput the numbers
numbers=x.split(',')
numbers_int = [int(x) for x in numbers]
numbers_int.sort() # List the inputted numbers in an ascending order
N=len(numbers_int)

def compute(m,n): 
    '''
    Compute with an operation of +,-,*,/
    If one of numbers is 0, it will not be divided.
    '''
    if m!=0 and n!=0:
        z=[m+n,n-m,m*n,fractions.Fraction(m,n),fractions.Fraction(n,m)] # The outcome of fractions.Fraction(m,n) is m/n, as a fraction form.
    if m==0 and n!=0:
        z=[m+n,n-m,m*n,fractions.Fraction(m,n)]
    if m!=0 and n==0:
        z=[m+n,n-m,m*n,fractions.Fraction(n,m)]
    if m==0 and n==0:
        z=[m+n,n-m,m*n]
    return z

def enumeration(i):
    '''
    For a given order of numbers, all possible operations are performed
    Operation results are stored in 'y'
    '''
    sequence = list(all_sequence[i]) # Convert tuple into list
    y = compute(sequence[0],sequence[1])
    del sequence[0:2] # Delete the two numbers used in the 'compute' function
    while sequence!=[]: # Repeat it until every number in 'sequence' is deleted (used in the 'computed' function.)
        y_copy = y # Store a copy of y 
        y=[]
        for j in y_copy:
            y += compute(j,sequence[0]) # Store the new results of y
        del sequence[0] # Delete the number in 'sequence' used in the 'compute' function
    return y

for i in range(0, N):
    if (int(numbers_int[i])>=1 and int(numbers_int[i])<=23) == False: #Examine whether the inputted numbers are 1~23.
        print('\nThe input number must be integers from 1 to 23\n')
        sys.exit()    
        
list1_time = 0
recursion_time = 0
for i in range(N, 1, -1):        
    all_sequence = list(itertools.permutations(numbers_int, i)) #Permutation of inputted numbers, note that each time we use i(2~N) numbers of the whole inputted numbers
    list1 = []
    for i in range(0, len(all_sequence)): #repeat 'enumeration' for every possible order of inputted numbers
        list1 += enumeration(i)
        list1_time = len(list1) # The exact recursion time in this for-loop 
        if 24 in list1: # When the right outcome 24 is found, exit the program and output the exact recursion time.
            print('\nYes')
            print('recursion times: '+ str(recursion_time + list1_time) + '\n') # The exact recursion time = recursion time of last for-loop + the exact list1_time
            sys.exit()
        recursion_time += len(list1) # Record the exact whole recursion time 
print('No\nrecursion times: '+ str(recursion_time)) # When there is no outcome of 24, output the failed message. 
