# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:19:42 2019

@author: 王梓洋
"""

import numpy as np
import matplotlib.pyplot as plt
population = np.zeros((100,100)) #100x100 suscepticle population (=0)
beta = 0.3
gamma = 0.05
time = 0 
outbreak = np.random.choice(range(100),2) #select random person
population[outbreak[0],outbreak[1]] = 1 #that person got infected 

plt.figure(figsize=(6,4),dpi=150) #plot the "time=0" situation.
plt.imshow(population,cmap='viridis',interpolation='nearest')

while time <= 99:        
    infectedIndex = np.where(population==1) #locate the infected
    for i in range(len(infectedIndex[0])): 
        x = infectedIndex[0][i]
        y = infectedIndex[1][i] 
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y): 
                    if xNeighbour not in [-1,100] and yNeighbour not in [-1,100]: #not fall off an edge
                        if population[xNeighbour,yNeighbour] == 0: # b probability the suscepticle infected (=1)
                            population[xNeighbour,yNeighbour] = np.random.choice(range(2),1,p=[1-beta,beta])[0]
                else: #for himself, g probability he recovered (=2)
                    population[xNeighbour,yNeighbour] = np.random.choice(range(2),1,p=[1-gamma,gamma])[0] + 1

    time = time + 1
    
    #plot heat map after 10,50,100 recursions
    if time==10 or time==50 or time==100:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
    
