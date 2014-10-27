# This program averages a variable on each plane of normal (x,y,z) specified by the user 
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
#----------------

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************

#Initial time of simulation, final time and time increment must be specified by user
t0=0.02
tf=1.4
dT=0.02

#Number of x and y cell must be specified
nx=40
ny=40
nz=80

#Parameters for mixing layer in term of solid volume fraction
voidMinCut = 0.0002
voidMaxCut = 0.0098

nzMinCutUp=nz/2+3
nzMaxCutUp=65
nzMaxCutDown=nz/2-3

#======================
#   MAIN
#======================

# Directory to work within
os.chdir("./voidFraction") # go to directory

# Output file for the mixing layer
outname='mixingLayer'
outMixing=open(outname,'w')

nt=int(tf/t0)
t=t0
for i in range(0,nt):
    #Current case
    print "Plane averaging time ", t
    fname='voidfraction_' + str(t)


    x,y,z,phi = numpy.loadtxt(fname, unpack=True)

    #Pre-allocate
    phiAvg=numpy.zeros([nz])
    zAvg=numpy.zeros([nz])
    
    s=0 #start of average
    e=nx*ny-1 # end of average

    for i in range(0,nz):
	phiAvg[i]=numpy.mean(phi[s:e])
	zAvg[i]=z[s]
	s +=nx*ny
	e +=nx*ny

    #Create output file back in the averaged folder
    outname='./averaged/VoidFraction_' + str(t)
    outfile=open(outname,'w')

    #Output the plane average
    for i in range(0,nz):
	outfile.write("%5.5e %5.5e\n" %(zAvg[i],phiAvg[i]))
    outfile.close()

    # Calculate local mixing layer value
    # We calculate the beggining and the end of the mixing layer by finding the z at which it begins
    # and the z at which it ends
    notFound = 1
    phiAvg = abs(1-phiAvg)
    i=0
    #Find beggining of mixing layer
    while(notFound):
	if(phiAvg[i]<voidMinCut): # if I am lower than 0.0001 something
	    hmin=zAvg[i]
	else:
	    notFound=0
	i+=1
	    

    #Find end of mixing layer
    i=nzMaxCutUp
    notFound=1
    while  notFound:
	if(phiAvg[i]>voidMaxCut): # if I am larger than 0.999 something
	    hmax=zAvg[i]
	else:
	    notFound=0
	i-=1
	if i==nzMaxCutDown:
	    notFound=0
    
    hmax = hmax - numpy.max(zAvg)/nz
    hmin = hmin + numpy.max(zAvg)/nz
    outMixing.write('%5.5e %5.5e %5.5e %5.5e\n' %(t, (hmax-hmin)/2, hmin, hmax))
    t += dT


#Go back to main dir
os.chdir("..")
print "Post-processing over"


