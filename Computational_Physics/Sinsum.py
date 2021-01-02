'''
sinsum.py
v. 1 8/27/18
calculate the sine of an angle from the series expansion
'''

# Import factorial from numpy
from numpy import math

# Initialization of variables
# Get the angle from the user
x = input("Enter the angle in degrees: ")
# convert angle to radians
x = x * math.pi / 180
# get the number of terms to compute from user
N = input("Enter number of terms to compute: ")
sum = 0

#create the loop for our calculation
for j in range (0, N+1):
    sum = sum + (-1)**j*x**(2*j+1)/math.factorial(2*j+1)


#print out result
print "sin(x) = ", sum

print "Percent error = ", math.fabs((math.sin(x)) - sum) / (math.sin(x)) * 100
