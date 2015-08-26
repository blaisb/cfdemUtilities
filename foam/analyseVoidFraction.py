# This program converts OpenFOAM raw data for the velocity field to a text file with 
# both position and velocity vector
# 
# Output format :
# position (x y z) and velocity vector 
# THIS PROGRAM REQUIRES A DIRECTORY U in the main folder
#
#
# Author : Bruno Blais

#Python imports
#----------------
import os
import sys
import numpy
import pylab
import matplotlib.pyplot as plt
#----------------

from funcReadFieldsFoam import *

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
#Name of the files to be considered
inname= ['ccx', 'ccy','ccz','p','voidfraction','cellVolumes']

#===================================
#   FUNCTIONS
#===================================

def volBelowThreshold(voidfraction,V,thres):
    vol = numpy.sum(V*(voidfraction<=thres))
    return vol

def volParticlesBelowThreshold(voidfraction,V,thres):
    vol = numpy.sum(V*(1-voidfraction)*(voidfraction<=thres))
    return vol

def fractionParticlesBelowThreshold(voidfraction,V,thres):
    frac = volParticlesBelowThreshold(voidfraction,V,thres) / volParticlesBelowThreshold(voidfraction,V,1.1)
    return frac

#======================
#   MAIN
#======================

colors=['b','g','r']


try:
    mode=sys.argv[1]
    path=sys.argv[2]
except:
    print 'Insufficient number of arguments'

# Analyse how % of the total particle volumes are within cells of a given void fraction
if (mode.lower()=="time"):
    folder=path+'/'
    [n,x] = readfScalar(folder+inname[0])
    [n,y] = readfScalar(folder+inname[1])
    [n,z] = readfScalar(folder+inname[2])
    [n, p] = readfScalar(folder+inname[3])
    [n, voidfraction] = readfScalar(folder+inname[4])
    [n, V] = readfScalar(folder+inname[5])
    tankVolume=volBelowThreshold(voidfraction,V,1.1)
    for i in numpy.arange(0.50,1.01,0.05):
        print "Threshold %1.2f --- Value %1.2f" %(i,fractionParticlesBelowThreshold(voidfraction,V,i))


# Makes histograms for all the given time steps of the void fraction distribution
elif (mode.lower()=="timehist"):
    fig, ax1=plt.subplots()
    
    for i in range(2,len(sys.argv)):
        j=i-2
        folder=sys.argv[i]+'/'
        [n, voidfraction] = readfScalar(folder+inname[4])
        [n, V] = readfScalar(folder+inname[5])
        tankVolume=volBelowThreshold(voidfraction,V,1.1)
        bins = numpy.arange(0.40,0.999,0.050)
        # the histogram of the data with histtype='step'
        percentiles=voidfraction#*V / volParticlesBelowThreshold(voidfraction,V,1.1)
        n, bins, patches = ax1.hist(percentiles,bins, normed=True,stacked=True, histtype='bar', rwidth=0.3+0.3*j,alpha=0.8-0.2*j,label=sys.argv[i],color=colors[j])
        bins=numpy.append(bins,1.)
        t=[]
        for k in bins:
            t.append(fractionParticlesBelowThreshold(voidfraction,V,k))
        ax2=ax1.twinx()
        ax2.plot(bins,t,color=colors[j])
    
    ax1.legend(loc="best");
    
    plt.show()

# Carries out the analysis for an entire folder with all the sub time step. Not implemented yet
elif (mode.lower()=="folder"):
    print "Not implemented yet"
else:
    print "This is not a mode of the script :\n -file \n -folder"


