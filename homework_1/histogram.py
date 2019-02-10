#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# fill an array x with 10000 random numbers that are normally
# distributed with the indicated mean and standard deviation
nTrials, mu, sigma = 1000, 100, 15
x = mu + sigma*np.random.randn(nTrials)

# the histogram of the data
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
n, bins, patches = plt.hist(x, 50, facecolor='green', alpha=0.75)

# add a curve that describes the data
dx = bins[1] - bins[0]
y = nTrials*dx*mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Decay Rate  (counts/min)')
plt.ylabel('Number')
plt.title('Histogram of Count Rate: $\mu=100,\ \sigma=15$')
yMax = 1.1*n.max()
plt.axis([40, 160, 0, yMax])
plt.grid(True)

plt.show()
