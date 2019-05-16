# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:26:33 2019

@author: 王梓洋
"""

import re


DNA=input("Please type in a DNA sequence:")
while 1==1:    
    try:
        if re.search('[^ATCG]', DNA) or (DNA.find('T') * DNA.find('U') > -1):
            print('Please input the correct sequence:', end='') #end='' ensures no extra white line after input
            DNA = input('')
        else:
            break
    except:
        print('Please input the correct sequence:', end='')
        DNA = input('')
                
                
DNA=list(DNA)

myDict={}
for word in DNA:
    if word in myDict:
        myDict[word]+=1
    else:
        myDict[word]=1
myDict
print(myDict)
import matplotlib.pyplot as plt
labels='A', 'T', 'C', 'G'
A=myDict['A']
T=myDict['T']
C=myDict['C']
G=myDict['G']
sizes=[A,T,C,G]
explode=(0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show 