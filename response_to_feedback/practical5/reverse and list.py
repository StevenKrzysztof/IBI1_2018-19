# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:26:33 2019

@author: 王梓洋
"""

X=input("Please give me a sring of words:")
X=X.split(' ')
X.reverse()
M=X[:]

n=0
L=[]
while 1==1:
    zwy=X[n]
    listen=list(zwy)
    listen.reverse()
    cjj="".join(listen)
    L.append(cjj)
    n=n+1
    if n>len(X)-1:
        break
L.sort()
L.reverse()
print(L)