# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:48:19 2018
coldmedication.py
solves differential equation for cold medication in GI tract and bloodstream
@author: Julian
"""

import matplotlib.pyplot as plt

#initial conditions
t = 0
tstop = 120
h = 0.05 #step size
I = 0 # pill dosage
y = 0 # no cold medication in bloodstream at the start
x = 0 # no cold medication in the GI tract
k1 = 0.6931 #dissolving constant
k2 = 0.231 #clearing constant (I set this to 0.231 rather than
#0.0231, which didn't work well graphically or with runtime)

xend = 0
yend = 0
tend = 0

#define rates

def Rx(x,I):
    return I-k1*x

def Ry(x,y):
    return k1*x-k2*y

plt.axis([0,tstop,0,12])

while t <= tstop:
    if t%4 <= 4.5%4:
        I = 12.0
    else:
        I = 0
    
    xend = x + Rx(x,I)*h 
    tend = t + h
    
    yend = y + Ry(x,y)*h #y concentration at end of our step
    
    y = y + (Ry(x,y) + Ry(xend,yend))/2.0*h
    x = x + (Rx(x,I) + Rx(xend, I))/2.0*h
    
    plt.plot(t,x,'b+')
    plt.plot(t,y,'r+')
    t = t + h
    
plt.show()

'''
a. The medication in the GI decreases as the medication in the bloodstream
raises somewhat. This is because the medication is diffusing from the GI
and into the bloodstream.
b. The amount of medication in the blood stream reaches 
its low point after about 5-6 hours
c. Cecilia falls asleep first, because she has the lowest rate of diffusion,
which means that more antihistamine will accumulate in her blood.
'''

