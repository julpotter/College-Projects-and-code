# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 12:15:18 2018
bunny.py
non linear map
@author: Julian
"""
import matplotlib.pyplot as plt
 
r = float(input("Enter the value of r: "))
N = 200
x = float(input("Enter the initial value of x: ")) #population of rabbits
xlist = []
xnewlist = []

for i in range(N):
    xlist.append(x)
    x = 4*r*x*(1-x)
    xnewlist.append(x)
    

plt.plot(xlist,xnewlist, 'ro')
plt.show()