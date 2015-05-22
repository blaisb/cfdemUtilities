#------------------------------------------------------------------------------------------------------------
#
# This program creates a probe dictionnary for openfoam to sample in r theta z with homogenous distribution 
# 
# Output format : probesDict format of openFOAM
#
# Usage : python createProbesPoints ./probesDictFile
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import os
import sys
import numpy 
#----------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
R=0.180
H=0.36

nR=59
nZ=100
nT=30

#********************************
#   FUNCTIONS
#********************************

def writeFile(name,x,y,z):
    print "Writing the file : ", name
    outfile=open(name,'w')

    #Write stupid header
    outfile.write("FoamFile { version     2.0; format      ascii; class       dictionary; object      probesDict;}\n\n")

    outfile.write("fields ( U\n voidfraction \n p \n Us );\n\n ")
    outfile.write("probeLocations (\n")
    for i in range(0,len(x)):
        outfile.write("(%f %f %f)\n" %(x[i],y[i],z[i]))
    outfile.write(");")

#================================
#   MAIN
#================================

originalPath=os.getcwd()

outputFile=sys.argv[1]

r=numpy.linspace(2e-3,R,nR)
Z=numpy.linspace(1e-3,H,nZ)
t=numpy.linspace(1e-2,2*3.14159,nT)
x=[]
y=[]
z=[]

for i in Z:
    for j in r:
        for k in t:
            x.append(j*numpy.cos(k))
            y.append(j*numpy.sin(k))
            z.append(i)

writeFile(outputFile,x,y,z)
os.chdir(originalPath)
print "File generation over"


