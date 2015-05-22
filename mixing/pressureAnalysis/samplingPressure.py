###############################################################################
#
#   File    : samplingPressure.py
#
#   Run Instructions    : python samplingPressure.py directory/with/the/timesteps
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the time step in a folder
#                   averaged the pressure on the raw_plane file
#                   and post-processes it in a graphic form
#                   However it uses the sample slices and the zeroth mesh
#                   instead of assuming that the sample is present by default
#
###############################################################################

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
rho=1400
plot=False


#======================
#   MAIN
#======================

# Directory to work within
if (len(sys.argv)<2) :
    print "You need to enter a folder argument"

folder=sys.argv[1]
#os.chdir(sys.argv[1]) #go to directory

# Acquire list of time step
timeFolder=os.listdir(folder)

# Sort so that time will already be sorted
timeFolder.sort() 

t=[]
pAvg=[]

#Open zeroth cellVolume raw file
fname =  folder+"/"+"0"+"/cellVolumes_constantPlane.raw"
x,y,z,vol = numpy.loadtxt(fname, unpack=True,comments="#")

# Loop through all times
for i in timeFolder:

    print "Opening ", i
    fname = folder+"/"+i+"/p_constantPlane.raw"
    x,y,z,p = numpy.loadtxt(fname, unpack=True,comments="#")

    t.append(float(i))
    pAvg.append(rho*numpy.sum(p*vol)/numpy.sum(vol))

print "Post-processing over"

# Save results
print "Saving results"

N = [numpy.asarray(t).T,numpy.asarray(pAvg).T]
numpy.savetxt("pressureBottom", numpy.asarray(N).T, fmt='%.8e', delimiter=' ', newline='\n')


#Plot results
if (plot):
    plt.plot(t,pAvg)

    plt.ylabel('Bottom pressure')
    plt.xlabel('Time (s)')
    plt.show()
