# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:56:22 2020

@author: grezende
"""
high=100
low=0
guessed=False
print("Please think of a number between 0 and 100!")

while(not guessed):
    guess = (high + low) // 2
    print("Is your secret number " + str(guess) + "?")
    input_usr = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(input_usr == 'h'):
        high = guess
    elif(input_usr == 'l'):
        low = guess
    elif(input_usr == 'c'):
        guessed = True
    else:
        print("Please, insert a correct option")

print("Game over. Your secret number was: " + str(guess))        

