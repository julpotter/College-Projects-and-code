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