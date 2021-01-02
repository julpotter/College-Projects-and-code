# -*- coding: utf-8 -*-
"""
4.
Created on Wed Sep 12 21:14:33 2018

@author: Julian
"""
from numpy import mean, std
import matplotlib.pyplot as plt

a = [10, 12, 15, 8, 13, 14, 19, 18, 11, 13, 7, 8, 11, 8, 12, 6, 13, 8, 6]



for i in range(len(a)):
    plt.plot(i, a[i], 'ro')
    
plt.show()    

x = mean(a)
y = std(a)
print("Mean is: " + str(x))
print("Standard deviation is: " + str(y))
#yes, 3.6 is near the square root of 11.1


    
