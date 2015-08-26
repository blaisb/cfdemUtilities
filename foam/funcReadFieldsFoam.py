# This program contains functions to read scalar or vector field from openFOAM
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

