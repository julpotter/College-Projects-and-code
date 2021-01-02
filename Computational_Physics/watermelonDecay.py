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
