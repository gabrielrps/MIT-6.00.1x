# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:15:50 2020

@author: grezende
"""

x = float(input("Entre com um número entre 0 e 1 "))

p = 0
while((2**p)*x)%1 != 0:
    print("Remainder = "+str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ""
if (num == 0):
    result = "0"
else:
    while(num > 0):
        result = str(num%2) + result
        num //= 2
    
    for i in range(len(result)):
        result = "0" + result
    
    result = result[0:-p] + "." + result[-p:]
    
print(result)    