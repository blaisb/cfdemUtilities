# This program converts OpenFOAM raw data for the velocity field to a text file with 
# both position and velocity vector that exist within the folder
# 
# Output format :
# position (x y z), velocity vector (x,y,z), velocity vector (r,theta,z)
#
# Author : Bruno Blais
#
#Python imports
#----------------
import os
import sys
import numpy 
#----------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
#

#================================
#    READER FUNCTIONS	
#================================
#This function reads an OpenFOAM raw for a scalar and extract a table of the data
def readfScalar(fname):

    infile = open(fname,'r')
    if (infile!=0):
	#Clear garbage lines
	for i in range(0,20,1):
	    infile.readline()

	#Read number of cell centers
	n=int(infile.readline())
	
	#Pre-allocate memory
	xu=numpy.zeros([n])
	
	#Clear garbage line "("
	infile.readline()

	#read current property "xu"
	for i in range(0,n,1):
	    number_str=infile.readline()
	    xu[i]=float(number_str)
    else:
	print "File %s could not be opened" %fname

    infile.close();
    return n,xu


#This function reads an OpenFOAM raw file for a vector and extracts a table of the data
def readfVector(fname):

    infile = open(fname,'r')
    if (infile!=0):
	#Clear garbage lines
	for i in range(0,20):
	     infile.readline()

	#Read number of cell centers
	n=int(infile.readline())
	
	#Pre-allocate memory
	x=numpy.zeros([n])
	y=numpy.zeros([n])
	z=numpy.zeros([n])
	
	#Clear garbage line "("
	infile.readline()

	#read current property "xu"
	for i in range(0,n,1):
	    number_str=infile.readline()
	    number2_str=number_str.split("(")
	    number3_str=number2_str[1].split(")")
	    number4_str=number3_str[0].split()
	    x[i]=float(number4_str[0])
	    y[i]=float(number4_str[1])
	    z[i]=float(number4_str[2])
    else:
	print "File %s could not be opened" %fname

    infile.close();
    return n,x,y,z

#================================
#   MAIN
#================================

#Name of the files to be considered
inname= ['ccx', 'ccy','ccz','U']

os.chdir(sys.argv[1]) # go to directory

#Current case
print "Post-processing time : ", sys.argv[1]

[n,x] = readfScalar(inname[0])
[n,y] = readfScalar(inname[1])
[n,z] = readfScalar(inname[2])
[n,u, v, w] = readfVector(inname[3])


#Create output file back in main folder

outname="../../U/U_%s" %str(i)
outfile=open(outname,'w')

for j in range(0,n):
    outfile.write("%5.5e %5.5e %5.5e %5.5e %5.5e %5.5e \n" %(x[j],y[j],z[j],u[j],v[j],w[j],p[j],V[i]))

outfile.close()

print "Post-processing over"


