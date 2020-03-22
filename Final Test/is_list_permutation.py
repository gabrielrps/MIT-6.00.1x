# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:00:43 2020

@author: gabri
"""

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']


def isPermutation(list1,list2):
    if len(list1) != len(list2):
        return False;  #two list does not have same length so impossible being permutation of each other
    for i in range(0, len(list1)):
        if list1.count(list1[i]) != list2.count(list1[i]):
            return False

def is_list_permutation(list1,list2):
    if (isPermutation(list1,list2) == False): #use the above method isPermutation to check if they are permutation of each other
        return False #if not return false
    elif not list1:
        return (None, None, None)
    else:
        mostOccurItem = max(set(list1), key=list1.count)  
        numberOfTimes = list1.count(mostOccurItem)
        theType = type(mostOccurItem)
        return (mostOccurItem, numberOfTimes, theType)

print(is_list_permutation(L1,L2))