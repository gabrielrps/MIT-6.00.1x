# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:51:15 2020

@author: gabri
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    if s == "":
        raise ValueError("No digits")
    result = 0
    for i in s:
        try: 
            result += int(i)
        except ValueError:
            continue     
    return result  
          
          
print(sum_digits(""))          