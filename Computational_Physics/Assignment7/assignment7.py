# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:17:08 2018

@author: Julian
"""

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


# -*- coding: utf-8 -*-
"""
Problem 2
Created on Mon Nov  5 12:43:15 2018
oscillator.py
solves a damped harmonic oscillator using RK4
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
    return xprime + 0.1*x + 25

#set initial values and range
k = 36.0 #spring constant
m = 1.0 #mass
x = 3.0
xprime = 0
beta = 0.25
a = 0 #initial time
b = 1000.0 #final time
v = 0
N = 100000
h = (b-a)/N

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




# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:14:50 2018
Problem 4.
@author: Julian
springy.py
"""
from __future__ import division
from math import sin, cos, pi
from numpy import arange
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt

#define our accelerations
def accL(L, theta, thetadot):
    return (L0 + L)*thetadot**2 - (k/m)*L+g*cos(theta)

def acctheta(L, Ldot, theta, thetadot):
    return -(1/(L0 + L)*(g*sin(theta))+2*Ldot*thetadot)

#define constants, initial values, ranges
k = 4.9 #spring constant
m = 5.0 #mass
L = 0.5 #initial length
L0 = 1.0
Ldot = 0
theta = pi/4
thetadot = 0.0
g = 9.81 #gravity
a = 0
b = 60 #times in seconds
N = 2000
h = (b-a)/N



#set up grid points in lists
tpoints = arange(a,b,h)
thetapoints = []
thetadotpoints = []
Lpoints = []
Ldotpoints = []


#implement Runge Kutta
for t in tpoints:
    k1thetadot = acctheta(L,Ldot,theta,thetadot)*h
    k1Ldot = accL(L,theta,thetadot)*h
    
    k1theta = thetadot*h
    k1L = Ldot*h
    
    k2thetadot = acctheta(L+k1L/2,Ldot+k1Ldot/2,theta+k1theta/2,thetadot+k1thetadot/2)*h
    k2Ldot = accL(L+k1L/2,theta+k1theta/2,thetadot+k1thetadot/2)*h
    
    k2theta = (thetadot + k1thetadot/2)*h
    k2L = (Ldot+k1Ldot/2)*h
    
    k3thetadot = acctheta(L+k2L/2,Ldot+k2Ldot/2,theta+k2theta/2,thetadot+k2thetadot/2)*h
    k3Ldot = accL(L+k2L/2,theta+k2theta/2,thetadot+k2thetadot/2)*h
    
    k3theta = (thetadot + k2thetadot/2)*h
    k3L = (Ldot+k2Ldot/2)*h
    
    k4thetadot = acctheta(L+k3L/2,Ldot+k3Ldot/2,theta+k3theta/2,thetadot+k3thetadot/2)*h
    k4Ldot = accL(L + k3L, theta + k3theta, thetadot + k3thetadot)*h
    
    k4theta = (thetadot + k3thetadot)*h
    k4L = (Ldot + k3Ldot)*h
    
    
    L = L + (k1L+2*k2L+2*k3L + k4L)/6
    Ldot = Ldot+(k1Ldot+2*k3Ldot+k4Ldot)/6
    
    theta = theta + (k1theta + 2*k3theta + 2*k3theta+k4theta)/6
    thetadot = thetadot + (k1thetadot + 2*k2thetadot+2*k3thetadot+k4thetadot)/6
    
    thetapoints.append(theta)
    thetadotpoints.append(thetadot)
    Lpoints.append(L)
    Ldotpoints.append(Ldot)
    
    
plt.figure(1)
plt.xlabel('t')
plt.ylabel('L')
plt.plot(tpoints,Lpoints)

plt.figure(2)
plt.xlabel('t')
plt.ylabel('theta')
plt.plot(tpoints,thetapoints)

plt.figure(3)
plt.xlabel('t')
plt.ylabel('Ldot')
plt.plot(Lpoints, Ldotpoints)

plt.figure(4)
plt.xlabel('theta')
plt.ylabel('thetadot')
plt.plot(thetapoints,thetadotpoints)
