'''
Julian Potter
8/31/18
5.
'''

from math import pow, factorial, sin

x = 45 #angle
N = 21
s = 0
for j in range(0, N):
    s = pow((-1), j)*(pow(x, (2*j+1)))/factorial(2*j+1)

#then compute fractional error
pe = (s - sin(x)/sin(x))*100
print "Percent error: " + str(pe) + "%"

