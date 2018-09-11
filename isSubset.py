# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:54:24 2018

@author: Wan Jung
"""
a=list(input('a：'))
b=list(input('b：'))

def isSubset(a,b):
	return set(b) <= set(a)

print('list(a) = ' , a)
print('list(b) = ' , b)

print(isSubset(a,b))