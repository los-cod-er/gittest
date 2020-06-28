# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

def binary_entropy(p):
    return -(p * np.log2(p))

plt.figure()
p1 = np.linspace(0, 1, 150)
entropy = binary_entropy(p1)
plt.plot(p1, entropy)
plt.xlabel('$p1$')
plt.ylabel('-plog(p)')
plt.show()
