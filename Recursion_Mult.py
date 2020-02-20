# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 22:12:34 2020

@author: grezende
"""


def mult_rec(x ,y):
    if (y == 1):
        return x
    return x + mult_rec(x, y-1)

print(mult_rec(3,8))