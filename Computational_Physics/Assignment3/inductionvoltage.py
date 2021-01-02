# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:42:55 2018
sigma standard deviation
@author: Julian
"""
from math import exp

V0 = 0
gamma0 = 0


def func(t, V, gamma):
    return V0 * exp(gamma * (-1) * t)


