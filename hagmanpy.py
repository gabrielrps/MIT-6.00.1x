# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:31:17 2020

@author: grezende
"""

def isWordGuessed(secretWord, lettersGuessed):
    def split(word): 
        return [char for char in word]      
    
    count = 0
    secretWordSplit = split(secretWord)
    for w in secretWordSplit:
        if w in lettersGuessed:
            count +=1 
    
    if count == len(secretWord):
        return True
    else:
        return False    

def getAvailableLetters(lettersGuessed):
    import string
    def split(word): 
        return [char for char in word]   
    
    listAlph = split(string.ascii_lowercase)
    
    for i in split(string.ascii_lowercase):
        if i in lettersGuessed:
            listAlph.remove(i)
            
    return ''.join(listAlph)        
            
def getGuessedWord(secretWord, lettersGuessed):
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

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Bem vindo ao jogo da forca!')
    print('A palavram tem ', len(secretWord), " letras.")
    erradas = 0
    letrasChutadas = []
    secretWord = secretWord.lower()
    
    while(8 - erradas > 0):
        if(isWordGuessed(secretWord, letrasChutadas)):
            print("*--------------------------------------------*")
            print("Parabéns você acerto a palavra:", secretWord)
            break
        else:
            print("*--------------------------------------------*")
            print('Você tem', 8 - erradas, 'tentativas restantes')
            print('Letras disponíveis:', getAvailableLetters(letrasChutadas))
            letra = input("Digite a letra que deseja: ", )
            if(letra in secretWord and letra not in letrasChutadas):
                print("*--------------------------------------------*")
                letrasChutadas.append(letra)
                print('Bom chute:', getGuessedWord(secretWord, letrasChutadas))
            elif(letra in letrasChutadas):
                print("*--------------------------------------------*")
                print("Essa letra já foi selecionada", getGuessedWord(secretWord, letrasChutadas))
            elif letra not in secretWord:
                print("*--------------------------------------------*")
                print("Essa letra não existe na palavra =(", getGuessedWord(secretWord, letrasChutadas))
                letrasChutadas.append(letra)
                erradas += 1
    
            if 8 - erradas == 0:
                print("*--------------------------------------------*")
                print('Desculpa! Mas você não acertou a palavra', secretWord)
                break
            else:
                continue             
            
                       
import random

inFile = open("words.txt", "r")
line = inFile.readline()
print(line)
wordList = line.split()
print("  ", len(wordList), "palavras carregadas")
hangman(random.choice(wordList))
