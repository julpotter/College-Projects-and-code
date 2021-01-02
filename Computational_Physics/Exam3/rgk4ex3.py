# -*- coding: utf-8 -*-
"""

Created on Mon Nov  5 12:43:15 2018
oscillator.py
solves a damped harmonic oscillator using RK4
@author: Julian
"""
from __future__ import division
from numpy import sin, cos, exp
from numpy import arange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#define our acceleration function
def acc(x,v,t):
    #return -k/m*sin(x)-beta*v + 0.52*cos(omega*t)
    #return -0.5*v-sin(x)+1.5*cos(2.0*t/3.0)
    #return 3.0*sin(4.0*t) - 36*x100000
    return -25*x-0.05*v+100*sin(5.6*t)

#set initial values and range
k = 1.0 #spring constant
m = 1.0 #mass
omega = 4.2 #frequency of the driving force
x = 0
beta = 0.2 #damping coefficient
a = 0 #initial time
b = 40.0 #final time
v = 0
N = 10000
h = (b-a)/N
t = 0

#grid pointss in lists
tpoints = arange(a,b,h)
xpoints = []
vpoints = []

#implement RK4
for t in tpoints:
    k1v = acc(x,v,t)*h
    k1x = v*h
    
    k2v = acc(x+k1x/2,v+k1v/2,t+h/2)*h
    k2x = (v+k1v/2)*h
    
    k3v = acc(x+k2x/2,v+k2v/2,t+h/2)*h
    k3x = (v+k2v/2)*h
    
    k4v = acc(x+k3x,v+k3v,t+h)*h
    k4x = (v+k3v)*h
    
    
    x = x+(1/6)*(k1x+2*k2x+2*k3x+k4x)
    v = v + (1/6)*(k1v+2*k2v+2*k3v+k4v)
    
    xpoints.append(x)
    vpoints.append(v)
    
#plot results
plt.figure(1)
plt.xlabel('t')
plt.ylabel('x')
plt.plot(tpoints, xpoints, 'rx')
plt.show()

plt.figure(2)
plt.xlabel('x')
plt.ylabel('v')
plt.plot(xpoints, vpoints, 'b+')
plt.show()
