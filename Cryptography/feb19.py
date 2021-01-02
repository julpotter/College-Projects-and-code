# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:08:49 2019

@author: Julian
"""

# The code dictionary maps 'A'->0, 'B'->1, ..., 'Z'->25, ' '->26
# The edoc dictionary is the inverse of that map
from numpy import math

code = {}
edoc = {}
N = 27
for i in range(N-1+10):
    code[chr(i+65)] = i
    edoc[i] = chr(i+65)
code[' '] = N-1
edoc[N-1] = ' '
  
# This function prints out the frequency of each character in s
def stats(s):
    c = {}
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        c[i] = 0
    for i in s:
        c[i] += 1
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        print i,"->",c[i]
        
Cipher = "SMMXHIDIFHNZWUHXMWXTMHDPWHAZFHAWHJMTQAATMHFWBZHIUJQAQWV"

