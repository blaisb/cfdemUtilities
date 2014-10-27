# This program plots the void fraction in the radial direction for the Couette-Tetlow case

#Usage : python plotSingleTetlow.py NAME_OF_FILE

#Data in the file must be in the format "r voidfraction"

# Author : Bruno Blais
# Last modified : 03-03-2014

#Python imports
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys

#=====================
#   Main plot
#=====================

fname=sys.argv[1]

#INPUT
print "R-> %s" %fname
r, phi = numpy.loadtxt(fname, unpack=True)

#Single sphere unsteady solution using Euler finite difference scheme
plt.figure(fname)
plt.plot(r,1-phi,'-go', label="Void Fraction")
plt.ylabel('Fraction of liquid')
plt.xlabel('Radius (r)')
plt.legend(loc=9)
plt.show()

