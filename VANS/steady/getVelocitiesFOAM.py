# This program converts OpenFOAM raw data for the velocity field to a text file with 
# both position and velocity vector
# 
# position (x y z) and radius 
# THIS PROGRAM REQUIRES A DIRECTORY U in the main folder

#In the current form of the software the radius must be fixed byu the user

# Author : Bruno Blais
# Last modified : 15-01-2014

#Python imports
#----------------
import os
import sys
import numpy 
#----------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
#Initial time of simulation, final time and time increment must be specified by user
t0=10.0
tf=100.0
dT=10.0

# Disable Z coordinates (OPENFOAMBUG)
zRead = False 

#====================
#    READERS	
#====================
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

#======================
#   MAIN
#======================

#Name of the files to be considered
inname= ['ccx', 'ccy','ccz','U']
os.chdir("./CFD") # go to directory

nt=int((tf-t0)/dT)+1
t=t0
for i in range(0,nt):
    #Current case
    print "Post-processing time ", t

    #Go to the directory corresponding to the timestep
    if (t==0) : os.chdir("0")
    elif ((numpy.abs(numpy.mod(t+0.001,1)))<0.01): os.chdir(str(int(t)))
    else :os.chdir(str(t))

    [n,x] = readfScalar(inname[0])
    [n,y] = readfScalar(inname[1])
    if zRead : [n,z] = readfScalar(inname[2])
    else : z = numpy.zeros([n])
    [n,u,v, w] = readfVector(inname[3])

    #Create output file back in main folder
    outname="../../U/U_%s" %str(i)
    outfile=open(outname,'w')

    for j in range(0,n):
	outfile.write("%5.5e %5.5e %5.5e %5.5e %5.5e %5.5e  \n" %(x[j],y[j],z[j],u[j],v[j],w[j]))

    outfile.close()
    t += dT
    #Go back to CFD directory
    os.chdir("..") # 

print "Post-processing over"


