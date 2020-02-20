# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:09:05 2020

@author: grezende
"""




def mult_iter(x , y):
    result = 0
    while(y > 0):
        result += x
        y -= 1
    return result;

print(mult_iter(2,6));    