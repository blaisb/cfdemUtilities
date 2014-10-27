# This program converts OpenFOAM raw data to a text file containing position (x y z) and void fraction (phi) 
# This program must be launched from the main folder of a case from which you can access ./CFD/  
# THIS PROGRAM REQUIRES A DIRECTORY voidfraction in the main folder
# Cell centre must have been previously made within the folder

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
t0=2.0
tf=100.
dT=0.5

#====================
#    READER	
#====================
#This function reads an OpenFOAM raw file and extract a table of the data
def readf(fname):

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

#======================
#   MAIN
#======================

#Name of the files to be considered
inname= ['ccx', 'ccy','ccz','voidfraction']
os.chdir("./CFD") # go to directory

nt=int((tf-t0)/dT)
t=t0
for i in range(0,nt):
    #Current case
    print "Post-processing time ", t

    #Go to the directory corresponding to the timestep
    if (t>0.99999 and t<1.0000001) : os.chdir("1")
    elif (t==0) : os.chdir("0")
    elif ((numpy.abs(numpy.mod(t,1)))<0.01): os.chdir(str(int(t)))
    else :os.chdir(str(t))


    #Create output file back in main folder
    outname="../../voidFraction/voidfraction_%s" %str(t)
    outfile=open(outname,'w')

    #Read each variables to be able to dimensionalise final array
    [n,x] = readf(inname[0])
    [n,y] = readf(inname[1])
    [n,z] = readf(inname[2])
    [n,phi] = readf(inname[3])
    
    for j in range(0,n):
	outfile.write("%5.5e %5.5e %5.5e %5.5e\n" %(x[j],y[j],z[j],phi[j]))

    outfile.close()
    t += dT
    #Go back to CFD directory
    os.chdir("..") # 

print "Post-processing over"


