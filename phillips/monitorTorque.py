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

#refresh frequency
tRefresh=0.5

#Number of refreshes
nRefresh=100

#=============================
#    READER OF LOG FILE
#=============================
# This function reads the log file and extracts the torque
def readf(fname):
    
    t=[]
    moment=[]

    # Create the patterns for the time and the moment. 
    # This pattern is used to check if a line contains the information we want
    patternVariable = re.compile('moment\Wpressure,viscous')
    patternTime = re.compile('Time =')
    patternTimeExclude = re.compile('Execution')

    infile = open(fname,'r')
    if (infile!=0):
	print "Log file opened"
	
	for l in infile:
	    if patternVariable.search(l):
		l_str = l.split(")")
		l2_str = l_str[2].split()
		l2_num = float(l2_str[2])
		moment.extend([l2_num])

	    if patternTime.search(l):
		if  not patternTimeExclude.search(l):
		    l_str= l.split()
		    l2_num=float(l_str[2])
		    t.extend([l2_num])
    else:
	print "File %s could not be opened" %fname

    return t, moment
    infile.close();

#======================
#   MAIN
#======================

# Get name from terminal
fname = sys.argv[1] 

plt.ion() # interactive mode is off, user cannot interact with the matplotlib windows
plt.figure(fname) #Create window
line1 = plt.plot([], [],'-k',label='black') #create the plot structure that will be updated

#Labeling
plt.ylabel('Measure torque on inner cylinder [N-m]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the torque')

for i in range(1,nRefresh):
    time.sleep(tRefresh)
    [t,moment] = readf(fname)
    if len(t) == len(moment) : plt.plot(t,moment,'-bo')
    else : plt.plot(t[1:],moment,'-bo')
    
    #If one wishes to toy around with the axis
    #x1,x2,y1,y2 = plt.axis()
    #y2+=0.001
    #y1 -=0.001
    #plt.axis((x1,x2,y1,y2))
    
    #Draw graph
    plt.draw()


