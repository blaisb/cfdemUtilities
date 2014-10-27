# Last Modified: Tue 01 Apr 2014 12:05:33 PM EDT
# This programs calculates the L2 error for a given velocity file
#
# Usage : python L2ErrorUCouette.py Velocity file
#
# Author : Bruno Blais
# Last modified : December 3rd


#Python imports
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#***********************************
# Parameters for analytical solution
#***********************************
omega = 0.62832
R=3.
k = 1./3.;


#===========================
# Main program
#===========================

fname = sys.argv[1]

# read the file
print "R-> Velocity file has been read"
[x,y,z,u,v,w] = numpy.loadtxt(fname, unpack=True)

r = numpy.sqrt(x**2 + y**2)
ut = numpy.sqrt(u**2 + v**2)

#Analytical solution for theta velocity in eulerian frame of reference
uth = omega *k* R * (-r/(R) + (R)/r) / (1/k - k)

err = numpy.sqrt((ut-uth)**2)
L2err = numpy.sum(err)
print "L2 err is : %5.5e" %(L2err)

fig = plt.figure()

#temp=numpy.ones([10,10])
#x=numpy.arange(0,1,0.1)
#y=numpy.arange(1,2,0.1)

plt.plot(r,err,'o')
#plt.subplot(1, 1, 1)
#plt.pcolor(x, y, err, cmap='RdBu', vmin=numpy.min(err), vmax=numpy.max(err))
#plt.title('pcolor')
#plt.axis([x.min(), x.max(), y.min(), y.max()])
#plt.colorbar()

plt.show()
