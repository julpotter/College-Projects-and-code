# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:59:25 2018


Plot the function y(t) = v(at0)t-(1/2)gt^2 for v0 = 20.0 m/s and g = 9.81 m/s^2
. Label the x axis
as “time (s)’ and the y axis as “position (m)”. Call your program ball.py. Determine the
maximum height reached by the ball.
@author: Julian
"""
import numpy as np
import matplotlib.pyplot as plt

N = 22
s = 0
m = 0
vzero = 20.0 #m/s
vzero2 = 5.0 #m/s
vzero3 = 15.0 #m/s
vzero4 = 25.0 #m/s

g = -9.81 #m/s^2
for i in range(N):
    plt.plot(s, m, 'bo')
    s = s + .2
    m = vzero * s + (g*s*s) / 2 

#vzero
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.show()

#maximum height is 20 meters

#vzero2
s = 0
m = 0
for i in range(N):
    plt.plot(s, m, 'ro')
    s = s + .2
    m = vzero2 * s + (g*s*s) / 2 

plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.show()

#vzero3
s = 0
m = 0
for i in range(N):
    plt.plot(s, m, 'go')
    s = s + .2
    m = vzero3 * s + (g*s*s) / 2 

plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.show()

#vzero4
s = 0
m = 0
for i in range(N):
    plt.plot(s, m, color='purple', marker='o')
    s = s + .2
    m = vzero4 * s + (g*s*s) / 2 

plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.show()
