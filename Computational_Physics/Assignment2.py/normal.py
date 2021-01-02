# -*- coding: utf-8 -*-
"""
3.
Created on Wed Sep 12 20:21:57 2018

@author: Julian
"""
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

mu = 0
sig = 0.5
x = -5


normal(sig, mu)

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sig * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sig**2) ), linewidth=2, color='r')

plt.show()










