# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:20:19 2020

@author: grezende
"""


def fact_rec(x):
    if (x == 1):
        return 1
    
    return x * fact_rec(x-1)

print(fact_rec(5))
