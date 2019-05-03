#first go to Tools > Manage Packages...
#Search for numpy and install,
#then search for matplotlib and install

import numpy as np
import matplotlib.pyplot as plt #sets up a pyplot graph as plt

def f(x):
    """function f takes in x then assigns y to x divided by 2 plus 3 """
    y = x**2 / 4 + 3
    return y


#sets the x axis to show -10 to 10 with .5 increments
#by creating a list of evenly spaced values at increments of .5 
t = np.arange(-15, 20, 0.5)

#plots the chart based on the range t and runs the f function for each item in range
plt.plot(t, f(t))

plt.show()