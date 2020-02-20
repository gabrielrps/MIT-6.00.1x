# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:19:16 2020

@author: grezende
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    def split(word): 
        return [char for char in word]      
    
    result = ''
    secretWordSplit = split(secretWord)
    for w in secretWordSplit:
        if w in lettersGuessed:
            result += w
        else:
            result += '_'
    return result        
    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))    