# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:24:42 2020

@author: grezende
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    result = 0
    if base > num:
        result = 0
    elif base == num:
        result = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                result = i
                break
    return result


print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))