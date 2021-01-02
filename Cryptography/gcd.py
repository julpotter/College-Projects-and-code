# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:46:00 2019

@author: Julian
"""

def gcd(a,b):
    while b!=0:
        print a
        a, b = b, a%b
    return a


