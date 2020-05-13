# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:41:05 2020

@author: 10139
"""
# Import some python libraries
import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Input full_data.csv
os.chdir("/Users/10139/Desktop/IBI 1/Week 4. Version control and web authoring tools/Practical 4 Getting started with Git and GitHub/GitKraken/IBI1_2019-20/IBI1_2019-20/Practical7")
print ('Task1:\nWorking dictionary:\n', os.getcwd(), '\n')
print ('List files in the working dictionary:', os.listdir(), '\n')
covid_data = pd.read_csv('full_data.csv')
# Use head command
print ('The outcome of "covid_data.head(5)":\n', covid_data.head(16), '\n') # The number 16 indicates the number of rows with data is sixteen.
# Use info command
print ('The outcome of "covid_data.info()":')
covid_data.info() # Data points are integer. Columns: data, location, new_cases, new_deaths, total_cases, total_deaths. There are 7996 rows with data (one is the names of the columns).  
# Use describe command
print ('\nThe outcome of "covid_data.describe()":\n', covid_data.describe(), '\n') # The mean of new cases is 194.546773, the median of new cases is 0.
# Use iloc & loc command
print ('Task2:\n',covid_data.iloc[0:15:3,:])
# Use a Boolean to show “total cases” for all rows corresponding to Afghanistan. 
Boolean_sequence = []
for i in range(0, 7996):
    if str(covid_data.iloc[i, 1]) == 'Afghanistan':
        Boolean_sequence.append (True)
    else:
        Boolean_sequence.append (False)
        break
for n in range(i+1, 7996):
    Boolean_sequence.append (False)
print ('\nTask3:\n', covid_data.loc[Boolean_sequence, 'total_cases'])
# Input world_new_cases.csv
world_data = pd.read_csv ('world_new_cases.csv')
# Calculate the mean and median for new cases around the world
mean = np.mean(world_data.iloc[:,2])
median = np.median(world_data.iloc[:,2])
print ('\nTask4:\nThe mean for new cases around the world is:', mean, '.')
print ('The median for new cases around the world is:', median, '.')
# Create a box plot
print ('\nTask5:')
plt.boxplot(world_data.iloc[:, 2],
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False
            )
plt.show()
# Create a graph
print ('\nTask6:')
plt.plot (world_data.iloc[:, 0], world_data.iloc[:, 2], 'b+')
plt.plot (world_data.iloc[:, 0], world_data.iloc[:, 3], 'r+')
plt.xlabel ('Date')
plt.xticks (world_data.iloc[0:len(world_data):4, 0], rotation = -90)
plt.ylabel ('Number')
plt.show()
print ('Blue points represent new cases.\nRed points represent new deaths.')
# Ask one question
quest = open('question.txt', 'w')
quest.write ('Question: Are there places in the World where have not yet been more than 10 total infections (as of 31 March)? If so, where are they?\n')
quest.write ('Line number: 69.\n')
# The codes to answer the question
places = 'The places in the world where there have not yet been more than 10 total infections (as of 31 March) are\n' 
n = 0
for i in range(0,7996):
    if str(covid_data.iloc[i, 0]) == '2020-03-31':
        if int(str(covid_data.iloc[i, 4])) <= 10:
            n = n + 1
            places = places + str(n) + ':' + str(covid_data.iloc[i, 1]) + '  '
places = places + '\nThere are ' + str(n) + ' eligible places.'
print ('\nTask7:\n', places)
quest.write (places)
quest.close()
            