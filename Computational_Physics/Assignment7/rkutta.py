# -*- coding: utf-8 -*-
"""
Problem 1
rkutta.py
@author: Julian
"""
from __future__ import division
from numpy import sin, cos
from numpy import arange
import matplotlib.pyplot as plt

#define our acceleration function
def acc(x,v,t):
    #return -k/m*x-2*beta*v + 0.9*cos(2.0*t/3.0)
    #return -0.5*v-sin(x)+1.5*cos(2.0*t/3.0)
    return 1 - t*sin(x)

#set initial values and range
k = 36.0 #spring constant
m = 1.0 #mass
x = 3.0
beta = 0.25
a = 0 #initial time
b = 1000.0 #final time
v = 0
N = 100000
h = 0.01

#grid pointss in lists
tpoints = arange(a,b,h)
xpoints = []
vpoints = []

#implement RK4
for t in range(40):
    k1v = acc(x,v,t)*h
    k1x = v*h
    
    k2v = acc(x+k1x/2,v+k1v/2,t+h/2)*h
    k2x = v+k1x
    
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
