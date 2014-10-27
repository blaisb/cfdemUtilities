# Last Modified: Mon 05 May 2014 05:37:34 PM EDT

#This program makes the plot for L2 error 

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

#===================
# MAIN PROGRAM
#===================

fname = sys.argv[1]

#Input file
print "R-> %s" %fname
nx, uL2E, pL2E = numpy.loadtxt(fname, unpack=True)

dx=2./nx

fig = plt.figure()

ax = fig.add_subplot(111) # Create plot object
#ax.plot(numpy.log(dx),numpy.log(l2E),'-o',label="L2")
ax.plot(dx,uL2E,'ko')
ax.plot(dx,pL2E,'ks')

ax.set_yscale('log')
ax.set_xscale('log')
plt.ylabel('L$^2$ Error')
plt.xlabel('$\Delta x$')
a,b = numpy.polyfit(numpy.log(dx),numpy.log(uL2E),1)
#ax.text(0.0013,0.06, r'$\log(L^2_{u})=%3.2f  \log(\Delta x) %3.2f$' %(a,b), fontsize=15)

a2,b2 = numpy.polyfit(numpy.log(dx),numpy.log(pL2E),1)
#ax.text(0.0013,0.03, r'$\log(L^2_{p})=%3.2f  \log(\Delta x) + %3.2f$' %(a2,b2), fontsize=15)

ax.grid(b=True, which='minor', color='grey', linestyle='--')

ax.grid(b=True, which='major', color='k', linestyle='-')

plt.xlim([0.002,0.1])
ax.plot(dx,uL2E,'-ko',label='$\log(L^2_{u})=%3.2f  \log(\Delta x) %3.2f$' %(a,b))
ax.plot(dx,pL2E,'--ks',label='$\log(L^2_{p})=%3.2f  \log(\Delta x) + %3.2f$' %(a2,b2))

#ax.plot(dx,numpy.exp(b)*dx**a, color="k")
#ax.plot(dx,numpy.exp(b2)*dx**a2, color="k")
ax.legend(loc=2)

print 'A vel      = ', a
print 'A pressure =', a2
plt.savefig("./L2Error.pdf")
plt.show()

