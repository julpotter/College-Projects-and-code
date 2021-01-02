# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 22:40:21 2018
SelfOrganizedCriticality.py
Drop a single grain of sand at a random
location on the grid
l Random (x,y)
l Update model at that point: Z(x,y) ‡ Z(x,y)+1
l If Z(x,y) > Threshold, spark an avalanche
l Threshold = 3
@author: Julian
"""
from numpy import random
xpos = []
ypos = []
N = 20
#populate grid
for i in range(N):
    xpos.append(0)
    ypos.append(0)
#Chose Random (x,y) position on grid
x = random.randint(0,N)
y = random.randint(0,N)
#Increment that cell  Z(x,y) -> Z(x,y)+1
xpos[x]+=1
ypos[y]+=1