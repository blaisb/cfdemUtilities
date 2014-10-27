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
import csv

#=====================
#   Main plot
#=====================

fname=sys.argv[1]

ri =0.064
ro=0.0238

#INPUT
print "R-> %s" %fname
r, phi = numpy.loadtxt(fname, unpack=True)

r_analytique=[]
phi_analytique=[]

#Open CSV file
with open('50p.csv', 'rb') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     i=0
     for row in csvreader:
	print row
	if (i >0):
	    r_analytique.extend([float(row[0])])
	    phi_analytique.extend([float(row[1])])
	i+=1



#Single sphere unsteady solution using Euler finite difference scheme
plt.figure(fname)
plt.plot(r/ro,1-phi,'-go', label="Void Fraction")
plt.plot(r_analytique,phi_analytique,label="Experimental results - Tetlow")
plt.ylabel('Fraction of liquid')
plt.xlabel('Radius (r)')
plt.legend(loc=9)
plt.show()

