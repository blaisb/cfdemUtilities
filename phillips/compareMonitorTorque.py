# This programs compares two log file of two different openfoam cases being run (or that have finished, etc.)
# The variable compared is the torque in the Z direction

# Author : Bruno Blais
# Last modified : 23-01-2014

#Python imports
#----------------------------------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
import re # Ouhh regular expressions :)
#----------------------------------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
# NONE

#=============================
#    READER OF LOG FILE
#=============================
# This function reads the log file and extracts the torque
def readf(fname):
    
    t=[]
    moment=[]

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

# Get names from terminal
fname=[]
for i in range(0,len(sys.argv)-1) : fname.extend([sys.argv[i+1]]) #better done in a loop heh?

#plt.ion() # interactive mode is on
plt.figure()
line1 = plt.plot([], [],'-k') #create structure that will be updated

#Labelling!
plt.ylabel('Measure torque on inner cylinder [N-m]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the torque')

# Plots are made manually, this allows for some thinkering in the format, could be made in a loop though
# The if clause is in the case that one more time is read than the torque as this would create
# two arrays that are not of the same length

#### Plot 1 
[t,moment] = readf(fname[0])
if len(t) == len(moment) : plt.plot(t,moment, '-b', label=fname[0]) 
else : plt.plot(t[1:],moment,'-b', label = fname[0])

#### Plot 2
[t,moment] = readf(fname[1])
if len(t) == len(moment) : plt.plot(t,moment,'-r', label = fname[1])
else : plt.plot(t[1:],moment,'-r', label = fname[1])

#### Plot 3
if len(sys.argv) >= 4 :
    [t,moment] = readf(fname[2])
    if len(t) == len(moment) : plt.plot(t,moment,'-g',label = fname[2])
    else : plt.plot(t[1:],moment,'-g',label = fname[2])

#### Plot 4
if len(sys.argv) >= 5 :
    [t,moment] = readf(fname[3])
    if len(t) == len(moment) : plt.plot(t,moment,'-y',label = fname[3])
    else : plt.plot(t[1:],moment,'-y',label = fname[3])

#### Plot 5
if len(sys.argv) >= 6 :
    [t,moment] = readf(fname[4])
    if len(t) == len(moment) : plt.plot(t,moment,'-m',label = fname[4])
    else : plt.plot(t[1:],moment, '-m', label = fname[4])

#### Plot 6
if len(sys.argv) >= 7 :
    [t,moment] = readf(fname[5])
    if len(t) == len(moment) : plt.plot(t,moment,'-k',label = fname[5])
    else : plt.plot(t[1:],moment, '-k', label = fname[5])

#### Plot 7
if len(sys.argv) >= 8 :
    [t,moment] = readf(fname[6])
    if len(t) == len(moment) : plt.plot(t,moment,'-x',label = fname[6])
    else : plt.plot(t[1:],moment, '-x', color='chartreuse', label = fname[6])

#### Plot 8
if len(sys.argv) >= 9 :
    [t,moment] = readf(fname[7])
    if len(t) == len(moment) : plt.plot(t,moment,'-o',label = fname[7])
    else : plt.plot(t[1:],moment, '-o', color='chartreuse', label = fname[7])

plt.legend(loc=7)
plt.show()


