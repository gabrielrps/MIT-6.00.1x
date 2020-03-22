# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:39:45 2020

@author: gabri
"""

def selection_sort(L):
    suffixSet = 0
    while suffixSet != len(L):
        for i in range(suffixSet, len(L)):
            if L[i] < L[suffixSet]:
                print(L)
                L[suffixSet], L[i] = L[i], L[suffixSet]
        suffixSet += 1  
        
    return L    
        
        
        

L = [1,5,6,8,3,5,2,9,0]

print(selection_sort(L))
        