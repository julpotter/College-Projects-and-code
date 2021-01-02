'''
Julian Potter
8/30/2018

1.

Can a newborn baby in the US expect to live for one billion seconds?

a = average global life-expectancy in years
d = in days
h = in hours
m = in minutes
s = in seconds
'''

a = 70

d = a*365
h = d*24
m = h*60
s = m*60

# running the code produces 2207520000, over 2.2 billion seconds



'''
Julian Potter
8/30/18
A premed student invests an amount $1000 in a bank account that pays
2.5% interest per year.

2.

'''
from math import exp

A = 1000.

a = A * (1 + (2.5)/100)**(5) #value in 5 years
b = A * (1 + (2.5)/100)**(10)#value in 10 years
c = A * (1 + (2.5)/100)**(30)#value in 30 years



'''
Julian Potter
8/30/18

3. Code correction
'''

V0 = 3
t = 2
a = 2
x = V0*t + (1./2)*a*t**2 #capitalize V, add decimal to 1/2
print x #print x instead of a



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



'''
Julian Potter
8/31/18
6.
'''

a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c #[1, 3, 5, 7, 11, 13, 17]
b[0] = -1 #[-1, 17]
print b
d = [e+1 for e in a] #add +1 to all elements of a
print d #[2, 4, 6, 8, 12]
d.append(b[0] + 1) #[2, 4, 6, 8, 0]
d.append(b[-1] + 1)#[2, 4, 6, 8, 0, 18]
print d
print d[-2] #0



'''
Julian Potter
8/31/18

7.

You can't resist a sale on watermelons at the supermarket so you buy 100 pounds of them.
Watermelons are 99% water. Every day a pound of water dries away from the watermelons.
A curious physics major wants to know when the watermelons will be 98% water and how
much the watermelons will weigh then. Write a Python program that tells you the weight and
water content of the watermelons each day for 100 days. From your program, determine
when the watermelons are 98% water and how much they weigh then.
'''
w = 100 #total weight of watermelon in pounds
wa = 99 #toal weight and percent of water in pounds
wnd = 1 #nondecaying weight

for i in range(1, 100):
wa = wa - 1
w = wa + wnd
print "Water: " + str(wa) + "% ; Weight: " + str(w) #Water: 98% ; Weight: 99 pounds



'''
Julian Potter
8/31/18

8.
An unsolved conjecture posed by Luthar Collatz in 1937 states the following: Take any natural
number n. If n is even, divide it by 2 to get n / 2, if n is odd multiply it by 3 and add 1 to
obtain 3n + 1. Repeat the process indefinitely. The conjecture is that no matter what number
you start with, you will always eventually reach 1. Write a Python program that calculates
the first 20 iterates for a user-specified natural number n. Such sequences are called
hailstone sequences because the values typically rise and fall analogously to a hailstone
inside a cloud. While a hailstone eventually becomes so heavy that it falls to ground, every
starting positive integer ever tested has produced a hailstone sequence that eventually drops
down to the number 1 and then "bounces" into the small loop 4, 2, 1, .... 
'''

n = input("Select natural number to start with: ")
print n
for i in range(0, 20):
if n%2 == 0:
n = n/2
print n
if n%2 != 0:
n = n*3 + 1
print n