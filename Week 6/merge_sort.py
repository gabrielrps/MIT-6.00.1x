# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:05:26 2020

@author: gabri
"""
import random

def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    while (i < len(left)):
        result.append(left[i])
        i += 1
    
    while (j < len(right)):
        result.append(right[j])
        j += 1
    
    return result
    

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left, right)
            
        


L = list(range(100))

random.shuffle(L)

print(mergeSort(L))
        