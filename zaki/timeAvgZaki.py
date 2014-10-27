#This program takes a time average of the Zaki sedimentation results
# Input: Case name , number of particle, initial time and final time of avg
# output:

# Author : Bruno Blais
# Last modified : December 3rd

#Python imports
import os
import sys
import numpy

#=====================
#   Main pcode
#=====================

#Name of input file (fname) and output file (outname)
fname="./"+sys.argv[1] 
outname="./"+sys.argv[1]+"AVG"

np=float(sys.argv[2])
N1=float(sys.argv[3])
N2=float(sys.argv[4])

# Read statistics as input
print "R-> %s" %fname
N, u ,v, w, unorm, wStd, wMax, wMin = numpy.loadtxt(fname, unpack=True)

# Find Number of iterations that are in the desired range
index=numpy.where((N > N1) & (N < N2))

#Time averaged properties
u_t=numpy.mean(u[index])
v_t=numpy.mean(v[index])
w_t=numpy.mean(w[index])
unorm_t=numpy.mean(unorm[index])
wStd_t=numpy.mean(wStd[index])
wMax_t=numpy.mean(wMax[index])
wMin_t=numpy.mean(wMin[index])

#Open temporary result file and write time-averaged resutls
outfile=open(outname,'w')
outfile.write("%5.5e %5.5e %5.5e %5.5e %5.5e %5.5e %5.5e %5.5e\n  " %(np, u_t, v_t, w_t, unorm_t, wStd_t, wMax_t, wMin_t))

outfile.close()



