# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:34:44 2020

@author: gabriel
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if (b == 0):
        return a
    else:
        return gcdRecur(b, a % b)    

        
print(gcdRecur(2, 6))
