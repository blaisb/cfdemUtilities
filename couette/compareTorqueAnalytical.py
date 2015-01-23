# This program is a Torque monitor for a log file that is currently being created in OpenFOAM
# The code dynamically re-reads the logfile and update the graphic
# It is impossible to close the graphic until the complete refresh is over (this can be modified)

# USAGE : python ./monitorTorque.py LOGFILE

# Author : Bruno Blais
# Last modified : 23-01-2014

#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
import re # Ouhh regular expressions :)
#----------------

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
omega = 1./60.*2.*numpy.pi
rho=1000
L=0.1
R=0.1
k = 1./4.
mu=1
openFoamLog=0
#Analytical solution for the Torque in the couette geometry
torque = -4.*numpy.pi*mu*omega*R*R*L*(k*k/(1.-k*k))

#==================================
#    READER OF OpenFOAM LOG FILE
#==================================
# This function reads the log file and extracts the torque
def readf(fname):
    t=[]
    moment=[]
    infile = open(fname,'r')
    if (infile!=0):
	print "Log file opened"
	
	for l in infile:
	    l_str = l.split(")")

	    if (len(l_str)>3):
		l2_str = l_str[5].split()
		if (len(l_str)>2):
			l2_num = float(l2_str[2])
			moment.extend([l2_num])
		l2_str = l_str[0].split()
		l2_num = float(l2_str[0])
		t.extend([l2_num])

    else:
	print "File %s could not be opened" %fname

    for i in range(0,len(moment)):
	moment[i] = abs(moment[i]/(4.*numpy.pi*(1*2.*numpy.pi)*L*R*R * (k*k)/(1.-k*k))) / mu


    return t, moment
    infile.close();

#======================
#   MAIN
#======================

fname=sys.argv[1]

#Labeling
ax = plt.figure("Torque") #Create window
plt.ylabel('Torque [N-m]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the Torque')

if (openFoamLog==1):
    fname = sys.argv[i] 
    [t,moment] = readf(fname)
    plt.plot(t,moment,'-')

if (openFoamLog==0):
    [t, momentX, momentY, momentZ] = numpy.loadtxt(fname, unpack=True)
    plt.plot(t,rho*(momentZ),'-',t,t/t*torque)

print rho*momentZ[-1]/torque

plt.show()

