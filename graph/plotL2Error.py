# Last Modified: Wed 29 Oct 2014 05:09:54 PM CET
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

#Figure size
plt.rcParams['figure.figsize'] = 10, 7

font = {#'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

plt.rc('font', **font)

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
plt.ylabel('$\Vert e \Vert$')
plt.xlabel('$\Delta x$')

# Regression
a,b = numpy.polyfit(numpy.log(dx),numpy.log(l2E),1)

if (b<0):
    ax.text(0.02,0.01, r'$\log(L^2)=%2.2f  \log(\Delta x) %2.2f$' %(a,b), fontsize=15)
else :
    ax.text(0.02,0.01, r'$\log(L^2)=%2.2f  \log(\Delta x) + %2.2f$' %(a,b), fontsize=15)

ax.grid(b=True, which='minor', color='b', linestyle='--')
ax.grid(b=True, which='major', color='b', linestyle='-') 
ax.plot(dx,l2E,'ko',label='$\Vert e_{\mathbf{u}}\Vert_{2}$')
ax.plot(dx,numpy.exp(b)*(dx)**a,'-k',label='$\log(\Vert e_{\mathbf{u}}\Vert_{2})=%3.2f  \log(\Delta x) %3.2f$' %(a,b))

ax.legend(loc=2)
print 'Slope is = \t', a

plt.savefig("./L2Error.png")
plt.show()

