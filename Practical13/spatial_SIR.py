# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:32:43 2020

@author: 10139
"""
# Import some necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Make array of all susceptible population
population = np.zeros((100,100))
# Choose a random point for where the outbreak happens
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]]=1
# Plot the whole map and add one small dot as the outbreak
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
# Set model parameters
beta = 0.3 # The variable beta holds the infection probability.
gamma = 0.05 # The variable gamma holds the recovery probability.
for n in range(1,101):
    # Find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # Get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # Infect each neighbour with probability beta
        # Infect all 8 neighbours 
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # Don't infect yourself! (Is this strictly necessary? YES.)
                if (xNeighbour,yNeighbour) != (x,y):
                    # Make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # Only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0] # Sitmulate that some neighbours are infected.
        population[x,y]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0] # Sitmulate that some infected people are recovered.
    plt.figure(figsize=(6,4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
