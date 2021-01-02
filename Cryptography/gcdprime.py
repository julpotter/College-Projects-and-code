# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:46:00 2019

@author: Julian
find greatest common factors of N
"""
import math
N = 5612592691460157028488501867482051458587407740355339131559497670427820545466264932268319464911726122036348856881906213034456112079790167
Ns = math.sqrt(N)
'''
def gcd(a,b):
    while b!=0:
        print a
        a, b = b, a%b
    return a

gcd(N, Ns)
1 low<sqrt(N)<N high
s = (low+high)/2
while low<high-1:
    if s**>N:
        high = (low+high)/2
    else:
        low = (low+high)/2
'''

s
low = 1
high = 16
s = (low+high)/2

while low<high-1:
    s = (low+high)/2
    if s*s>N:
        high = s
    else:
        low = s
        
print s
        
