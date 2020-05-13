# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:07:58 2020

@author: 10139
"""
# Import some necessary libraries
import numpy as np
import matplotlib.pyplot as plt

N = 10000 # The variable N holds the total number of people in the population.
IP = 1 # The variable IP holds the total number of infected people in the population.
SP = N-IP # The variable SP holds the total number of susceptible people in the population.
RP = 0 # The variable RP holds the total number of recovered people in the population.
beta = 0.3 # The variable beta holds the infection probability.
gamma = 0.05 # The variable gamma holds the recovery probability.
# Create arrays for each of variables
IP_list = [IP]
SP_list = [SP]
RP_list = [RP]
# Calculate new values of variables
for i in range(1,1001):
    infection_probability = beta*IP/N  # Calculate the infection probability.
    # Store the current situation of infected people and recovered people in two arrays.
    IP_current = np.random.choice([0,1],SP,p=[1-infection_probability,infection_probability])
    RP_current = np.random.choice([0,1],IP,p=[1-gamma,gamma])
    for n in IP_current:
        if n == 1:
            IP += 1
    for n in RP_current:
        if n == 1:
            RP += 1
            IP -= 1
    SP = N-IP-RP
    # Store new values of variables in three arrays.
    IP_list.append(IP)
    SP_list.append(SP)
    RP_list.append(RP)
# Create a graph
time = []
for i in range(0,1001,200):
    time.append(i)
plt.plot (IP_list,'b')
plt.plot (SP_list,'r')
plt.plot (RP_list,'g')
plt.title ('SIR model')
plt.xlabel ('time')
plt.xticks (time)
plt.ylabel ('number of people')
plt.legend (('infected','susceptible','recovered'))
plt.rcParams['savefig.dpi'] = 3000
plt.savefig('SIR_figure.png')
plt.show()