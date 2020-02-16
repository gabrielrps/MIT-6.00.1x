# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:17:49 2020

@author: gabriel
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testValue = min(a, b)
    print(testValue)

    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue


print(gcdIter(100, 12))