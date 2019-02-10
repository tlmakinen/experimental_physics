#!/usr/bin/env python

# Usage: python simpleGraphError.py data.txt 

# Read a set of x, y, error points from a text file.
# Plot them using the errorbar function

import numpy
import matplotlib.pyplot as plt
import sys

# the sys.argv array contains the command line arguments
# sys.argv[0] will be the name of the script being run
# here we want the first argument, which is the name
# of the file that contains our data
fName = sys.argv[1]

# open the data file and read it in
f = open(fName)
lines = f.readlines()

# remove the first line, which contains the column label data
# we do this the pythonic way
lines[0:1] = []

# create empty numpy arrays to hold the data points
x = numpy.array([])
y = numpy.array([])
yErrors = numpy.array([])

# loop through the lines that have been read in,
# split them into x, y, and yErr values and append
# those values to the arrays created above
# Programming notes:
#  i) each line in the lines list is a string
# ii) the split() function breaks each line into three
#     three smaller strings, each of which represents
#     a numerical value
# iii) the string representations of the numbers are converted 
#     to floating point numbers using the float() function
for line in lines :
    splitLine = line.split()
    x = numpy.append(x, float(splitLine[0]))
    y = numpy.append(y, float(splitLine[1]))
    yErrors = numpy.append(yErrors, float(splitLine[2]))

    
# Create a figure.  Let matplotlib figure out the range
plt.figure(1)
plt.plot(x, y, 'bo')
plt.errorbar(x, y, yerr=yErrors, fmt=None)

# Draw a straight red line over the data.
xl = [0., 10.]
yl = [0., 100.]
plt.plot(xl, yl, 'r-', linewidth=1)

# be sure to always add a title, and to label the
# x and y axes, including units
plt.title("x vs. y")
plt.xlabel("x  (m)")
plt.ylabel("y (m)")

# display the plot
plt.show()










