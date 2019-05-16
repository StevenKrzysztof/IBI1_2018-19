# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:49:10 2019

@author: 王梓洋
"""

# give n a value
n=98
#loop until the answer is 1
while 1==1:
# if n can be divided evenly by 2, keep n/2 for the next time of the loop and print the value.  
  if n%2==0:
    n=n/2
    print(n)
# if n can not be divided evenly by 2, make n= n*3+1 for the next time of the loop.
  elif n%2!=0:
    n=n*3+1
    print(n)
  if n==1:
      break