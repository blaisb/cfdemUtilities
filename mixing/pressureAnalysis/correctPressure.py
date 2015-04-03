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
plot=False
samplePoints=50

#======================
#   MAIN
#======================

# Directory to work within
if (len(sys.argv)<2) :
    print "You need to enter a file argument"

fileId=sys.argv[1]

#425 RPM
beg=50. 
end=80.
gap=28.



print "Opening ", fileId
t,p = numpy.loadtxt(fileId, unpack=True,comments="#")
sortIndex=numpy.argsort(t)
tS=t[sortIndex]
pS=p[sortIndex]

print "Correcting"

for i,j in enumerate(pS):
    if (tS[i]>60.):
        pS[i]=pS[i] + min(1.,(tS[i]-beg)/(end-beg))*gap


# Save results
print "Saving results"
A = [numpy.asarray(tS).T,numpy.asarray(pS).T]
numpy.savetxt(fileId+"_CORR", numpy.asarray(A).T, fmt='%.8e', delimiter=' ', newline='\n')

