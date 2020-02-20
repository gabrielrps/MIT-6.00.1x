# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:00:03 2020

@author: grezende
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    t = ()
    for i in range(len(aTup)):
        if(i % 2 == 0):
            t = t + (aTup[i],)
    return t            

def oddTuples2(aTup):
    '''
    Another way 
    
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]
        
t = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(t))
print(oddTuples2(t))
