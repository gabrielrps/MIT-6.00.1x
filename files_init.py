# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:52:38 2020

@author: gabriel
"""

def createArq():
    nameArq = open("teste", "w")
    
    for i in range(2):
        name = input("What's your name? ")
        name += "\n"
        nameArq.write(name)
        
    nameArq.close()    
    
def readArq():
    nameArq = open("teste", "r")
    
    for i in nameArq:
        print(i)
        
    nameArq.close()        


createArq()
readArq()