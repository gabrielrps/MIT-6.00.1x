# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:16:50 2020

@author: gabri
"""
def bi_search(L, n):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == n
    else:
        half = len(L) // 2
        if(L[half] > n):
            return bi_search(L[:half], n)
        else:
            return bi_search(L[half:], n)
        
    

L = [1,5,6,8,3,5,2,9,0]

print(bi_search(sorted(L), 3))

