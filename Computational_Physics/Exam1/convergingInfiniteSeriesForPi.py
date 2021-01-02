# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 01:41:02 2018

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

