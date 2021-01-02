# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 00:59:38 2018
Full submission of code
@author: Julian
"""


"""
Created on Mon Sep 17 00:45:26 2018
(a)Write two lines of code that reads a line of text inputted by the user and
then reads a floating-point number from the user
@author: Julian
"""

a = raw_input("Input text: ")
s = input("Input number: ")

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 01:41:02 2018
Converging infinite series for pi
2.
@author: Julian
"""
from math import factorial, pow
from numpy import sqrt, float, pi

N = 1
m = (2 * sqrt(2)) / 9801
for k in range(N):
    s = float((factorial(4*k) * (1103 + 26390 * k)) / ((pow(factorial(k), 4)) * pow(396, (4*k))))


ms = m * s
pi2 = 1 / ms   
print(pi2)
print(pi)

O = 2
m = (2 * sqrt(2)) / 9801
for k in range(O):
    s = float((factorial(4*k) * (1103 + 26390 * k)) / ((pow(factorial(k), 4)) * pow(396, (4*k))))


ms = m * s
pi2 = 1 / ms   
print(pi2)
print(pi)

P = 5
m = (2 * sqrt(2)) / 9801
for k in range(P):
    s = float((factorial(4*k) * (1103 + 26390 * k)) / ((pow(factorial(k), 4)) * pow(396, (4*k))))


ms = m * s
pi2 = 1 / ms   
print(pi2)
print(pi)

#this formula is accurate only when N = 1


# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 05:51:54 2018
3. 
@author: Julian
"""
from numpy import genfromtxt, mean, std, histogram, arange
import matplotlib.pyplot as plt

t = genfromtxt("stars.txt")
K = []
M = []
for i in range(len(t)):
    K.append(t[i][0])
    M.append(t[i][1])

print('Mean of temperatures: ')
print(mean(K))
print('Standard deviation of temperatures: ')
print(std(K))

print('Mean of magnitude: ')
print(mean(M))
print('Standard deviation of magnitude: ')
print(std(M))


#histogram of # of stars vs temperature
plt.figure(1)
plt.hist(K)
plt.ylabel('Stars')
plt.xlabel('Temperature')

#graph resembles mean and standard deviation

#histogram of # of stars vs magnitude
plt.figure(2)
plt.hist(M)
plt.ylabel('Stars')
plt.xlabel('Magnitude')
#graph resembles mean and standard deviation

plt.figure(3)
plt.plot(K, M, 'bo')
plt.xlabel('Temperature')
plt.ylabel('Magnitude')
#the temperatures seem to be most often around 600 with the magnitude around 6
# to 10


plt.figure(4)
plt.plot(K, M, 'bo')
plt.xlabel('Temperature')
plt.ylabel('Magnitude')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.show()


# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:35:49 2018
4.
@author: Julian
"""
from numpy import sqrt

mhAB = 35 + (25 / (9.8 * 2))

print(mhAB) #max height is 36.27m
mt = sqrt((mhAB - 35) / 4.9)
d = 1/2 * 9.8 * (1 - mt)** #distance apart


# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:35:49 2018
ballAB.py
4.
@author: Julian
"""
from numpy import sqrt
import matplotlib.pyplot as plt
g = -9.8
#find maximum height of thrown balls A and B
mhAB = 35 + (25 / (9.8 * 2))

#a.
print(mhAB) #max height is 36.27m
mt = sqrt((mhAB - 35) / 4.9) #time it takes either ball to travel to max height

print(mt)
#b.
d = 5 * (1 - mt) + (1/2) * (-9.8) * (1 - mt)**2 #distance apart
print(d) #distance apart is 2.4m

#c. determine the distance between the balls over time
dt = d / 1 #distance over time
print(dt)


N = 30
t = 0
Ay = 35
By = 35
for i in range(N):
    plt.plot(t, Ay, 'ro')
    plt.plot(t, By, 'bo')
    Ay = Ay + 5*t+(g*t*t)/2
    t = t + .1
    By = By + 5*t+(g*t*t)/2


plt.figure(1)    
plt.xlabel('Time')
plt.ylabel('Position')       
plt.show()

#e.
N = 30
t = 0
Ay = 35
By = 35
d = 0
plt.figure(2)
for i in range(N):
    plt.plot(t, d, 'bo')
    Ay = Ay + 5*t+(g*t*t)/2
    t = t + .1
    By = By + 5*t+(g*t*t)/2
    d = abs(Ay - By)

plt.xlabel('Time (s)')
plt.ylabel('Distance (m)')
plt.show()

#f. The balls start together, drift apart, and then converge before
# dropping to continuously drift apart. This is expected because the
# balls are at the same vertical height at one point when one is falling
# and one is rising, but afterwards, they continuously drift apart

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:53:16 2018
hubble.py
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

data = np.loadtxt('Hubble.txt', float)
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

