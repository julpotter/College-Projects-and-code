# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:48:23 2018
assignment4.py

@author: Julian
"""

"""
Created on Mon Oct  1 17:29:52 2018
IVPEuler.py
1.
Solve the following IVP using Euler’s method and print
out the value of y(t) every from t = 0
until t = 2 for h = 0.1:    
dy_dt = e^(-2t) - y, y(0) = 1.

@author: Julian
"""
import matplotlib.pyplot as plt
from math import tan, exp

#specify differential equation
def dy_dt(y): 
    return exp(-2 * t) - y

#initial conditions
t = 0
y = 1

#get time step from user
h = 0.1

#apply the Euler method
while (t <= 2.0):    
    print(y)
    y = y + dy_dt(y)*h
    t = t + h
    
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 17:41:43 2018
2.
IVPEuler.py
@author: Julian
"""
import matplotlib.pyplot as plt
from math import tan, exp

#specify differential equation
def dy_dt(y): 
    return (t-y)**2

#initial conditions
t = 1.0
y = 0.5

#get time step from user
h = 0.025

t_end = 0
y_end = 0
count = 0
while(t >= 0.5):
    count = count + 1
    print("Step " + str(count) + " of Heuns's")
    y_end = y + dy_dt(y)*h
    t_end = t + h
    y = y + (dy_dt(y) + dy_dt(y_end))/2*h
    print(y - tan(y))
    t = t - h
    

#specify differential equation
def dy_dt(y): 
    return (t-y)**2

#initial conditions
t = 1.0
y = 0.5

#get time step from user
h = 0.0025

t_end = 0
y_end = 0
count = 0
while(t >= 0.5025):
    count = count + 1
    print("Step " + str(count) + " of Heuns's")
    y_end = y + dy_dt(y)*h
    t_end = t + h
    y = y + (dy_dt(y) + dy_dt(y_end))/2*h
    print(y - tan(y))
    t = t - h
hf = y
    
#final values between this 200 step method and the 20 step method are
#different by about 0.001
    
#Euler method
#apply the Euler method
t = 1.0
y = 0.5
h = 0.0025
count = 0
while (t >= 0.5025):    
    count = count + 1
    print("Step " + str(count) + " of Euler's")
    print(y)
    y = y + dy_dt(y)*h
    t = t - h
ef = y
print("Relative error")
print(abs(hf - ef)) # relative error is 2.9268538299e-05


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

"""
Created on Mon Oct  1 19:22:45 2018
newtoncooling.py
4.
@author: Julian
"""

import matplotlib.pyplot as plt
from math import sin, pi

def R(T,Ts):
    return -r*(T- Ts)

def Ts(t):
    return 92 - 10*sin(2*pi*(t+3)/24)

#initialize parameters
t = 0
T = input("Input initial temperature of apartment in fahrenheit: ")


Tend = 0.0
tend = 0.0
r = 0.1
h = 0.1

#apply Heun's method
while t < 48.0:
    Tsur = Ts(t)
    tend = t + h
    Tsurend = Ts(tend)
    Tend = T + R(T,Tsurend)*h
    T = T + (R(T, Tsur) + R(Tend, Tsurend))/2.0*h
    t = t + h
    
    plt.plot(t, T, 'bo')
    plt.plot(t, Tsur, 'rx')
    
'''
a. About 95 degrees fahrenheit
b. At about 20 hours, 31 hours, and 43 hours
c. lag
d. The apartment lags by about 10 hours
'''

"""
Created on Wed Sep 26 12:48:19 2018
coldmedication.py
5.
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