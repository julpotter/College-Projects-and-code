# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 12:06:12 2018

euler.py
solve a differential equation by Euler's method
@author: Julian
"""

import matplotlib.pyplot as plt
from math import tan

#specify differential equation
def dy_dt(y): 
    return y*y+1

#initial conditions
t = 0
y = 0

#get time step from user
h = float(input("Enter time step h: "))

#apply the Euler method
while (t <= 2.0):
    plt.plot(t, y,'bo')
    plt.plot(t, tan(t), 'rx')
    
    y = y + dy_dt(y)*h
    t = t + h

t = 0
y = 0
    
plt.title("Euler Method")
plt.legend(loc='upper left')
plt.show()

#Heun's method (more accurate)
t_end = 0
y_end = 0
plt.figure(2)
while(t <= 2.0):
    plt.plot(t,y,'bo')
    plt.plot(t,tan(t), 'rx')
    
    y_end = y + dy_dt(y)*h
    t_end = t + h
    y = y + (dy_dt(y) + dy_dt(y_end))/2*h
    print(y - tan(y))
    t = t + h
    
plt.show()