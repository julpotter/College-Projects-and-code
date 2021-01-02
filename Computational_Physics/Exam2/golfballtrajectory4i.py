# -*- coding: utf-8 -*-
"""
Created on Oct 21
golfballtrajectory4i.py
model golfball trajectory
@author: Julian
"""

from numpy import array, cross
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi, exp

done = 0 #for a repeating loop

#define the drag coefficient function
def k_D(v):
    if v<= 14:
        return 0.5
    if v>14:
        return 7.0/v
#define euler algorithm
def euler(vx,vy,vz,phi):
    #initial conditions
    x = 0
    y = 0
    z = 1.8 # release height in meters
    t = 0
    h= 0.0001 # time step
    k_L = 4.0E-4
    omega = 0
    g = 9.81
    
    while x<=18.44: #distance to home base from pitcher's mound
        X.append(x)
        Y.append(y)
        Z.append(z)
        
        
        v = sqrt(vx**2+vy**2+vz**2)
        #calculate acceleration components
        ax = -k_D(v)*v*vx+k_L*(vz*omega*sin(phi)-vy*omega*cos(phi))
        az = -k_D(v)*v*vz-k_L*vx*omega*sin(phi)-g
        #apply Euler algorithm
        vx = vx+ax*h
        vy = 0
        vz = vz+az*h
        
        x = x+vx*h
        y = y+vy*h
        z = z+vz*h
        t = t+h

#define out loop
#while not done:
X = []
Y = []
Z = []
    
v = 70.0
phi = 225.8*pi/180.


theta = 9.0*pi/180.0 #angle from horizontal

vx = v*cos(theta)
vy = 0
vz = v*sin(theta)

euler(vx,vy,vz,phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.plot(X,Y,zs = Z, zdir = 'z')