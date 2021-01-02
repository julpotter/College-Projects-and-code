

import numpy as np
import matplotlib.pyplot as plt

#set up x-axis values
x = np.linspace(0,20,1000)

#x = np.arange(0,20,0.001)

y1 = np.log10(x)
y2 = 0.01*x**
y3 = 0.9*np.sin(x)


#plot
plt.plot(x,y1, 'g-', label='y1')
plt.plot(x,y1, 'r-', label='y2')
plt.plot(x,y1, 'bo', label='y3')
plt.plot(x, y1+y2+y3, 'c^', label='sum')

plt.legend(loc=2)
plt.show()

