# This program makes the plot for L2 error of two series of data 

# Author : Bruno Blais

#Python imports
import os
import sys
import math
import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FormatStrFormatter
import pylab
from scipy import stats
from matplotlib import rcParams


# User parameter
outputPDF=False
showGraphic=True


# Modify font of the graphic
font = {'weight' : 'normal',
        'size'   : 18}
plt.rc('font', **font)
plt.rcParams['legend.numpoints'] = 1
params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 28,
             'legend.fontsize': 17,
             'xtick.labelsize': 15,
             'ytick.labelsize': 15,
             'text.usetex': True,
             }
plt.rcParams.update(params)


#================================
# FUNCTIONS
#================================

def rsquared(x, y):
    """ Return R^2 where x and y are array-like."""
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return r_value**2

#================================
# MAIN PROGRAM
#================================

fname = sys.argv[1]

#Input file
print "R-> %s" %fname
nx, uL2E, pL2E = numpy.loadtxt(fname, unpack=True)

dx=1./nx
fig = plt.figure()

ax = fig.add_subplot(111) # Create plot object
ax.plot(dx,uL2E,'ko')
ax.plot(dx,pL2E,'ks')

ax.set_yscale('log')
ax.set_xscale('log')

plt.ylabel('$\Vert e \Vert_2 $')
plt.xlabel('$\Delta x$')

# Linear regression
a,b = numpy.polyfit(numpy.log(dx),numpy.log(uL2E),1)
a2,b2 = numpy.polyfit(numpy.log(dx),numpy.log(pL2E),1)


ax.grid(b=True, which='minor', color='grey', linestyle='--')

ax.grid(b=True, which='major', color='k', linestyle='-')

plt.xlim([0.001,0.1])

ax.plot(dx,uL2E,'ko',label='$\Vert e_{\mathbf{u}}\Vert_{2}$')
ax.plot(dx,pL2E,'ks',label='$\Vert e_{p}\Vert_{2}$')

ax.plot(dx,numpy.exp(b)*dx**a,'-k',label='$\Vert e_{\mathbf{u}}\Vert_{2}=%3.2f  \Delta x^{%3.2f}$' %(numpy.exp(b),a))
ax.plot(dx,numpy.exp(b2)*dx**a2,'--k',label='$\Vert e_{p}\Vert_{2}=%3.2f  \Delta x^{%3.2f}$' %(numpy.exp(b2),a2))

ax.legend(loc=2)

print 'A vel    = ', a
print 'A pres   = ', a2
print 'R^2 vel  = ', rsquared(numpy.log(dx),numpy.log(uL2E))
print 'R^2 pres = ', rsquared(numpy.log(dx),numpy.log(pL2E))

if(outputPDF): plt.savefig("./L2Error.pdf")

if (showGraphic): plt.show()

