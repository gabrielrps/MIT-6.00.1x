# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:23:36 2020

@author: gabri
"""

import random

def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(L)):
            if(L[i-1] > L[i]):
                swap = False
                temp = L[i]
                L[i] = L[i-1]
                L[i-1] = temp
                
    return L            
                
        
L = list(range(1, 2000))
         
random.shuffle(L)

print("-----------------------------------")

print(bubble_sort(L))
