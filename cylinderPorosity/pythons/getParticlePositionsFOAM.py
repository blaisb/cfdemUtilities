# This program converts OpenFOAM raw data to a text file containing information on the particles
# in the format that can be read by the porosity code
# 
# position (x y z) and radius 
# THIS PROGRAM REQUIRES A DIRECTORY particles in the main folder

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
t0=5
tf=115.0
dT=5
radius = 0.0007485
height=0.05
ri = 0.0064
ro = 0.0238

#====================
#    READER	
#====================
#This function reads an OpenFOAM raw file and extract a table of the data
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
inname= ['lagrangian/particleCloud/positions']
os.chdir("./") # go to directory

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
    outname="../particlesInfo/particlesInfo_%s" %str(i)
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


