lt# -*- coding: utf-8 -*-
"""
Created on Wed May 13 08:46:13 2020

@author: 10139
"""
# Import some necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
 
def vaccination(r):
    N = 10000 # The variable N holds the total number of people in the population.
    IP = 1 # The variable IP holds the total number of infected people in the population.
    VP = int(r/10*N) # The variable VP holds the total number of vaccinated people in the population.
    if r!=10:
        SP = N-IP-VP # The variable SP holds the total number of susceptible people in the population.
    else:
        SP = 0 # When 100% people are vaccinated, all of them have immunity to the disease.
    RP = 0 # The variable RP holds the total number of recovered people in the population.
    beta = 0.3 # The variable beta holds the infection probability.
    gamma = 0.05 # The variable gamma holds the recovery probability.
    IP_list = [IP] # Create an array for IP
    # Calculate new values of variables
    for i in range(1,1001):
        infection_probability = beta*IP/N  # Calculate the infection probability.
        # Store the current situation of infected people and recovered people in two arrays.
        IP_current = np.random.choice(range(2),SP,p=[1-infection_probability,infection_probability])
        RP_current = np.random.choice(range(2),IP,p=[1-gamma,gamma])
        for n in IP_current:
            if n == 1:
                IP += 1
        for n in RP_current:
            if n == 1:
                RP += 1
                IP -= 1
        SP = N-IP-RP-VP
        if SP<0: # When r=10, SP could be smaller than 0.
            SP = 0
        # Store new values of variables in three arrays.
        IP_list.append(IP)
    return IP_list

# Create a graph
time = [] # Store the data of x axis.
timescale=np.arange(0,1001)
for i in range(0,1001,200):
    time.append(i)
for r in range(0,11):
    plt.plot (timescale, vaccination(r), label=str(r*10)+'%', color=cm.viridis(30*r))
    plt.xlabel ('time')
    plt.ylabel ('number of people')
    plt.legend ()
    plt.title ('SIR model with different vaccination rates')
    plt.xticks (time)
plt.rcParams['savefig.dpi'] = 3000
plt.savefig('SIR_vaccination_figure.png')
plt.show()
