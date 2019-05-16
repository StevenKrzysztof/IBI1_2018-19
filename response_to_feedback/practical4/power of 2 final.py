# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:48:50 2019

@author: 王梓洋
"""

# given an integer, find how it could be shown as the powers of 2
# to give an integer

import random
x=random.randint(0,8192)
'''
# if you want to test by x = 1750, you can delete comments above and use this.
x = 1750
'''
# to make the result in fomat of "integer = (a serious powers of 2 adding together)"
y=str(x)+" is "
#make sure the integer is no larger than 8192(2**13) 
m=13
#loop to find the powers(calculate no more than 14 times) 
for i in range (0,14):
#if the integer is larger than 2**m, then we minus the integer by 2**m for the next time of the loop and keep m in y
    if x/2**m>1:
        x=x-2**m
        y=y+"2**"+str(m)+"+"
# if the integer is divisible by 2**m, then we keep the solution for the next time of the loop and keep m in y 
    elif x/2**m==1:
        x=0
        y=y+"2**"+str(m)
# if the integer is smaller than 2**m, then keep x and y for the next time of the loop.
    else:
        x=x
        y=y
    m=m-1
print(y)