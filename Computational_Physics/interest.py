'''
Julian Potter
8/30/18
A premed student invests an amount $1000 in a bank account that pays
2.5% interest per year.

'''
from math import exp

A = 1000.

a = A * (1 + (2.5)/100)**(5) #value in 5 years
b = A * (1 + (2.5)/100)**(10)#value in 10 years
c = A * (1 + (2.5)/100)**(30)#value in 30 years
