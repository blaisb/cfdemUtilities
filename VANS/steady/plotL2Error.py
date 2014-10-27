#This program makes the plot for L2 error in term of Lagrangian and Eulerian velcotiy particles in the couette Case

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

#Input file
print "R-> %s" %fname
nx, l2E = numpy.loadtxt(fname, unpack=True)

dx=2./nx

fig = plt.figure()

ax = fig.add_subplot(111) # Create plot object
#ax.plot(numpy.log(dx),numpy.log(l2E),'-o',label="L2")
ax.plot(dx,l2E,'-o')

ax.set_yscale('log')
ax.set_xscale('log')
plt.ylabel('L$^2$ Error')
plt.xlabel('$\Delta x$')
a,b = numpy.polyfit(numpy.log(dx),numpy.log(l2E),1)
ax.text(0.02,0.01, r'$\log(L^2)=%3.3f  \log(\Delta x) + %3.3f$' %(a,b), fontsize=15)

ax.grid(b=True, which='minor', color='r', linestyle='--')

ax.grid(b=True, which='major', color='k', linestyle='-')



ax.plot(numpy.log(dx),numpy.log(dx)*a+b,label="Linear regression")
print 'A = ', a

plt.savefig("./L2Error.png")

plt.show()

