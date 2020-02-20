# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:13:07 2020

@author: grezende
"""

num = 19
result = ""

if(num < 0):
    isNeg = True
else:    
    isNeg = False

if (num == 0):
    result = "0"
else:
    while(num > 0):
        result = str(num%2) + result
        num //= 2
    
print(result)    