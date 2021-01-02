# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:21:45 2018
2.
You are assigned to find the terminal velocity for an elite bicyclist of mass 70 kg.
Assume that the drag force is given by 2 , drag
v
F C Av
v
   where ρ is the density of air,
A the frontal area of the bicyclist, and C the drag coefficient which we will take equal to
½. (We don’t know a precise value for the drag coefficient of a bicyclist but the best wat
to determine it via wind tunnel measurements.) Assume a frontal area of A = 0.33 m2,
which is typical of a rider in racing crouch. Assume that the bicyclist can maintain a
constant power output P = 400 W for an extended period of time and has an initial
velocity of 4.0 m/s. Graph the velocity of the bicyclist as a function of time from 0 to
200 seconds. What is the terminal velocity that you find? In 1995 the record for the
distance traveled by bicycle in 1 hour is a little more than 55 km, which corresponds to an
average velocity of approximately 15 m/s. How does your finding compare with this
value?
@author: Julian
"""
from math import fabs
from numpy import sin, cos, pi, sqrt, arange
import matplotlib.pyplot as plt

g = 9.8
k_D = 0.5*1.225*0.33 #C*rho*A
v = 4.0 #initial speed
P = 400 #power output
m = 70 #mass of bicyclist

x = 0
t = 0
dt = 0.1

while t<=200:
    a = -k_D*v*fabs(v)/m + P/(m*v)
    v = v + a*dt
    x = x + v*dt
    t = t + dt
    plt.plot(t,v, 'r+')
    

print("Max speed is {0:4.2f}".format(v))