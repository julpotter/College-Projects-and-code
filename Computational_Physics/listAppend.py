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
