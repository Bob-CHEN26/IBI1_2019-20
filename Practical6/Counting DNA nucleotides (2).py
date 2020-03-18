# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:00:13 2020

@author: 10139
"""

#Input the DNA string
s = input('')
#Set up a dictionary
nucleotides = {'A':0, 'C':0, 'G':0, 'T':0}
#Extract each value of the DNA string and revise the counting data of the specific letter
for i in s:
    if i == 'A':
        nucleotides['A'] += 1
    elif i == 'C':
        nucleotides['C'] += 1
    elif i == 'G':
        nucleotides['G'] += 1
    elif i == 'T':
        nucleotides['T'] += 1
    else:
        print ('The DNA string exists some errors.')
        exit
print ('The DNA string(', s, ')has', nucleotides['A'], 'A,', nucleotides['C'], 'C,', nucleotides['G'], 'G,', nucleotides['T'], 'T.')
#Construct a pie
import matplotlib.pyplot as plt
labels = 'A', 'C', 'G', 'T'
sizes = [nucleotides['A'], nucleotides['C'],nucleotides['G'], nucleotides['T']]
colors = ['violet', 'ivory', 'orange', 'red']
explode = (0, 0.2, 0, 0)
plt.pie(sizes, explode=explode, colors=colors, labels=labels, autopct='%1.1f%%', shadow=True, startangle=100)
plt.axis('equal')
plt.title('pie of the four DNA nucleotides')
plt.show()