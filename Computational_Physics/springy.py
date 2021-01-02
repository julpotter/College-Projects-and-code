# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:14:50 2018

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
