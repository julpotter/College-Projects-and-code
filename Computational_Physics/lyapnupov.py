# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 12:29:59 2018
lyapnupov.py
@author: Julian
"""
from numpy import arange, fabs, log
import matplotlib.pyplot as plt
#initial conditions
rlist = []
x = 0
dx = 0
lamblist = []
sum = 0
n = 10000

for r in arange(0.01,1.0,0.001):
    x = 0.5
    for i in arange(0,n):
        dx = 4*r*(1-2*x)
        if i>5000:
            sum += log(fabs(dx))
        x = 4*r*x*(1-x)
    lamblist.append(sum/n/log(2))
    rlist.append(r)
    
    sum = 0 #reinitialize

    
plt.plot(rlist,lamblist)
plt.ylim(-1,1)
plt.grid(which = 'both')
plt.show()