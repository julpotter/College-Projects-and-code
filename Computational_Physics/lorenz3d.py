# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:27:31 2018
lorenz3d.py
@author: Julian
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#define lorenz equations
def lorenz(x,y,z, s = 10, r = 28, b = 2.667):
    x_dot = s*(y-x)
    y_dot = r*x-y-x*z
    z_dot = x*y-b*z
    return x_dot,y_dot,z_dot

#step size and count 
dt = 0.01
stepCnt = 10000

#create some lists for storing calculated values but we need 1 more for initial value
xs = np.empty((stepCnt +1,))
ys = np.empty((stepCnt +1,))
zs = np.empty((stepCnt +1,))

#set initial values
xs[0],ys[0],zs[0] = (0.,1.,1.05)

#step through time ala Euler
for i in np.arange(stepCnt):
    #derivatives
    x_dot,y_dot,z_dot = lorenz(xs[i],ys[i],zs[i])
    xs[i+1] = xs[i] + (x_dot*dt)
    ys[i+1] = ys[i] + (y_dot*dt)
    zs[i+1] = zs[i] + (z_dot*dt)
    
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs,ys,zs)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.show()