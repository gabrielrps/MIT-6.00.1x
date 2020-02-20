# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 10:34:40 2020

@author: grezende
"""

def quoeficient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

(x, y) = quoeficient_and_remainder(14, 5)

print("------------------------------------------")


def getData(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
        
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    
    return (min_nums, max_nums, unique_words)
            

aTuple = ((27, "Gabriel"),
          (47, "Rosicler"),
          (51, "Sérgio"),
          (21, "Sophia"))

(min_n, max_n, unique_w) = getData(aTuple)

print("------------------------------------------")

