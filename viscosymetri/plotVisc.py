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
#Physical parameter
R = 0.0238
L=0.01
k=0.0138/0.0238
mu=0.1
phiVar=17500.*20;
epsMax=0.65
nBar=2.
factor = 1./(4.*numpy.pi*(1*2.*numpy.pi)*L*R*R * (k*k)/(1.-k*k)) / mu /2. / numpy.pi


#=============================
#    READER OF LOG FILE
#=============================
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

# Get name from terminal
ax = plt.figure("Torque") #Create window

#Labeling
plt.ylabel('Dyanmic viscosity [Pa*s]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the viscosity')

visc=[]
phi=[]
viscP = []


for i in range(1,len(sys.argv)):
    fname = sys.argv[i] 

    [t,moment] = readf(fname)
    phi.extend([float(int(fname))/phiVar])
    visc.extend([numpy.average(moment[-100:-1])])
    plt.plot(t,moment,'-')

    #get the power viscosity
    fnamePower="p"+fname
    t, p = numpy.loadtxt(fnamePower, unpack=True)

    # convert power to viscosity
    viscP.extend([p[-1]*factor]) 
plt.show()

#Second plot of evolution of viscosity vs phi


    

ax = plt.figure("Viscosity") #Create window
plt.ylabel('Dyanmic viscosity [Pa*s]')
plt.xlabel('Fraction of solid')
plt.title('Viscosity vs fraction of solid')



viscAnalytical=[]
for i in phi:
    viscAnalytical.extend([(1-i/epsMax)**(-nBar*epsMax)])

plt.plot(phi,visc,'-x', label='Simulation results Torque')
plt.plot(phi,viscP,'-x', label='Simulation results Power')
plt.plot(phi, viscAnalytical,'-o',label='Analytical model')
plt.legend(loc=2)
#plt.yscale('log')
plt.show()

