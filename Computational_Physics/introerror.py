# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:45:34 2018

@author: Julian
"""

import matplotlib.pyplot as plt
from numpy.random import *
from matplotlib.colors import LogNorm
from numpy import arange, mean, std, min, max, sqrt, meshgrid, linspace, vstack
from scipy.stats import gaussian_kde

#measured values
#length = 3.1 +/- 0.1
#w = 2.5 +/- 0.04
#area A= l*w

avg_len = 3.1
std_len = 0.1
avg_wid = 2.5
std_wid = 0.04

length = []
width = []
area = []

N = 10000 # number of trials
for i in range(N):
    len_t = normal(avg_len, std_len)
    wid_t = normal(avg_wid, std_wid)
    area_t = len_t*wid_t
    
    length = length + [len_t]
    width = width + [wid_t]
    area = area + [area_t]

#plot the histogram
plt.figure(1)
plt.hist(area, bins=arange(0,10,0.1))
plt.show()
plt.figure(2)
plt.scatter(length,width,alpha=0.5)
plt.show()

print(mean(area))
print(std(area))

plt.figure(3)
plt.hist2d(length, width, bins=20, normed=LogNorm(), cmap='Blues')
plt.colorbar()
plt.show()


data = vstack([length, width])
kde = gaussian_kde(data)

#evaluate on a rectangular grid

xgrid = linspace(2.8,3.4,80)
ygrid = linspace(2.2,2.8,80)
Xgrid,Ygrid = meshgrid(xgrid,ygrid)
Z = kde.evaluate(vstack([Xgrid.ravel(),Ygrid.ravel()]))
#plot results as an image
plt.figure(4)
plt.imshow(Z.reshape(Xgrid.shape), origin='lower', aspect='auto',extent = [2.8,3.4,2.2,2.8],cmap='Reds')
cb = plt.colorbar()
cb.set_label("Density")
plt.show()


for i in range(N):
    len_t = normal(avg_len, std_len*2)
    wid_t = normal(avg_wid, std_wid*2)
    area_t = len_t*wid_t
    
    length = length + [len_t]
    width = width + [wid_t]
    area = area + [area_t]
    
plt.figure(1)
plt.hist(area, bins=arange(0,10,0.1))
plt.show()
plt.figure(2)
plt.scatter(length,width,alpha=0.5)
plt.show()

print(mean(area))
print(std(area))

plt.figure(4)
plt.hist2d(length, width, bins=20, normed=LogNorm(), cmap='Blues')
plt.colorbar()
plt.show()
plt.show(plt.scatter(length,width,alpha=0.5), plt.scatter(length,width,alpha=0.2))
