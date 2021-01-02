'''
8/29/19
Julian Potter
'''


from math import pi, sqrt

N = input("Enter the number of terms: ")

sum = 0
for i in range(1, N+1):
    sum = sum + 1./(i**2)
sum = 6.*sum
print sqrt(sum)
print pi
print "% error = ", (pi-sqrt(sum))/pi * 100
    
