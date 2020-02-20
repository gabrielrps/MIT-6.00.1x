# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:08:05 2020

@author: grezende
"""


def fib_efficient(n, d):
    global numCount
    numCount += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
    
    

numCount = 0
d = {1:1, 2:2}
print(fib_efficient(34, d))
print(numCount)