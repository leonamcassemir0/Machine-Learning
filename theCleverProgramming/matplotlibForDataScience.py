import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 100)
figure = plt.figure()
"""
plt.plot(x1, np.sin(x1), '-')
plt.plot(x1, np.cos(x1), '--')
plt.show()  # to show the plot


# create the first of two panels and set current axis
plt.subplot(2, 1, 1)   # (rows, columns, panel number)
plt.plot(x1, np.sin(x1))


# create the second of two panels and set current axis
plt.subplot(2, 1, 2)   # (rows, columns, panel number)
plt.plot(x1, np.cos(x1))
plt.show()
"""

plt.plot([0, 2, 4, 6])
plt.ylabel('Numbers')
plt.show()
