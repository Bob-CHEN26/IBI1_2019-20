# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:52:36 2020

@author: 10139
"""

# Read the file called saccharomyces_cerevisiae.R64-1-1.cdna.all.fa
file = open ('saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
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
    data[str(i)] ='>Gene: ' + gene_name +'  Length: '+ str(length) + 'bp' + '\n' + sequence
# Refresh the temporary data
    gene_name = ''
    sseq = ''
    sequence = ''
    start = 0
    length = 0
# Output a new fasta file
fasta = open ('mito_gene.fa', 'w')
for i in range(1, n+1):
    line = data[str(i)]
    fasta.write(line + '\n')
    line = ''
fasta.close()
# Print the outcome
fasta = open ('mito_gene.fa', 'r')
for line in fasta:
    print (line[:-1])
    