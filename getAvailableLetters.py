# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:33:21 2020

@author: grezende
"""

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    def split(word): 
        return [char for char in word]   
    
    listAlph = split(string.ascii_lowercase)
    
    for i in split(string.ascii_lowercase):
        if i in lettersGuessed:
            listAlph.remove(i)
            
    return ''.join(listAlph)        
            
    

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

