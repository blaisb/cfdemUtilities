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
#----------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
#
readZ=False
readShear=True
readPseudo=True

#Initial time of simulation, final time and time increment must be specified by user
t0=1.
tf=1.
dT=1.

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

# Check if the destination folder exists
if not os.path.isdir("./U"):
    print "********** Abort **********"
    print "The folder particlesInfo does not exist, you must create it manually in the working folder"

#Name of the files to be considered
inname= ['ccx', 'ccy','ccz','p','psi','xi','cellVolumes']

os.chdir(sys.argv[1]) # go to directory

nt=int((tf-t0)/dT)+1
t=t0
for i in range(0,nt):
    #Current case
    print "Post-processing time ", t

    #Go to the directory corresponding to the timestep
    if (t==0) : os.chdir("0")
    elif ((numpy.abs(numpy.mod(t+0.00001,1)))<0.01): os.chdir(str(int(t)))
    else :os.chdir(str(t))

    [n,x] = readfScalar(inname[0])
    [n,y] = readfScalar(inname[1])
    if readZ :[n,z] = readfScalar(inname[2])
    else : z=numpy.zeros([numpy.size(x)])
    [n, p] = readfScalar(inname[3])
    [n, psi] = readfScalar(inname[4])
    [n, xi] = readfScalar(inname[5])
    [n, V] = readfScalar(inname[6])
       
    #Create output file back in main folder
    outname="../../U/U_%s" %str(i)
    outfile=open(outname,'w')

    for j in range(0,n):
            outfile.write("%5.5e %5.5e %5.5e %5.5e %5.5e %5.5e %5.5e \n" %(x[j],y[j],z[j],p[j],psi[j],xi[j],V[j]))
    
    outfile.close()
    
    #Go back to CFD directory
    os.chdir("..") # 

print "Post-processing over"


