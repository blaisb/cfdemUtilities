# This extract the viscous force in the X direction from the force log
# and compares it with the analytical solution

# USAGE : python ./monitorTorque.py LOGFILE

# Author : Bruno Blais
# Last modified : 5-08-2014

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
L=0.025
H=0.025
V=0.1
mu=1.0
phiVar=17500.*20;
epsMax=0.65
nBar=2.5
factor =  H / V / L / L 

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
		l2_str = l_str[1].split("(")
		if (len(l_str)>2):
			l3_str=l2_str[1].split()
			l3_num = float(l3_str[0])
			moment.extend([l3_num])
		l2_str = l_str[0].split()
		l2_num = float(l2_str[0])
		t.extend([l2_num])

    else:
	print "File %s could not be opened" %fname

    for i in range(0,len(moment)):
	moment[i] = abs(moment[i] * factor)

    return t, moment
    infile.close();

#======================
#   MAIN
#======================

# Get name from terminal
ax = plt.figure("Viscous Force") #Create window

#Labeling
plt.ylabel('Dynamic viscosity [Pa*s]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the viscosity')

visc=[]
phi=[]
viscP = []


for i in range(1,len(sys.argv)):
    fname = sys.argv[i] 

    [t,moment] = readf(fname)
    phi.extend([1.-float(fname)])
    visc.extend([numpy.average(moment[-2:-1])])
    plt.plot(t,moment,'-')

    #get the power viscosity
    #fnamePower="p"+fname
    #t, p = numpy.loadtxt(fnamePower, unpack=True)

    # convert power to viscosity
    #viscP.extend([p[-1]*factor]) 
plt.show()

#Second plot of evolution of viscosity vs phi

ax = plt.figure("Viscosity") #Create window
plt.ylabel('Dynamic Viscosity [Pa*s]')
plt.xlabel('Fraction of solid')
plt.title('Viscosity vs fraction of solid')

viscAnalytical=[]
for i in phi:
    viscAnalytical.extend([(1-i/epsMax)**(-nBar*epsMax)])

plt.plot(phi,visc,'-x', label='Simulation results Force')
#plt.plot(phi,viscP,'-x', label='Simulation results Power')
plt.plot(phi, viscAnalytical,'-.o',label='Analytical model')
plt.legend(loc=2)
#plt.yscale('log')
plt.show()

