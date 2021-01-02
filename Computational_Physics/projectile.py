# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:21:45 2018
projectile.py
determines motion of a projectile with air resistance
@author: Julian
"""
from numpy import sin, cos, pi, sqrt, arange
import matplotlib.pyplot as plt

g = 9.8
k_D = float(input("Enter the drag coefficient k_D: "))
#k_D = g/45**2
v = float(input("Enter the initial speed: "))
theta = float(input("Enter the initial angle in degrees: "))
theta = theta*pi/180


def euler(vx,vy):
    g = 9.8
    x = 0
    y = 0
    t = 0
    dt = 0.01
    
    while y>=0:
        ax = -k_D*sqrt(vx*vx + vy*vy)*vx
        ay = -g - k_D*sqrt(vx*vx+vy*vy)*vy
        vx = vx + ax*dt
        vy = vy + ay*dt
        
        x = x + vx*dt
        y = y + vy*dt
        t = t + dt
        
        plt.plot(x,y,'r+')
        #plt.plot(t,v, 'bo')
        
vx = v*cos(theta)
vy = v*sin(theta)

euler(vx,vy)

plt.show()