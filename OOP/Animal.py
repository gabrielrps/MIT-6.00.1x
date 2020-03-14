# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:40:22 2020

@author: grezende
"""

class Animal(object):
    
    def __init__(self, age):
        self.age = age
        self.name = None
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newAge):
        self.age = newAge
        
    def set_name(self, newName=""):
        self.name = newName
        
    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)
    
class Cat(Animal):
    
    def speak(self):
        print("meow")
    
    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.age)    

class Rabbit(Animal):
    
    def speak(self):
        print("meep")
    
    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.age)    
    
        