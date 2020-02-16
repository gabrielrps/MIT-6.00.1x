# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:00:46 2020

@author: gabriel
"""
from math import *


def polysum(n, s):
    area = (0.25*n*(s*s))/tan(pi/n)
    perim = (n*s)**2
    return round(area+perim, 4)

print(polysum(77, 34))    
