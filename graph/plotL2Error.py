# Last Modified: Mon 27 Oct 2014 02:46:01 PM CET
# This program makes the log-log plot for L2 error and outputs the order of convergence (slope) as a printed output
# Graphic is in better shape now

# Author : Bruno Blais
# Last modified : December 3rd

#Python imports
import os
import sys
import math
import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FormatStrFormatter
import pylab

#===================
# MAIN PROGRAM
#===================
fname = sys.argv[1]

# Input file
print "R-> %s" %fname
nx, l2E = numpy.loadtxt(fname, unpack=True)

#Set dx as a function of number of points
dx=2./nx

# Initiate the figure
fig = plt.figure()

# Create plotting object
ax = fig.add_subplot(111) 
ax.plot(dx,l2E,'o')
ax.set_yscale('log')
ax.set_xscale('log')

# Labeling
plt.ylabel('L$^2$ Error')
plt.xlabel('$\Delta x$')

# Regression
a,b = numpy.polyfit(numpy.log(dx),numpy.log(l2E),1)

if (b<0):
    ax.text(0.02,0.01, r'$\log(L^2)=%2.2f  \log(\Delta x) %2.2f$' %(a,b), fontsize=15)
else :
    ax.text(0.02,0.01, r'$\log(L^2)=%2.2f  \log(\Delta x) + %2.2f$' %(a,b), fontsize=15)

ax.grid(b=True, which='minor', color='r', linestyle='--')
ax.grid(b=True, which='major', color='k', linestyle='-') 
ax.plot(dx,numpy.exp(b) * dx**a,label="Linear regression")

print 'Slope is = \t', a

plt.savefig("./L2Error.png")
plt.show()

