# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 08:46:01 2020

@author: 10139
"""
# Step 1: Input files
# Read the .fa files 
human = open ('SOD2_human.fa', 'r')
mouse = open ('SOD2_mouse.fa', 'r')
random = open ('RandomSeq.fa', 'r')
# Extract the amino acid sequences
sign = False
seq_human = ''
seq_mouse = ''
seq_random = ''
for line in human: # Extract human's sequence
    line  = line.rstrip()
    if sign == True:
        seq_human += line
    if line.startswith ('>'):
        sign = True
sign = False
for line in mouse: # Extract mice's sequence
    line  = line.rstrip()
    if sign == True:
        seq_mouse += line
    if line.startswith ('>'):
        sign = True
sign = False
for line in random: # Extract a random sequence
    line  = line.rstrip()
    if sign == True:
        seq_random += line
    if line.startswith ('>'):
        sign = True
# Read BLOSUM62 matrix
import pandas as pd
matrix = pd.read_csv('BLOSUM62.csv')

# Step 2: Compare each amino acid
# Compare SOD2_human with SOD2_mouse
row_name = 'ARNDCQEGHILKMFPSTWYVBZX*'
edit_distance1 = 0
alignment1 = ''
score1 = 0
for i in range (len(seq_human)):
    row = 0
    column = 1
    for j in row_name:
        if j == seq_human[i]:
            break
        else:
            row = row + 1
    if row == 25:
        row = 24
    for j in row_name:
        if j == seq_mouse[i]:
            break
        else:
            column += 1   # Find the location of the specific BLOSUM score  
    if seq_human[i] != seq_mouse[i]:
        edit_distance1 += 1  # Calculate the Hamming/edit distance
        if int(matrix.iloc[row, column]) >= 0:
            alignment1 += '+'
        else:
            alignment1 += ' '
    else:
        alignment1 += seq_human[i]   # Record the alignment
    score1 += int(matrix.iloc[row, column])  # Calculate the sum of BLOSUM score    
# Compare SOD2_human with RandomSeq
edit_distance2 = 0
alignment2 = ''
score2 = 0
for i in range (len(seq_human)):
    row = 0
    column = 1
    for j in row_name:
        if j == seq_human[i]:
            break
        else:
            row = row + 1
    if row == 25:
        row = 24
    for j in row_name:
        if j == seq_random[i]:
            break
        else:
            column += 1      # Find the location of the specific BLOSUM score  
    if seq_human[i] != seq_random[i]:
        edit_distance2 += 1  # Calculate the Hamming/edit distance
        if int(matrix.iloc[row, column]) >= 0:
            alignment2 += '+'
        else:
            alignment2 += ' '
    else:
        alignment2 += seq_human[i]    # Record the alignment
    score2 += int(matrix.iloc[row, column])  # Calculate the sum of BLOSUM score   
# Compare RandomSeq with SOD2_mouse
edit_distance3 = 0
alignment3 = ''
score3 = 0
for i in range (len(seq_random)):
    row = 0
    column = 1
    for j in row_name:
        if j == seq_random[i]:
            break
        else:
            row = row + 1
    if row == 25:
        row = 24
    for j in row_name:
        if j == seq_mouse[i]:
            break
        else:
            column += 1    # Find the location of the specific BLOSUM score  
    if seq_random[i] != seq_mouse[i]:
        edit_distance3 += 1  # Calculate the Hamming/edit distance
        if int(matrix.iloc[row, column]) >= 0:
            alignment3 += '+'
        else:
            alignment3 += ' '
    else:
        alignment3 += seq_random[i]  # Record the alignment
    score3 += int(matrix.iloc[row, column]) # Calculate the sum of BLOSUM score
# Step 3: Print output
print ('A comparsion between SOD2_human and SOD2_mouse\nSOD2_human(NP_000627.2):\n',seq_human, '\n\nAlignment:\n', alignment1, '\n\nSOD_mouse(NP_038699.2):\n',seq_mouse, '\n\nThe final BLOSUM score is', str(score1), '.\n', 'The Hamming/edit distance is', str(edit_distance1), ', so the similarity of them is', str(100-edit_distance1/len(seq_human)*100), '%.\n' )
print ('A comparsion between SOD2_human and RandomSeq\nSOD2_human(NP_000627.2):\n',seq_human, '\n\nAlignment:\n', alignment2, '\n\nRandomSeq:\n',seq_random, '\n\nThe final BLOSUM score is', str(score2), '.\n', 'The Hamming/edit distance is', str(edit_distance2), ', so the similarity of them is', str(100-edit_distance2/len(seq_human)*100), '%.\n' )
print ('A comparsion between RandomSeq and SOD2_mouse\nRandomSeq:\n',seq_random, '\n\nAlignment:\n', alignment3, '\n\nSOD_mouse(NP_038699.2):\n',seq_mouse, '\n\nThe final BLOSUM score is', str(score3), '.\n', 'The Hamming/edit distance is', str(edit_distance3), ', so the similarity of them is', str(100-edit_distance3/len(seq_random)*100), '%.\n' )


