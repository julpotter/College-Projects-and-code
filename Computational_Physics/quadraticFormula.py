'''
Julian Potter
8/31/18
4.
'''

a = 2; b = 1; c = 2
from math import sqrt
if b*b-4*a*c < 0:
    print "undefined"
else:
    q = sqrt(b*b - 4*a*c)
    x1 = (-b + q)/(2*a) #add parentheses to 2*a
    x2 = (-b - q)/(2*a) #add parentheses to 2*a
    print x1, x2

