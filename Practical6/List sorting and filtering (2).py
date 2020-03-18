# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:43:50 2020

@author: 10139
"""

#Input a list of 10 values
gene_lengths=[int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input()),int(input())]
#Sort values
gene_lengths.sort()
print ('The list of sorted values is', gene_lengths)
#Remove the longest and shortest gene lengths removed
del(gene_lengths[0])
del(gene_lengths[len(gene_lengths)-1])
print ('Th revised list of sorted values is', gene_lengths)
#Construct a boxplot
import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(gene_lengths,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False,
            boxprops = {'color':'orangered','facecolor':'yellow'}
            )
plt.title('boxplot of gene lengths')
plt.show()
