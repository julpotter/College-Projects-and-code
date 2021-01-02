# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:35:49 2018
ballAB.py
4.
@author: Julian
"""
from numpy import sqrt
import matplotlib.pyplot as plt
g = -9.8
#find maximum height of thrown balls A and B
mhAB = 35 + (25 / (9.8 * 2))

#a.
print(mhAB) #max height is 36.27m
mt = sqrt((mhAB - 35) / 4.9) #time it takes either ball to travel to max height

print(mt)
#b.
d = 5 * (1 - mt) + (1/2) * (-9.8) * (1 - mt)**2 #distance apart
print(d) #distance apart is 2.4m

#c. determine the distance between the balls over time
dt = d / 1 #distance over time
print(dt)


N = 30
t = 0
Ay = 35
By = 35
for i in range(N):
    plt.plot(t, Ay, 'ro')
    plt.plot(t, By, 'bo')
    Ay = Ay + 5*t+(g*t*t)/2
    t = t + .1
    By = By + 5*t+(g*t*t)/2


plt.figure(1)    
plt.xlabel('Time')
plt.ylabel('Position')       
plt.show()

#e.
N = 30
t = 0
Ay = 35
By = 35
d = 0
plt.figure(2)
for i in range(N):
    plt.plot(t, d, 'bo')
    Ay = Ay + 5*t+(g*t*t)/2
    t = t + .1
    By = By + 5*t+(g*t*t)/2
    d = abs(Ay - By)

plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.show()

#f. The balls start together, drift apart, and then converge before
# dropping to continuously drift apart. This is expected because the
# balls are at the same vertical height at one point when one is falling
# and one is rising, but afterwards, they continuously drift apart



