# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:21:45 2018
projectile.py
determines motion of a projectile with air resistance
@author: Julian
"""
from math import fabs
from numpy import sin, cos, pi, sqrt, arange
import matplotlib.pyplot as plt

g = 9.8
k_D = 0.5*1.225*0.33 #C*rho*A
v = 4.0 #initial speed m/s
P = 400 #power output W
m = 70 #mass of bicyclist kg
inc = 6.0 * pi/180.0 #incline in radians
gres = g*sin(inc) #acceleration due to gravity

x = 0
t = 0
dt = 0.1
while x<=1000:
    a = -k_D*v*fabs(v)/m + P/(m*v) - gres
    v = v + a*dt
    x = x + v*dt
    t = t + dt
    plt.plot(x,v, 'r+')
  
while x<=2000:
    a = -k_D*v*fabs(v)/m + P/(m*v)
    v = v + a*dt
    x = x + v*dt
    t = t + dt
    plt.plot(x,v, 'r+')

while x<=3000:
    a = -k_D*v*fabs(v)/m + P/(m*v) + gres
    v = v + a*dt
    x = x + v*dt
    t = t + dt
    plt.plot(x,v, 'r+')



