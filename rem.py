# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 21:57:35 2020

@author: grezende
"""

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        
        
print(rem(7, 5))        