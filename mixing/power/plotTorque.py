# This program is a Torque monitor for a log file that is currently being created in OpenFOAM
# The code reads multiple logfile and superposes on the same graphic
# The code has been extended to be able to take both the SRF, AMI force analysis and the
# native IBM analysis
#
#   USAGE   : python ./plotTorque.py MODE FILE MODE FILE
#   
#   MODE    : (srf, SRF, ami, AMI), (ibm, IBM)
#
# Author : Bruno Blais

#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
import re # Ouhh regular expressions :)
#----------------

#==============================================================================
#   OPTIONS AND USER PARAMETERS
#==============================================================================
rho=1000
skip=1
fullMoments=False # Show viscous and pressure moments for AMI and SRF

#==============================================================================
#    READER OF LOG FILE
#==============================================================================
# This function reads the log file and extracts the pressure and viscous torque
def readf(fname):
    
    t=[]
    momentVisc=[]
    momentPres=[]

    infile = open(fname,'r')
    if (infile!=0):
	print "Log file opened"
	
	for l in infile:
	    l_str = l.split(")")

	    if (len(l_str)>3):
		l2_str = l_str[5].split()
		if (len(l_str)>2):
		    l2_num = float(l2_str[2])
		    momentVisc.extend([l2_num])

                l2_str = l_str[4].split()
                if (len(l_str)>2):
                    l2_num = float(l2_str[2])
                    momentPres.extend([l2_num])

		l2_str = l_str[0].split()
		l2_num = float(l2_str[0])
		t.extend([l2_num])

    else:
	print "File %s could not be opened" %fname

    return t, momentVisc, momentPres
    infile.close();

#==============================================================================
#   MAIN
#==============================================================================

# Get name from terminal
ax = plt.figure("Torque") #Create window

#Labeling
plt.ylabel('Torque [N-m]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the torque')

for i in range(1,len(sys.argv),2):
    mode=sys.argv[i]
    fname = sys.argv[i+1] 

    if( mode=="srf" or mode=="SRF" or mode=="ami" or mode=="AMI" ):
        [t,momentVisc,momentPres] = readf(fname)
        moment = numpy.asarray(momentVisc) + numpy.asarray(momentPres)

    if( mode=="ibm" or mode=="IBM" ):
        [t,x,y,moment] = numpy.loadtxt(fname,unpack=True)
        moment *= rho 
    if (fullMoments):
        plt.plot(t[skip:-1],moment[skip:-1],'-o',label="Combined_"+fname)
        plt.plot(t[skip:-1],momentPres[skip:-1],label="Pressure")
        plt.plot(t[skip:-1],momentVisc[skip:-1],label="Viscous")
    else:
        plt.plot(t[skip:-1],moment[skip:-1],'-o',label=fname)
    plt.legend()
plt.show()

