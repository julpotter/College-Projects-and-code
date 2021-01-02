# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 20:09:24 2018
1. Help Dak Prescott keep his starting position as quarterback for the Dallas Cowboys.
Prescott offers you a lucrative consulting fee to determine the optimum angle of launch
for a pass. He can throw the ball with an initial speed of 30 m/s. Write a Python program
that uses the modified solves the equations of motion assuming quadratic air resistance.
The terminal velocity of a football is 45 m/s. Plot the range as a function of the angle.
Answer the following questions:
(a) At what launch angle (to the nearest ½o, he is very accurate, you know) should he
throw the ball for the greatest range in air?
(b) Any capable quarterback can throw a football up to 80 yards; do your results
agree with this observation?
@author: Julian
"""


"""
Created on Mon Oct  1 12:21:45 2018
projectile.py
determines motion of a projectile with air resistance
@author: Julian
"""
from numpy import sin, cos, pi, sqrt, arange, argmax
import matplotlib.pyplot as plt

g = 9.8
#k_D = float(input("Enter the drag coefficient k_D: "))
k_D = g/45**2
v = 30
#theta = float(input("Enter the initial angle in degrees: "))
#theta = theta*pi/180
theta = []
dist = []
for i in arange(10,50.1,0.1):
    theta.append(i)
    
    
def euler(vx,vy,dist):
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
    dist.append(x)
        
for i in theta:
    i = i*pi/180.
    vx = v*cos(i)
    vy = v*sin(i)
    euler(vx,vy,dist)

plt.plot(theta,dist,'darkslateblue')
print("Max range is {0:4.2f} m at an angle of {1:4.2f} degrees.".format(max(dist),theta[argmax(dist)]))


'''
a. 42.5 degrees
b. Yes, because the max distance at an initial velocity of 30m/s
reaches up to about 69 meters, which equals about 75 yards
'''


plt.show()

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


'''
Terminal velocity is 12.558 m/s
This finding is a bit less than that record. This is likely because
the world-record holder had reduced drag and more mass, so he had 
higher terminal velocity.
'''
