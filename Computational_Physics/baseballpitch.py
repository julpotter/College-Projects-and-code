# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:26:39 2018
baseballpitch.py
model a pitched baseball trajectory
@author: Julian
"""

from numpy import array
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi, exp

done = 0 #for a repeating loop

#define the drag coefficient function
def k_D(v):
    delta = 5.0
    vd = 35.0
    return 0.0039+0.0058/(1+exp((v-vd)/delta))

#define euler algorithm
def euler(vx,vy,vz,phi):
    #initial conditions
    x = 0
    y = 0
    z = 1.8 # release height in meters
    t = 0
    h= 0.0001 # time step
    k_L = 4.0E-4
    omega = 1800.0/60.0*2*pi
    g = 9.81
    
    while x<=18.44: #distance to home base from pitcher's mound
        X.append(x)
        Y.append(y)
        Z.append(z)
        
        
        v = sqrt(vx**2+vy**2+vz**2)
        #calculate acceleration components
        ax = -k_D(v)*v*vx+k_L*(vz*omega*sin(phi)-vy*omega*cos(phi))
        ay = -k_D(v)*v*vy+k_L*(vx*omega*cos(phi))
        az = -k_D(v)*v*vz-k_L*vx*omega*sin(phi)-g
        
        #apply Euler algorithm
        vx = vx+ax*h
        vy = vy+ay*h
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
    
TYPE = str(input("Input type of pitch: Fastball(f), Curveball(c), Slider(s): \n"))
if TYPE == 'c' or TYPE == 'C':
    v = 42.0
    phi = 225.8*pi/180.
if TYPE == 's' or TYPE == 'S':
    v = 42.0
    phi = 0.0
if TYPE == 'f' or TYPE == 'F':
    v = 42.0
    phi = -90.0*pi/180.0

theta = 1.0*pi/180.0 #angle from horizontal

vx = v*cos(theta)
vy = v*sin(theta)
vz = 0 #v*sin(theta)

euler(vx,vy,vz,phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.plot(X,Y,zs = Z, zdir = 'z')