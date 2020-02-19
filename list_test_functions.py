# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:45:17 2020

@author: gabri
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

lista = [-1,-2,-3,4, 5.5]

applyToEach(lista, abs)
print(lista)

applyToEach(lista, int)
print(lista)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
