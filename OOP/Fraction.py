# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:04:14 2020

@author: grezende
"""

class Fraction(object):
    
    def __init__(self, numer, demom):
        self.numer = numer
        self.demom = demom
        
    def __str__(self):
        return str(self.numer) + " / " + str(self.demom)
    
    def getNumer(self):
        return self.numer
    
    def getDemom(self):
        return self.demom
    
    def __add__(self, other):
        numerNew = other.getDemom() * self.getNumer() + other.getNumer() * self.getDemom()
        demomNew = other.getDemom() * self.getDemom()
        
        return Fraction(numerNew, demomNew)
    
    def __sub__(self, other):
        numerNew = other.getDemom() * self.getNumer() - other.getNumer() * self.getDemom()
        demomNew = other.getDemom() * self.getDemom()
        
        return Fraction(numerNew, demomNew)
    
    def convert(self):
        return self.getNumer() / self.getDemom()
    
    
 
oneHalf = Fraction(1,2)
twoThirds = Fraction(2,3)    

new = oneHalf + twoThirds

print(new)

print(new.convert())
    
    
        