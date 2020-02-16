# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:46:04 2020

@author: gabriel
"""

def fibonacci_rec(x):
    if x < 2:
        return 1
    
    return fibonacci_rec(x-1) + fibonacci_rec(x-2)

print(fibonacci_rec(4))