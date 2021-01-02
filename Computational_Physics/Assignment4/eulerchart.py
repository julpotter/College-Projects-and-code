# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:36:59 2018
3.
eulerchart.py
@author: Julian
"""

import matplotlib.pyplot as plt
from math import tan, exp

#specify differential equation
def dy_dt(y): 
    return 4-t+2*y

#initial conditions
t = 0.0
y = 1

#apply the Euler method

def exact(t):
    a = -7./4
    b = 1./2
    c = 11./4
    return  a + b*t + c*exp(2*t)

#solutions for exact
count = 0
for i in range(6):
    print("t = " + str(i))
    print("Exact: " + str(exact(i)))
    
#solutions for eulers at h = 0.1
h = 0.1
count = 0
while (t <= 5.0):
    print("Time: " + str(t))
    y = y + dy_dt(y)*h
    t = t + h         
    count = count + 1
    print("Step " + str(count) + " of Euler's, h = 0.1")
    print(y) 
    print(t)


#solutions for eulers at h = 0.05
h = 0.05
t = 0
count = 0
while (t <= 5.0):
    print("Time: " + str(t))
    y = y + dy_dt(y)*h
    t = t + h         
    count = count + 1
    print("Step " + str(count) + " of Euler's, h = 0.05")
    print(y) 
    print(t)


#solutions for eulers at h = 0.025
h = 0.025
t = 0
count = 0
while (t <= 5.0):
    print("Time: " + str(t))
    y = y + dy_dt(y)*h
    t = t + h         
    count = count + 1
    print("Step " + str(count) + " of Euler's, h = 0.025")
    print(y) 
    print(t)

    
#solutions for eulers at h = 0.01
h = 0.01
t = 0
count = 0
while (t <= 5.0):
    print("Time: " + str(t))
    y = y + dy_dt(y)*h
    t = t + h        
    count = count + 1
    print("Step " + str(count) + " of Euler's, h = 0.01")
    print(y) 
    print(t)


    
#solutions for eulers at h = 0.005
h = 0.005
t = 0
count = 0
while (t <= 5.0):
    print("Time: " + str(t))
    y = y + dy_dt(y)*h
    t = t + h    
    count = count + 1
    print("Step " + str(count) + " of Euler's, h = 0.005")
    print(y) 

def euler(t, h, y):
    time = 0
    while (time <= t):
        y = y + dy_dt(y)*h
        time = time + h            
    return y
    
absMagnitude1 = abs(exact(1.0) - euler(1.0, 0.005, 1))
absMagnitude5 = abs(exact(5.0) - euler(5.0, 0.005, 1))

plt.figure(1)
plt.plot(t, absMagnitude1)
plt.plot(t, absMagnitude5)

'''
the relation between error and step size indicates
that smaller step size means lesser error
'''