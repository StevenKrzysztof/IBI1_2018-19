# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:09:28 2019

@author: 王梓洋
"""

#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

#some definitions
population = 10000
N = population
susceptible = N-1
recovered=0
recordI=[1]
recordS=[9999]
recordR=[0]
beta = 0.3
gamma = 0.05
infected = 1

time = 0
while time <= 999:
     
     infectednew = sum(np.random.choice(range(2),susceptible,p=[(1-beta*(susceptible/population)),beta*(susceptible/population)]))
     recoverednew = sum(np.random.choice(range(2),infected,p=[(1-gamma),gamma]))

     infected=infected + infectednew - recoverednew
     susceptible=susceptible - infectednew
     recovered=recovered + recoverednew
     
     recordI.append(infected)
     recordS.append(susceptible)
     recordR.append(recovered)
     time = time + 1
     
 
#Ploting  

plt.xlabel("time") 
plt.ylabel("number of people") 
plt.title("SIR model")
plt.legend("susceptible")
plt.legend("recovered")
plt.legend("infected")
plt.plot(recordI)
plt.plot(recordS)
plt.plot(recordR)
plt.savefig('SIR',type="png") 
plt.show()



