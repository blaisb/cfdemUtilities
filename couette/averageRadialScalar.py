# This program averages a variable for each value of r for each files specified by the user 
# This program must be launched from the main folder of a case from which you can access ./CFD/ and ./voidfraction/ 
# A FOLDER ./voidfraction/averaged must exist!

# Author : Bruno Blais
# Last modified : 15-01-2014

#Python imports
#----------------
import os
import sys
import numpy 
import math
import matplotlib.pyplot as plt
#----------------

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************

#Initial time of simulation, final time and time increment must be specified by user
t0=2.0
tf=100.
dT=0.5


#Number of x and y cell must be specified
nz=1
nr = 10

#======================
#   MAIN
#======================

# Directory to work within
os.chdir("./voidFraction") # go to directory

nt=int((tf-t0)/dT)
t=t0
for i in range(0,nt):
    #Current case
    print "Radially averaging time ", t
    fname='voidfraction_' + str(t)

    x,y,z,phi = numpy.loadtxt(fname, unpack=True)

    #Pre-allocate
    phiAvg=numpy.zeros([4*nr*nr])
    r = numpy.zeros([4*nr*nr])
    lr = numpy.zeros([nr]) # list of possible radiuses
    phiR = numpy.zeros([nr]) # radially averaged variable

    #Calculate radiuses
    r = numpy.sqrt(x*x + y * y)

    #Establish list of possible radiuses
    nlr = 0 # counter on how many radiuses were found
    for j in range (0,len(r)):
	cr = r[j] # current radius
	present = 0;
	for k in range(0,nlr):
	    if (numpy.abs(cr - lr[k]) < 1e-5):
		present =1
		phiR[k] += phi[j]
	
	if (present == 0):
	    lr[nlr] = cr
	    nlr +=1

    #Do the final average
    for j in range (0,nr):
	phiR[j] = phiR[j] / (4*nr)


    #Create output file back in the averaged folder
    outname='./averaged/radialVoidFraction_' + str(t)
    outfile=open(outname,'w')

    for i in range(0,nr):
	outfile.write("%5.5e %5.5e\n" %(lr[i],phiR[i]))
    outfile.close()
    t = t+dT

#Go back to main dir
os.chdir("..")
print "Post-processing over"


