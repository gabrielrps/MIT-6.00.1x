# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 13:36:10 2020

@author: gabri
"""

import pylab as plt

mySample = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


for i in range(30):
    mySample.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    

    
plt.figure("lin quad")
plt.clf()
plt.subplot(121)
plt.ylim(0, 900)
plt.plot(mySample, myLinear, "b-", label="Linear", linewidth=1.0)
plt.subplot(122)
plt.ylim(0, 900)
plt.plot(mySample, myQuadratic, "ro", label="Quadratic", linewidth=1.0)

plt.figure("cube exp")
plt.clf()
plt.plot(mySample, myCubic, "g^", label="Cubic", linewidth=1.0)
plt.plot(mySample, myExponential, "r--", label="Exponencial", linewidth=1.0)

plt.figure("lin quad")
plt.title("Linear x Quadratic")
plt.xlabel("Sample Points")
plt.legend(loc = "upper left")

plt.figure("cube exp")
plt.title("Cube x Exponencial")
plt.xlabel("Sample Points")
plt.yscale("log")
plt.legend(loc = "upper right")


