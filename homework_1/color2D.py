#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

# We build a 2D function  (i.e., 2D array called A2D) by stacking 1D arrays
# on top of one another

for i in range(256) :
    X = float(i)*np.ones(256)
    for j in range(256) :
        X[j] *= float(j)
        
    # append the X array to A2D
    if i == 0 :
        A2D = X
    else :
        A2D = np.vstack((A2D,X))

fig = plt.figure()
ax = fig.add_subplot(111)

# This makes the color plot.  The origin='lower' argument
# causes the vertical coordinate to run from down to up
im = ax.imshow(A2D, origin='lower', interpolation='nearest')

# Always label your axes, providing units as appropriate
plt.xlabel('X (apples)')
plt.ylabel('Y (oranges)')
plt.title('X vs Y')

# Add a color bar, which gives the vertical range
zMax = A2D.max()
tickValues = [0., 0.25*zMax, 0.5*zMax, 0.75*zMax, zMax]
plt.colorbar(im, ticks=tickValues)

# Display the result
plt.show()

