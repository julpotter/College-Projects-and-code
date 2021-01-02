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

