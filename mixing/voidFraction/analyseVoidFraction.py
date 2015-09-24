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
png=True

#********************************
#   Figures options
#********************************

plt.rcParams['figure.figsize'] = 10, 7
params = {'backend': 'ps',
             'axes.labelsize': 20,
             'text.fontsize': 20,
             'legend.fontsize': 18,
             'xtick.labelsize': 18,
             'ytick.labelsize': 18,
             'text.usetex': True,
             }

plt.rcParams.update(params)


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
labels=["1.5 s.", "6 s.", "50 s."]

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
    for i in numpy.arange(0.50,1.01,0.025):
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
        bins = numpy.arange(0.40,0.999,0.025)
        # the histogram of the data with histtype='step'
        #percentiles=voidfraction#*V / volParticlesBelowThreshold(voidfraction,V,1.1)
        percentiles=[]
        #Make percentiles manually
        percentiles.append(fractionParticlesBelowThreshold(voidfraction,V,bins[0]))
        for k in range(1,len(bins)):
            percentiles.append(fractionParticlesBelowThreshold(voidfraction,V,bins[k]) - fractionParticlesBelowThreshold(voidfraction,V,bins[k-1]))

        #n, bins, patches = ax1.hist(percentiles,bins, normed=False,stacked=True, histtype='bar', rwidth=0.3+0.3*j,alpha=0.8-0.2*j,label=sys.argv[i],color=colors[j])
        ax1.bar(bins,percentiles,width=0.025,alpha=0.9-0.3*j,label=labels[j],color=colors[j])
        plt.ylim([0,.5])
        plt.xlim([0.4,1])
        plt.ylabel("Volume fraction of cells with particles")
        plt.xlabel("Void fraction")
       #plt.clf() # Get rid of this histogram since not the one we want.

        #nx_frac = n/float(len(n)) # Each bin divided by total number of objects.
        #width = bins[1] - bins[0] # Width of each bin.
        #x = numpy.ravel(zip(bins[:-1], bins[:-1]+width))
        #y = numpy.ravel(zip(nx_frac,nx_frac))

        #plt.plot(x,y,linestyle="dashed",label="MyLabel")
        
        bins=numpy.append(bins,1.)
        t=[]
        for k in bins:
            t.append(fractionParticlesBelowThreshold(voidfraction,V,k))
        ax2=ax1.twinx()
        ax2.plot(bins,t,'-^',color=colors[j],linewidth=2.5)
        plt.ylabel("Cumulative fraction")
        plt.ylim([0,1.])
        plt.xlabel("Void fraction")

    ax1.legend(loc="upper left");
    
    if (png): plt.savefig("./hist.png",dpi=300)
    plt.show()

# Carries out the analysis for an entire folder with all the sub time step. Not implemented yet
elif (mode.lower()=="folder"):
    print "Not implemented yet"
else:
    print "This is not a mode of the script :\n -file \n -folder"


