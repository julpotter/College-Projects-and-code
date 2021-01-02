# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:40:08 2018

@author: Julian
"""

#E2-1
import matplotlib.pyplot as plt
from math import sin, pi

def R(T,Ts):
    return -r*(T- Ts)

def Ts(t):
    return 92 - 10*sin(2*pi*(t+3)/24)

#initialize parameters
t = 0
T = 68  #in Fahrenheit

Tend = 0.0
tend = 0.0
r = 0.15
h = 0.1
Tsur = 25

#apply Heun's method
while t < 48.0:
    tend = t + h
    Tend = T + R(T,Tsur)*h
    T = T + (R(T, Tsur) + R(Tend, Tsur))/2.0*h
    t = t + h
    
    plt.plot(t, T, 'bo')
    plt.plot(t, Tsur, 'rx')

#E2-1-c
import matplotlib.pyplot as plt
from math import sin

def R(T,Ts):
    return -r*(T- Ts)

def Ts(t):
    return 20*(1+0.5*sin(t/8))

#initialize parameters
t = 0 #6am
T = 68  #in Fahrenheit

Tend = 0.0
tend = 0.0
r = 0.15
h = 0.1

#apply Heun's method
while t < 144.0:
    Tsur = Ts(t)
    tend = t + h
    Tsurend = Ts(tend)
    Tend = T + R(T,Tsurend)*h
    T = T + (R(T, Tsur) + R(Tend, Tsurend))/2.0*h
    t = t + h
    
    plt.plot(t, T, 'bo')
    plt.plot(t, Tsur, 'rx')
#E2-2
"""
Created on Sat Oct 20 18:13:47 2018
nuclearforce.py
@author: Julian
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from sympy import diff
from math import sqrt, exp

#Experimental data. Either read in a file or use the created data below

rMeas = [2.9019,3.26463,3.62737,3.99011,4.35285]
UMeas = [-145.299,-111.289,-62.1917,-46.7048,-32.3581]
sigUMeas = [7.73623,8.5017,7.88238,7.46152,8.21121]
Error = 0.1
c = 299792458E15 #speed of light, fm/s


#find the value of g
def findg(U,r):
    sqrt(-U * (r/exp(-r/diff(r))))
    
#find the value of m
def findm(r):
    197.3/(diff(r) * c**2)
    
    
def funcU(g,r):
    return -g**2 * (exp(-r/diff(r))/r)

vGuess = [2.0,-2.0]
vPars,aCov = optimize.curve_fit(funcU,UMeas,rMeas,vGuess)
print(vPars)

xFine = np.linspace(0.4,3.0,100)
plt.figure(2)
plt.plot(xFine,funcU(xFine,*vPars),'g-',lw=1) #Fitter curve
plt.plot(xFine,funcU(xFine,1.5,-1.0),'r-',lw=1)
plt.title("Fitted curve(green) and true curve(red)")
plt.show()
#E2-3
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


"""
Created on Oct 21
golfballtrajectory4i.py
model golfball trajectory
@author: Julian
"""
#E2-4-i
from numpy import array, cross
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi, exp

done = 0 #for a repeating loop

#define the drag coefficient function
def k_D(v):
    if v<= 14:
        return 0.5
    if v>14:
        return 7.0/v
#define euler algorithm
def euler(vx,vy,vz,phi):
    #initial conditions
    x = 0
    y = 0
    z = 1.8 # release height in meters
    t = 0
    h= 0.0001 # time step
    k_L = 4.0E-4
    omega = 0
    g = 9.81
    
    while x<=18.44: #distance to home base from pitcher's mound
        X.append(x)
        Y.append(y)
        Z.append(z)
        
        
        v = sqrt(vx**2+vy**2+vz**2)
        #calculate acceleration components
        ax = -k_D(v)*v*vx+k_L*(vz*omega*sin(phi)-vy*omega*cos(phi))
        az = -k_D(v)*v*vz-k_L*vx*omega*sin(phi)-g
        #apply Euler algorithm
        vx = vx+ax*h
        vy = 0
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
    
v = 70.0
phi = 225.8*pi/180.


theta = 9.0*pi/180.0 #angle from horizontal

vx = v*cos(theta)
vy = 0
vz = v*sin(theta)

euler(vx,vy,vz,phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.plot(X,Y,zs = Z, zdir = 'z')

#E2-4-ii
from numpy import array, cross
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi, exp

done = 0 #for a repeating loop

#define the drag coefficient function
def k_D(v):
    if v<= 14:
        return 0.5
    if v>14:
        return 7.0/v
#define euler algorithm
def euler(vx,vy,vz,phi):
    #initial conditions
    x = 0
    y = 0
    z = 1.8 # release height in meters
    t = 0
    h= 0.0001 # time step
    k_L = 4.0E-4
    omega = 0.25*2*pi
    g = 9.81
    
    while x<=18.44: #distance to home base from pitcher's mound
        X.append(x)
        Y.append(y)
        Z.append(z)
        
        
        v = sqrt(vx**2+vy**2+vz**2)
        #calculate acceleration components
        ax = -k_D(v)*v*vx+k_L*(vz*omega*sin(phi)-vy*omega*cos(phi))
        az = -k_D(v)*v*vz-k_L*vx*omega*sin(phi)-g
        #apply Euler algorithm
        vx = vx+ax*h
        vy = 0
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
    
v = 70.0
phi = 225.8*pi/180.


theta = 9.0*pi/180.0 #angle from horizontal

vx = v*cos(theta)
vy = 0
vz = v*sin(theta)

euler(vx,vy,vz,phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.plot(X,Y,zs = Z, zdir = 'z')

#E2-4-iii
from numpy import array, cross
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from math import sin, cos, sqrt, pi, exp

done = 0 #for a repeating loop

#define the drag coefficient function
def k_D(v):
    if v<= 14:
        return 0.5
    if v>14:
        return 7.0/v
#define euler algorithm
def euler(vx,vy,vz,phi):
    #initial conditions
    x = 0
    y = 0
    z = 1.8 # release height in meters
    t = 0
    h= 0.0001 # time step
    k_L = 4.0E-4
    omega = 0.25*2*pi
    g = 9.81
    
    while x<=18.44: #distance to home base from pitcher's mound
        X.append(x)
        Y.append(y)
        Z.append(z)
        
        
        v = sqrt(vx**2+vy**2+vz**2)
        #calculate acceleration components
        ax = -k_D(v)*v*vx+k_L*(vz*omega*sin(phi)-vy*omega*cos(phi))
        az = -k_D(v)*v*vz-k_L*vx*omega*sin(phi)-g
        #apply Euler algorithm
        vx = vx+ax*h
        vy = 0
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
    
v = 70.0
phi = 225.8*pi/180.


theta = 9.0*pi/180.0 #angle from horizontal

vx = v*cos(theta)
vy = 0
vz = v*sin(theta)

euler(vx,vy,vz,phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.plot(X,Y,zs = Z, zdir = 'z')