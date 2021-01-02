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
def xprime(x,y,t):
    return exp(-0.002*t)-0.08*x-x*y**2
def yprime(x,y,t):
    return 0.08*x-y+x*y**2

#set initial values and range
x = 0
y = 0
a = 0 #initial time
b = 1000.0 #final time
N = 10000
h = (b-a)/N

#grid pointss in lists
tpoints = arange(a,b,h)
xpoints = []
ypoints = []

#implement RK4
for t in tpoints:
    k1y = yprime(x,y,t)*h
    k1x = xprime(x,y,t)*h
    
    k2y = yprime(x+k1x/2,y+k1y/2,t+h/2)*h
    k2x = xprime(x+k1x/2,y+k1y/2,t+h/2)*h
    
    k3y = yprime(x+k2x/2,y+k2y/2,t+h/2)*h
    k3x = xprime(x+k2x/2,y+k2y/2,t+h/2)*h
    
    k4y = yprime(x+k3x,y+k3y,t+h)*h
    k4x = xprime(x+k3x,y+k3y,t+h)*h
    
    
    x = x+(1/6.0)*(k1x+2*k2x+2*k3x+k4x)
    y = y + (1/6.0)*(k1y+2*k2y+2*k3y+k4y)
    
    xpoints.append(x)
    ypoints.append(y)
    
#plot results
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(tpoints,xpoints,zs=ypoints,zdir='z') #plot trajectory in 3D
ax.set_xlim3d(0,1000)
ax.set_ylim3d(0,2.5)
ax.set_zlim3d(0,2.5)
plt.show()
