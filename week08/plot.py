# This program plots the function y = x^2
# Author: Joanna Kelly


import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()
