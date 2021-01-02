# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:35:49 2018
MCoptimize.py
use Monte Carlo methods to find a curve fit
@author: Julian
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

#Experimental data. Either read in a file or use the created data below
xMeas = np.random.uniform(0.5,3.0,size=20)
yTrue = 1.5/xMeas
yError = 0.1
yMeas = yTrue + np.random.normal(scale=yError, size=np.size(yTrue))

plt.figure(1)
plt.errorbar(xMeas, yMeas, yerr = yError, fmt = 'bo', ecolor = 'b')
plt.xlabel('Time')
plt.ylabel('Measured value')
plt.xlim(0.4,3.0)
plt.show()

def f_decay(x,a,b):
    return a*x**(b)

vGuess = [2.0,-2.0]
vPars,aCov = optimize.curve_fit(f_decay,xMeas,yMeas,vGuess)
print(vPars)

xFine = np.linspace(0.4,3.0,100)
plt.figure(2)
plt.errorbar(xMeas,yMeas,yerr=yError,lw=0,elinewidth=1,ecolor='b',fmt='bo')
plt.plot(xFine,f_decay(xFine,*vPars),'g-',lw=1) #Fitter curve
plt.plot(xFine,f_decay(xFine,1.5,-1.0),'r-',lw=1)
plt.title("Fitted curve(green) and true curve(red)")
plt.show()

#apply Monte Carlo simulation for curve fitting
nTrials = 4000 #number of Monte Carlo trials
aFitPars = np.array([]) #store parameters from each trial

for iTrial in range(nTrials):
    xTrial = np.random.uniform(0.5,3.0, size = np.size(xMeas))
    yGen = f_decay(xTrial,1.5,-1.0)
    yTrial = yGen + np.random.normal(scale = yError, size= np.size(yGen))
    
    try:
        vTrial,aCova=optimize.curve_fit(f_decay,xTrial,yTrial,vGuess)
    except:
        dumdum = 1
        continue
    
#stack the trial outcome parameters on the running sample:
    if np.size(aFitPars)<1:
        aFitPars = np.copy(vTrial)
    else:
        aFitPars = np.vstack((aFitPars,vTrial))
    

plt.figure(5)
plt.scatter(aFitPars[:,0],aFitPars[:,1],alpha = 0.5, edgecolor = 'none')
    
np.shape(aFitPars)
#print(np.median(aFitPars[:,1]))
#print(np.std(aFitPars[:,1]))
print("Mean = {0:8.6f} +/- {1:8.6f}".format(np.median(aFitPars[:,1]),np.std(aFitPars[:,1])))

plt.figure(3)
plt.hist(aFitPars[:,1],bins=150)
plt.xlabel('Power Law index b')
plt.ylabel('N(b)')
plt.show()

plt.figure(4)
plt.hist(aFitPars[:,0],bins=50)
plt.xlabel('Power Law index a')
plt.ylabel('N(a)')



#Multi axis histogram
fig = plt.figure(figsize = (6,6))
grid = plt.GridSpec(4,4, hspace=0.4, wspace=0.5)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1,0], xticklabels = [], sharey = main_ax)
y_hist = fig.add_subplot(grid[:-1,0], xticklabels = [], sharey = main_ax)
x_hist = fig.add_subplot(grid[-1,1:], yticklabels =[], sharex = main_ax)

#scatter point on the main axes
main_ax.plot(aFitPars[:,0],aFitPars[:,1],'ok', markersize=2, alpha = 0.2)

#put histograms on attached axes
x_hist.hist(aFitPars[:,0], 50, histtype = 'stepfilled', orientation = 'vertical', color = 'gray')
x_hist.invert_yaxis()

y_hist.hist(aFitPars[:,1], 50, histtype = 'stepfilled', orientation = 'horizontal', color = 'gray')
y_hist.invert_xaxis()
plt.show()
