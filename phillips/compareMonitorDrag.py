#This programs compares two log file of two different openfoam cases being run (or that have finished, etc.)
# The comparison that is carried out here is on the drag force

# Author : Bruno Blais
# Last modified : 23-01-2014

#Python imports
#---------------------------------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
import re # Ouhh regular expressions :)
#-----------------------------------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
#refresh frequency


#=============================
#    READER OF LOG FILE
#=============================
# This function reads the log file and extracts the torque
def readf(fname):
    
    t=[]
    dragx=[]
    dragy=[]
    dragz=[]

    patternVariable = re.compile('Volume CPU dragtota')
    patternTime = re.compile('Time =')
    patternTimeExclude = re.compile('Execution')


    infile = open(fname,'r')
    if (infile!=0):
	print "Log file opened"
	l_prev="init"
	for l in infile:
	    if patternVariable.search(l_prev):
		l_str = l.split()
		dragx.extend([float(l_str[5])])
		dragy.extend([float(l_str[6])])
		dragz.extend([float(l_str[7])])
	    if patternTime.search(l):
		if  not patternTimeExclude.search(l):
		    l_str= l.split()
		    l2_num=float(l_str[2])
		    t.extend([l2_num])
	    l_prev=l
    else:
	print "File %s could not be opened" %fname

    return t, dragx, dragy, dragz
    infile.close();

#======================
#   MAIN
#======================

# Get names from terminal
fname=[]
for i in range(0,len(sys.argv)-1) : fname.extend([sys.argv[i+1]])

#plt.ion() # interactive mode is on
plt.figure()
line1 = plt.plot([], [],'-k') #create structure that will be updated
plt.ylabel('Drag force on the particles [N]')
plt.xlabel('Time [s]')
plt.title('Dynamic evolution of the average drag on the particles')


#### Plot 1 
[t,dragx,dragy,dragz] = readf(fname[0])
plt.plot(t,dragx[2:],'-b',label = fname[0])

#### Plot 2
[t,dragx,dragy,dragz] = readf(fname[1])
plt.plot(t,dragx[2:],'-r',label = fname[1])

#### Plot 3
if len(sys.argv) >= 4 :
    [t,dragx,dragy,dragz] = readf(fname[2])
    plt.plot(t,dragx[2:],'-g',label = fname[2])

#### Plot 4
if len(sys.argv) >= 5 :
    [t,dragx,dragy,dragz] = readf(fname[3])
    plt.plot(t,dragx[2:],'-y',label = fname[3])

#### Plot 5
if len(sys.argv) >= 6 :
    [t,dragx,dragy,dragz] = readf(fname[4])
    plt.plot(t,dragx[2:],'-m',label = fname[4])

#### Plot 6
if len(sys.argv) >= 7 :
    [t,dragx,dragy,dragz] = readf(fname[5])
    plt.plot(t,dragx[2:],'-m',label = fname[5])

plt.legend()
plt.show()


