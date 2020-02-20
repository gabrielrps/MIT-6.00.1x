# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 11:54:15 2020

@author: grezende
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for i in aDict.keys():
        result += len(aDict[i])
        
    return result    


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = 0
    index = ''
    for i in aDict.keys():
        if(len(aDict[i]) > result):
            result = len(aDict[i])
            index = i
        
    return index   



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
print(biggest(animals))