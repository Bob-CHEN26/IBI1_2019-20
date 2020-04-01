# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:50:13 2020

@author: 10139
"""

# Read the file called saccharomyces_cerevisiae.R64-1-1.cdna.all.fa
file = open ('saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
# Input a filename as the new fasta file
file_name = input ('The filename of new fasta file is: ')
# Extract mitochondria sequences
data = {} # A dictionary storing the extracted mitochondria sequences 
initialdata = '' # A temporary string storing a mitochondria sequence
sign = False # Test whether it needs to add the new line
n = 0 # Count the number of mitochondria sequences
# Find mitochondria sequences
for line in file:
    line  = line.rstrip()
    if not 'mRNA cdna chromosome:R64-1-1:Mito' in line:
        if sign == False:
            continue
        else:
            if '>' in line: # Find the end of a mitochondria sequence
                sign = False # Indicate to stop storing a mitochondria sequence
                data[str(n)] = initialdata # Store a complete sequence in a dictionary called data
                initialdata = '' 
                continue
    else: 
        sign = True # Indicate to start storing a mitochondria sequence
        n = n + 1
    initialdata = initialdata + line # Store a mitochondria sequence in a temporary string
import re
gene_name = '' # A temporary string storing a gene name
length = 0 # A temporary numeric datum storing the length of a mitochondria sequence
sseq = '' # A temporary string storing a sequence to be simplified
start = 0 #  A temporary numeric datum storing the index of the start point of a mitochondria sequence
sequence = ''# A temporary string storing a mitochondria sequence
for i in range(1, n+1):
    sseq = data[str(i)][:]
# Find the gene name
    gene_name = re.search (r'gene:(\w+)', sseq)
    gene_name = gene_name.group(1)
# Find the sequence length
    for j in range(0, len(sseq)):
        if sseq[j] == ']':
            start = j + 1 
    length = len(sseq) - start
# Find the mitochondria sequence
    for k in range(start, len(sseq)):
        sequence = sequence + sseq[k]
    DNA_reverse = sequence[:]
    DNA_reverse = DNA_reverse[::-1] #reverse the sequence
    cDNA = ''
# Interconvert A and T, C and G
    for m in DNA_reverse:
        if m == 'A':
            cDNA = cDNA + 'T'
        elif m == 'T':
            cDNA = cDNA + 'A'
        elif m == 'C':
            cDNA = cDNA + 'G'
        elif m == 'G':
            cDNA = cDNA + 'C'
    data[str(i)] = '>Gene: ' + gene_name +'  Length: '+ str(length) + 'bp' + '\n' + cDNA
# Refresh the temporary data
    gene_name = ''
    sseq = ''
    sequence = ''
    start = 0
    length = 0
# Output a new fasta file
fasta = open (file_name, 'w')
for i in range(1, n+1):
    line = data[str(i)]
    fasta.write(line + '\n')
    line = ''
fasta.close()
# Print the outcome
fasta = open ('mito_gene_RC.fa', 'r')
for line in fasta:
    print (line[:-1])