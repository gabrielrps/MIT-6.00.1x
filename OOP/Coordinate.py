# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:17:26 2020

@author: grezende
"""

class Coordinate(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def __eq__(self, other):
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__(self):
        return "Coordinate"+ str((self.x, self.y))
    
c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin))

print(Coordinate.distance(c, origin))

print(isinstance(c, Coordinate))

foo = c - origin

print(foo)
