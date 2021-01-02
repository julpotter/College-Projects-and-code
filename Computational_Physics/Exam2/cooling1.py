# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:45:51 2018
cooling.py
solve newton's law of cooling
@author: olenick
"""
import matplotlib.pyplot as plt
from math import sin, pi

def R(T,Ts):
    return -r*(T- Ts)

def Ts(t):
    return 92 - 10*sin(2*pi*(t+3)/24)

#initialize parameters
t = 0
T = 68  #in Fahrenheit

Tend = 0.0
tend = 0.0
r = 0.15
h = 0.1
Tsur = 25

#apply Heun's method
while t < 48.0:
    tend = t + h
    Tend = T + R(T,Tsur)*h
    T = T + (R(T, Tsur) + R(Tend, Tsur))/2.0*h
    t = t + h
    
    plt.plot(t, T, 'bo')
    plt.plot(t, Tsur, 'rx')
