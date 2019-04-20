# -*- coding: utf-8 -*- 

'''
# astroid
http://jwilson.coe.uga.edu/EMAT6680Fa2014/Gieseking/Exploration%2010/Parametric%20Equations.html
'''

import matplotlib.pyplot as plt
import numpy as np
from curbrac import curbrac

# figure size and dpi
dbl_width   = 1000.0
dbl_height  = 600.0
dbl_dpi     = 100.0

# line width and colour for the epllise
lw = 2
color='royalblue'

r1 = 5.0    # radius 1
r2 = 20.0   # radius 2

theta = np.linspace(0, 2.0 * np.pi, 101)

# calculate the points of the two astroids
x1 = r1 * (np.sin(theta) ** 3)
y1 = r1 * (np.cos(theta) ** 3)
x2 = r2 * (np.sin(theta) ** 3)
y2 = r2 * (np.cos(theta) ** 3)

# fontdict for axis titles
font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 12,
        }

str_title1 = 'Example: Anti-Clockwise for a a pair of concentrate astroid'
str_title2 = 'Example: Clockwise for a a pair of concentrate astroid'

fig, axes = plt.subplots(2, 1, figsize=(dbl_width / dbl_dpi, dbl_width / dbl_dpi), dpi=dbl_dpi)

axes[0].plot(x1, y1, lw=lw, color=color)
axes[0].plot(x2, y2, lw=lw, color=color)
axes[1].plot(x1, y1, lw=lw, color=color)
axes[1].plot(x2, y2, lw=lw, color=color)

axes[0].set_aspect('equal', 'box')
axes[0].grid(color='lightgray', linestyle='--')
axes[0].set_title(str_title1, fontdict=font)
axes[1].set_aspect('equal', 'box')
axes[1].grid(color='lightgray', linestyle='--')
axes[1].set_title(str_title2, fontdict=font)

# bracket coefficient
k_r = 0.1

# points for the brackets
phi = np.linspace(0, 2.0 * np.pi, 9)

x1 = r1 * (np.sin(phi) ** 3)
y1 = r1 * (np.cos(phi) ** 3)
x2 = r2 * (np.sin(phi) ** 3)
y2 = r2 * (np.cos(phi) ** 3)

# fontdict for the brackets
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'style': 'normal',
        'size': 6,
        }

# bracket line width and colour
lw = 2
color = 'r'

for i in range(0, len(x1)):

    p1 = [x1[i], y1[i]]
    p2 = [x2[i], y2[i]]

    str_text = 'Astroid\nanti-clockwise'

    theta, pt = curbrac(axes[0], p1, p2, k_r, str_text=str_text, color=color, lw=lw, int_line_num=2, fontdict=font)

for i in range(0, len(x1)):

    p1 = [x2[i], y2[i]]
    p2 = [x1[i], y1[i]]

    str_text = 'Astroid\nclockwise'

    theta, pt = curbrac(axes[1], p1, p2, k_r, str_text=str_text, color=color, lw=lw, int_line_num=2, fontdict=font)

plt.show()