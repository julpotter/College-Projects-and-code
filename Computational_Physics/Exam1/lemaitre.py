"""
Created on Wed Sep 26 14:53:16 2018
lemaitre.py
5.
One of the greatest discoveries of the 20th century is that of the expanding universe, which is
attributed to Edwin Hubble (1929). What is not widely known is that the original treatise by
Georges Lemaître (1927) contained a rich fusion of both theory and observation. The French
paper was meticulously censored when printed in English: All discussion of radial velocities
and distances (and the very first empirical determination of the “Hubble constant” H) were
omitted. You will explore the quality of the data of both Hubble and Lemaître and decide
which data and conclusions were better.

@author: Julian
"""



import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.loadtxt('Lemaitre.txt', float)
t = data[:,0]
y = data[:,1]
#ysigma = data[:,2]

print(np.mean(y))
print(np.median(y))

#give initial parameters 
A0,B0,C0,omega0,tau0 = 19.712,0.316,18.9757,11.0432,12.95

#specify the function we wish to fit
def func(t,A,B,C,omega,tau):
    return A*(1+B*np.cos(omega*t))*np.exp(-t**2/(2*tau**2))+C

#now we fit the curve
popt,pcov = curve_fit(func,t,y,p0 = [A0,B0,C0,omega0,tau0])
perr = np.sqrt(np.diag(pcov)) #computes one standard deviation errors on the
#fitted parameters

print("A = {0:6.4f} +/- {1:6.4f}, B = {2:6.4f} +/- {3:6.4f}, A = {4:6.4f} +/- {5:6.4f}".
      format(popt[0],perr[0],popt[1],perr[1],popt[2],perr[2]))
print("omega = {0:6.4f} +/- {1:6.4f}, tau = {2:6.4f} +/- {3:6.4f}".format(popt[3], perr[3], popt[4], perr[4]))


#plot data and fit
plt.errorbar(t,y, fmt = 'bo',ecolor='r')
plt.plot(t,func(t,*popt), 'r-', label='fit')
plt.show()

#b. a. Number of data points = 24
print(len(t))

