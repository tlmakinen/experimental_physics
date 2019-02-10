import numpy
import matplotlib.pyplot as plt

# enter the data as python lists 
x = [ 0., 10., 20., 30., 40. ]
force = [ 10., 25., 35., 60., 80.]

#create a figure and set limits on the axes
plt.figure(1)
plt.xlim(0.,50.)
plt.ylim(0.,100.)

# plot the force points vs. the x points
# 'bo' ==> use blue circle markers
plt.plot(x, force, 'bo', label='1st Force')

# add a second plot where the force values 75% as large.  
force2 = force
for i in range(len(force)) : force2[i] *= 0.75

# Use red crosses.   Make the marker size a bit larger
plt.plot(x, force2, 'r+', markersize=12, label='2nd Force')

# draw the legend, the numpoints argument is needed since
# legend() defaults to 2.
plt.legend(numpoints=1)

# be sure to always add a title, and to label the
# x and y axes, including units
plt.title("Force vs. Position")
plt.xlabel("x  (m)")
plt.ylabel("Force (N)")

# display the plot
plt.show()










