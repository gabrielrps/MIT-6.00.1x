# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:23:25 2020

@author: gabriel
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
      return aStr == char

    midIndex = len(aStr) // 2
    midChar = aStr[midIndex]
    
    if char == midChar:
       return True
    elif(char < midChar):
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])
            
        
    

print(isIn("z", "eghhjklruvwwzzz"))