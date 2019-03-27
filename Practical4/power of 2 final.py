# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:48:50 2019

@author: 王梓洋
"""

x=1498
y=str(x)+" = "
m=13
for i in range (0,14):
    if x/2**m>1:
        x=x-2**m
        y=y+"2**"+str(m)+"+"
    elif x/2**m==1:
        x=0
        y=y+"2**"+str(m)
    else:
        x=x
        y=y
    m=m-1
print(y)