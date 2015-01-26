###############################################################################
#
#   File    : planePressure.py
#
#   Run Instructions    : python planePressure.py directory/with/the/timesteps
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the time step in a folder
#                   averaged the pressure on the raw_plane file
#                   and post-processes it in a graphic form
#
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

#======================
#   MAIN
#======================

# Directory to work within
if (len(sys.argv)<2) :
    print "You need to enter a folder argument"

folder=sys.argv[1]
#os.chdir(sys.argv[1]) #go to directory

# Output file for the mixing layer
outname='pressureAnalysis'
outPressure=open(outname,'w')

# Acquire list of time step
timeFolder=os.listdir(folder)

# Sort so that time will already be sorted
timeFolder.sort() 

t=[]
pAvg=[]

# Loop through all times
for i in timeFolder:

    print "Opening ", i
    fname = folder+"/"+i+"/p_constantPlane.raw"
    x,y,z,p = numpy.loadtxt(fname, unpack=True,comments="#")
    fname =  folder+"/"+i+"/cellVolumes_constantPlane.raw"
    x,y,z,vol = numpy.loadtxt(fname, unpack=True,comments="#")



    t.append(float(i))
    pAvg.append(rho*numpy.sum(p*vol)/numpy.sum(vol))

print "Post-processing over"

#Plot results
plt.plot(t,pAvg)

plt.ylabel('Bottom pressure')
plt.xlabel('Time (s)')
plt.show()
