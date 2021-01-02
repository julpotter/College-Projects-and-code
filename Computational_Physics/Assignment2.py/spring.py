# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:37:26 2018

@author: Julian
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

#data
x = [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]
y = [45, 38, 41, 35, 31, 40, 25, 32, 36, 29, 34, 38, 26, 42, 27, 28, 27]

#initialize values
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
chi_squared = 0

#perform the sums for the fit
for value in x:
    sum_x = sum_x + value
    
for value in y:
    sum_y = sum_y + value
    
for value in x:
    sum_xx = sum_xx + value * value
    
for i in range(len(x)):
    sum_xy = sum_xy + x[i]*y[i]
    
#determine the coefficients A and B
delta = len(x)*sum_xx - sum_x*sum_x
A = (sum_xx*sum_y - sum_x*sum_xy)/delta
B = (len(x)*sum_xy - sum_x*sum_y)/delta
print("Delta value is " + str(delta))

#calculate chi-squared
sigma_y = np.std(y)
for i in range(len(y)):
    chi_squared = (chi_squared + (y[i] - A - B*x[i])**2)/sigma_y**2

print("The number of data points is N = {0:4d}".format(len(y)))
print("The value of chi-squared is {0:6.2E}".format(chi_squared))
print("The value of A is {0:6.2E} and B is {1:6.2E}".format(A,B))

sigma_A = sigma_y*np.sqrt(sum_xx/delta)
sigma_B = sigma_y*np.sqrt(len(y)/delta)


print("A = {0:4.2f} +/- {1:4.2f}, B = {2:4.2f} +/- {3:4.2f}".format(A, sigma_A, B, sigma_B))

#calculate the Pearson r coefficient
r = 0
sum_diffxy = 0
sum_xdiff_squared = 0
sum_ydiff_squared = 0
x_bar = np.mean(x)
y_bar = np.mean(y)

for i in range(len(y)):
    sum_xdiff_squared = sum_xdiff_squared + (x[i] - x_bar)**2
    sum_ydiff_squared = sum_ydiff_squared + (y[i] - y_bar)**2
    sum_diffxy = sum_diffxy + (x[i] - x_bar)*(y[i] - y_bar)
    
r = sum_diffxy/np.sqrt(sum_xdiff_squared * sum_ydiff_squared)

print("The correlation coefficient is r = {0:6.2E} +/- {1:2.2f}".format(r, np.sqrt(1-r**2)))

plt.errorbar(x,y, yerr=np.std(y), fmt='bx', label='data')
xp = np.linspace(min(x),max(x),50)
yp = A + B*xp
plt.plot(xp,yp,'r-',label='fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=2)
plt.show()