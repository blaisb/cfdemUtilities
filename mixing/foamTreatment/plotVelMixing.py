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
rInt=20
tol=3e-3

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

originalPath=os.getcwd()
os.chdir(sys.argv[1]) # go to directory

#Current case
print "Post-processing time : ", sys.argv[1]

[n,x] = readfScalar(inname[0])
[n,y] = readfScalar(inname[1])
[n,z] = readfScalar(inname[2])
[n,u, v, w] = readfVector(inname[3])

#Calculate uR, uTheta, and Uz
theta=numpy.arctan2(y,x)
r = numpy.sqrt(x*x+y*y)

ur = numpy.cos(theta) * u + numpy.sin(theta)*v
ut = -numpy.sin(theta) * u + numpy.cos(theta)*v

#Obtain all the z of interest
#zS=[z[1]]
#for i in z:
#    present=False
#    for j in zS:
#        if (abs((j-i))<2e-3): 
#            present=True
#            break
#    if (present==False):
#        zS.append(i)

#Design array of z and r of interest
zS=numpy.linspace(0,max(z)+1e-3,40)
rS=numpy.linspace(0,max(r)+1e-3,25)
#Slice into radi slice for averaging

acc=numpy.zeros([len(zS),len(rS),3])
occ=numpy.zeros([len(zS),len(rS)])
notLoc=0
for i in range(0,n):
    locz=-1
    locr=-1
    for j,zz in enumerate(zS):
        if (abs(z[i]-zz)<tol): locz=j
        for k,rr in enumerate(rS):
            if (abs(r[i]-rr)<tol) : locr=k
            if (locz>0 and locr>0):
                acc[locz,locr,0]+=u[i]
                acc[locz,locr,1]+=v[i]
                acc[locz,locr,2]+=w[i]
                occ[locz,locr]+=1
                break

    if(locz<0 and locr<0):
       notLoc+=1



print " A total of : ", notLoc, "   points were not located"

os.chdir(originalPath)
print "Post-processing over"


