# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:43:27 2020

@author: 10139
"""

seq = 'ATGCGACTACGATCGAGGGCCAT' #Input a sequence
DNA_reverse = seq[:]
DNA_reverse = DNA_reverse[::-1] #reverse the sequence
cDNA = ''
# Interconvert A and T, C and G
for n in DNA_reverse:
    if n == 'A':
        cDNA = cDNA + 'T'
    elif n == 'T':
        cDNA = cDNA + 'A'
    elif n == 'C':
        cDNA = cDNA + 'G'
    elif n == 'G':
        cDNA = cDNA + 'C'
# Print the outcome
print ('The complementary DNA strand is', cDNA, '.')