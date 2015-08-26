# Last Modified: Tue 01 Apr 2014 12:05:09 PM EDT
#
# This program converts OpenFOAM raw lagrangian data to a text file containing information on the particles
# in the format that can be read by the porosity code
#
# Output format
# position (x y z) and radius 
# THIS PROGRAM REQUIRES A DIRECTORY particlesInfo in the main folder
#
# In the current form of the software the radius of the particles must be fixed the user
#
# Author : Bruno Blais


# Python imports
#----------------
import os
import sys
import numpy 
#----------------

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
#Initial time of simulation, final time and time increment must be specified by user
t0=2.5
tf=10.0
dT=0.5
radius = 0.0007485
height=0.05
ri = 0.0064
ro = 0.0238

#Tolerance to round-off timestamps
tol=0.0001

#====================
#    READER	
#====================
#This function reads an OpenFOAM raw lagrangian file and extract a table of the data
def readf(fname):

    infile = open(fname,'r')
    if (infile!=0):
	#Clear garbage lines
	for i in range(0,17):
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
	    #Cut using a series of split. This is slow, but it works
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

# Name of the files to be considered
inname= ['lagrangian/particleCloud/positions']

# Check if the destination folder exists
if not os.path.isdir("./particlesInfo"):
    print "********** Abort **********"
    print "The folder particlesInfo does not exist, you must create it manually in the working folder"

os.chdir("./CFD") # go to FOAM directory
nt=int((tf-t0)/dT)
t=t0
for i in range(0,nt):
    #Current case
    print "Post-processing time ", t

    #Go to the directory corresponding to the timestep
    if (t==0): os.chdir("0")
    elif ((numpy.abs(numpy.mod(t,1)))<tol): os.chdir(str(int(t)))
    else : os.chdir(str(t))

    #Create output file back in main folder
    outname="../../particlesInfo/particlesInfo_%s" %str(i)
    outfile=open(outname,'w')

    #Read each variables to be able to dimensionalise final array
    [n,x,y,z] = readf(inname[0])
 
    #Write header
    outfile.write("%i\n" %nt)
    outfile.write("%5.5e\n" %height)
    outfile.write("%5.5e\n" %ri)
    outfile.write("%5.5e\n" %ro)
    outfile.write("%i\n"  %n)
    outfile.write("%5.5e\n" %t)
    outfile.write("**************************************************\n")

    for j in range(0,n):
	outfile.write("%5.5e %5.5e %5.5e %5.5e \n" %(x[j],y[j],z[j],radius))

    outfile.close()
    t += dT
    #Go back to CFD directory
    os.chdir("..") # 

print "Post-processing over"


