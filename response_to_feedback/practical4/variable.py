# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:28:13 2019

@author: 王梓洋
"""

a=123
b=123123
print('the remainder of b divided by 7 is ',b%7)
print('b divided by 7 is ',b/7)
c=b/7
d=c/11
e=d/13
print('value of c is ',c,'value of d is ',d,'value of e is ',e)
#e and a are the same
print('e is the same as a is ',e==a)
X=(5<12)
Y=(9<7)
print('X is ',X,';''Y is ',Y)
Z = (X and not Y) or (Y and not X)
print('either X or Y is ture is ',Z)
W = (X!=Y)
print('Zhiwen''s more elegant solution is ',W)
print('W and Z are always the same is ',W==Z)
