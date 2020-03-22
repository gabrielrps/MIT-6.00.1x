# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:06:32 2020

@author: gabri
"""


def f(a,b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    #intersect: look at the common keys in d1 and d2 and apply the function f to these keys' values
    intersect = {}
    difference = {}
    for key in d1:
        if key in d2:
            difference[key] = f(d1[key],d2[key])
        else:
            intersect[key] = d1[key]
    for key in d2:
        if key not in d1:
           intersect[key] = d2[key] 
    tuple_interdiff = (difference, intersect)
    return tuple_interdiff
