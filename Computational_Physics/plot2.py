
from __future__ import print
import matplotlib.pyplot as plt

g = 9.81
t0 = 0
y0 = 1.5 # initial height
v0 = float(input("Enter the initial velocity v0 :"))

#use lists to save position and time
y = []
t = []

ycalc = 0
tcalc = 0

#create a loop to populate our lists with values
while(ycalc >= 0):
    ycalc = y0 + v0*tcalc - 1/2.*g*tcalc**
    y.append(ycalc)
    t.append(tcalc)
    print "Height is {0:5.2f} and time is {1:5.2f}".format(ycalc,tcalc)
    tcalc = tcalc + 0.05 #increment

print "The maximum height reach is ", max(y)

#graph our results
plt.plot(t,y, 'r^')
plt.xlabel("Time t (s)")
plt.ylabel('Height y (m)')
plt.show()
