###############################################################################
#
#   File    : analysePressure.py
#
#   Run Instructions    : python analysePressure.py directory/with/the/files
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the files in a folder and output
#                   a two column file that is N vs P
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
plot=True
rhof=1000

#======================
#   MAIN
#======================

# Directory to work within
if (len(sys.argv)<2) :
    print "You need to enter a folder argument"

folder=sys.argv[1]


# Acquire list of time step
speedFolder=os.listdir(folder)

# Go into folder
#os.chdir(sys.argv[1]) #go to directory

# Sort so that time will already be sorted
speedFolder.sort() 

N=[]
pAvg=[]

# Loop through all times
for i in speedFolder:

    print "Opening ", i
    pMat = numpy.loadtxt(folder+"/"+i, unpack=True,comments="#")
    t=pMat[0,:]
    dP=(pMat[1,:]-pMat[-1,:]) * rhof
    tempString= i.split("_")
    N.append(float(tempString[-1]))
    sortIndex=numpy.argsort(t)
    pS=dP[sortIndex]
    pAvg.append(numpy.average(pS[-10000:-1]))

print "Post-processing over"

# Save results
print "Saving results"
A = [numpy.asarray(N).T,numpy.asarray(pAvg).T]
numpy.savetxt("pressure_"+folder, numpy.asarray(A).T, fmt='%.8e', delimiter=' ', newline='\n')


#Plot results
if (plot):
    plt.plot(t,dP)

    plt.ylabel('Bottom pressure')
    plt.xlabel('Time (s)')
    plt.show()
