# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 12:15:18 2018
bifurcationdiagram.py
@author: Julian
"""
import matplotlib.pyplot as plt
import numpy as np
 
r = 0.96
N = 1500
x = 0.5
xlist = []
rlist = []
for r in np.arange(0.75,1,0.0005):
    x = 0.25
    for i in range(N):
        x = 4*r*x*(1-x)
        if(i>1000):
            xlist.append(x)
            rlist.append(r)
    
       

plt.plot(rlist,xlist,'rx')
plt.show()