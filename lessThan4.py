# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:29:10 2020

@author: grezende
"""

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    newList = []
    for i in aList:
        if len(i) < 4:
            newList.append(i)
    return newList        
    
    
aList = ["apple", "cat", "dog", "banana"]
print(lessThan4(aList))    