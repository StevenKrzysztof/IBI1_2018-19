# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:45:07 2019

@author: 王梓洋
"""
n=1000
i=0
m=0
while 1==1:
  if n%2==0:
    n=n/2 
    i=i+1
    m=m+2**str(i)
    print(n,i,m)
  else:
    n=n-2**0
    n=n/2
    i=i+1
    print(n,i)
  if n==1:
     break
        