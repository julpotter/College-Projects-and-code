# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:41:43 2018
2.
IVPEuler.py
@author: Julian
"""
import matplotlib.pyplot as plt
from math import tan, exp

#specify differential equation
def dy_dt(y): 
    return (t-y)**2

#initial conditions
t = 1.0
y = 0.5

#get time step from user
h = 0.025

t_end = 0
y_end = 0
count = 0
while(t >= 0.5):
    count = count + 1
    print("Step " + str(count) + " of Heuns's")
    y_end = y + dy_dt(y)*h
    t_end = t + h
    y = y + (dy_dt(y) + dy_dt(y_end))/2*h
    print(y - tan(y))
    t = t - h
    

#specify differential equation
def dy_dt(y): 
    return (t-y)**2

#initial conditions
t = 1.0
y = 0.5

#get time step from user
h = 0.0025

t_end = 0
y_end = 0
count = 0
while(t >= 0.5025):
    count = count + 1
    print("Step " + str(count) + " of Heuns's")
    y_end = y + dy_dt(y)*h
    t_end = t + h
    y = y + (dy_dt(y) + dy_dt(y_end))/2*h
    print(y - tan(y))
    t = t - h
hf = y
    
#final values between this 200 step method and the 20 step method are
#different by about 0.001
    
#Euler method
#apply the Euler method
t = 1.0
y = 0.5
h = 0.0025
count = 0
while (t >= 0.5025):    
    count = count + 1
    print("Step " + str(count) + " of Euler's")
    print(y)
    y = y + dy_dt(y)*h
    t = t - h
ef = y
print("Relative error")
print(abs(hf - ef)) #2.9268538299e-05
