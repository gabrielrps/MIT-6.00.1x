# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:40:46 2020

@author: grezende
"""

epsilon = 0.01
y = 25.0
guess = y/2.0
numGuesses = 0

while(abs(guess*guess - y ) >= epsilon):
    numGuesses += 1
    guess = guess - (((guess**2) - y ) / (2*guess))
    
print("numGuesses = " + str(numGuesses))
print("Square Root of " + str(y) + " is about " + str(guess))   