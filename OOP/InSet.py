# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:29:25 2020

@author: grezende
"""

class intSet(object):
    
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + " not found")
            
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ","
        
        return "{"+ result[:-1] +"}"
    
    def __len__(self):
        return len(self.vals)

    def intersect(self, other):
        result = intSet()
            
        for e in self.vals:
            if e in other.vals:
                result.insert(e)

        return result
    
s = intSet()
s.insert(3)
s.insert(4)
s.insert(3)    

print(s)