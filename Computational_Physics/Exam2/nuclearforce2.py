# -*- coding: utf-8 -*-
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