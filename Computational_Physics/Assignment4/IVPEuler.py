# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:29:52 2018
IVPEuler.py

Solve the following IVP using Euler’s method and print
out the value of y(t) every from t = 0
until t = 2 for h = 0.1:    
dy_dt = e^(-2t) - y, y(0) = 1.

@author: Julian
"""
import matplotlib.pyplot as plt
from math import tan, exp

#specify differential equation
def dy_dt(y): 
    return exp(-2 * t) - y

#initial conditions
t = 0
y = 1

#get time step from user
h = 0.1

#apply the Euler method
while (t <= 2.0):    
    print(y)
    y = y + dy_dt(y)*h
    t = t + h


    


