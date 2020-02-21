# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:32:49 2020

@author: grezende
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    newList = {}
    result = set()
    for k,v in aDict.items():
        if v in newList:
            result.discard(newList[v])
        else:
            newList[v] = k
            result.add(k)
    return sorted(list(result))

    
    

print(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}))