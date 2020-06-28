# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:39:15 2020

@author: 13988

pri

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) *np.cos(x)

plt.imshow(z, origin = 'lower', extent=[0,5,0,5],cmap='viridis')
plt.colorbar();             
        
            
        
        
    