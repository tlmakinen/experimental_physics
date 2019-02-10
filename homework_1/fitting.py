#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from math import exp, sqrt, pi
import scipy.optimize as optimize
import scipy.stats

# we define this function before the rest of the code
# this can be done with a built-in function, but we
# use a custom function here as an illustrative example

def fitFunction(z, amplitude, mean, sigma):
    arg = -0.5*np.power(((z-mean)/sigma),2)
    val = amplitude*np.exp(arg)
    return val 

nTrials = 1000000
y = np.zeros(nTrials)
numbersPerTrial = 10
w = sqrt(numbersPerTrial)
# each entry is the average of the numbers generated from a uniform
# random distribution.   The result is shifted by -1/2 and scaled
# up by the sqrt of the number of numbers being averaged
for i in range(nTrials) :
    x = np.random.rand(numbersPerTrial)  - 0.5
    y[i] = w*np.average(x)
    
# histogram the data
nBins = 50
nCounts, binEdges = np.histogram(y, bins=nBins)

# There will be one more bin edge than the number of bins.
# For what follows, we are interested in the bin centers
binCenters = np.zeros(nBins)
for i in range(nBins) : binCenters[i] = 0.5*(binEdges[i+1]+binEdges[i])

# plot the generated points
ax = plt.subplot(111)
plotErrors = np.sqrt(nCounts)
plotErrors = np.minimum(plotErrors,0.9*nCounts)
plt.errorbar(binCenters,nCounts,yerr=plotErrors,fmt='o')

# fit to a gaussian function
fitErrors = np.sqrt(nCounts+1.)
initialGuess = [np.max(nCounts), 0., 1.]
fittedParameters, covariance = optimize.curve_fit(fitFunction, binCenters, nCounts, p0=initialGuess, sigma=fitErrors)
[ fittedAmplitude, fittedMean, fittedSigma ] = fittedParameters

# put the fitted curve values into an array and plot them
fittedCurve = fitFunction(binCenters, fittedAmplitude, fittedMean, fittedSigma) 
plt.plot(binCenters, fittedCurve, 'r-', linewidth=1)

ax.set_yscale("log", )#nonposx='clip')
plt.xlabel('x (arb. units)')
plt.ylabel('Number')
plt.title('Fitted Histogram Example')
yMax = 2.0*nCounts.max()
plt.axis([-2.0, 2.0, 0., yMax])
plt.grid(True)

# Get the errors on the fitted parameters and the goodness-of-fit variables
# and add them to the plot using the text() function.
errA = sqrt(covariance[0][0])
errMu = sqrt(covariance[1][1])
errSigma = sqrt(covariance[2][2])
chisq = np.sum( ((nCounts-fittedCurve) / fitErrors)**2)
ndof = nBins - 3
pValue = 1. - scipy.stats.chi2.cdf(chisq,ndof)

# comment out, since this line is not python 3.x compliant
#print "chisq=" + str(chisq) +" ndof=" + str(ndof) + " pValue=" + str(pValue)


textString = "$A={0:6.1f} \pm {1:4.1f}$ \n $\mu={2:8.3f} \pm {3:6.3f}$ \n $\sigma={4:8.3f} \pm {5:6.3f}$ ".format(
    fittedAmplitude, errA, fittedMean, errMu, fittedSigma, errSigma)

textString += "\n$\chi^2={0:5.1f}$  \n$p={1:8.5f}$".format(chisq, pValue) 

plt.text(-1.9, 0.7*yMax, textString, fontsize=16, verticalalignment='top')
#plt.text(0.7, 0.7*yMax, textString1, fontsize=16, verticalalignment='top')

plt.show()
