# This programs agglomerate the Torque and dissipation results at different Re for different
# methods and compare them
#
# USAGE     : python ./plotAllNp.py 
#   
# Comments  : list of prefix, velocity and viscosity must be changed manually in the python file
#
# Author : Bruno Blais
# Last modified : 23-01-2014

#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import re # Ouhh regular expressions :)
#----------------

#==============================================================================
#   OPTIONS AND USER PARAMETERS
#==============================================================================
#Physical parameter
saveTxt=True
saveImage=True
savePdf=False
prefix = ["SRF_iforce"]
viscosity = [1]
speed = [0.01,0.05,0.1,0.5,1, 2, 4, 8, 16, 32,50,75,100,150,175, 200]
expPrefix=[]
D=0.340
rho=1400
keepPts=100


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
	print "Log file opened - ", fname
	
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

NpAMI = []
NpIBM = []
exp1 = []
exp2 = []
exp3 = []
exp4 = []
NpSRF = []

for iPrefix in prefix:
    for jVisc in viscosity:
        NList = numpy.asarray(speed)/60. * 1400 /jVisc * D *D 
        for kSpeed in speed:
            fname= iPrefix+"_"+str(jVisc)+"_"+str(kSpeed)
            if (iPrefix[0:3]=="IBM") :
	        print "Log file opened - ", fname
                [t,x,y,moment] = numpy.loadtxt(fname,unpack=True)   
                moment = numpy.asarray(moment)*rho
            else :
                [t,momentV,momentP] = readf(fname)
                moment = numpy.asarray(momentV)+numpy.asarray(momentP)
            N =  kSpeed / 60.

            Np = numpy.asarray(moment) *2. *numpy.pi * N / (rho * N**3 * D**5)
            
            
            if (iPrefix[0:3]=="AMI") : NpAMI.extend([numpy.average(Np[-10:-1])])
            if (iPrefix[0:3]=="SRF") : NpSRF.extend([numpy.average(Np[-10:-1])])
             
a=0
for ePrefix in expPrefix:
    fname="../"+ePrefix
    if (a==0): 
        exp1= numpy.loadtxt(fname)
    elif (a==1): 
        exp2=numpy.loadtxt(fname)
    elif (a==2): 
         exp3=numpy.loadtxt(fname)
    elif (a==3): 
        exp4=numpy.loadtxt(fname)
    a+=1

#Plot of Np vs N
ax = plt.figure("Np vs Re") #Create window
plt.ylabel('Np')
plt.xlabel('Re')
plt.title('Np vs Re')

ax = plt.subplot(111)

#plt.plot(NList,NpAMI,'x-', label='AMI - Torque')
plt.plot(NList,NpSRF,'o-', label='SRF - Torque')
#plt.plot(NList,NpIBM,'s-', label='IBM')
#plt.plot(exp1[:,0], exp1[:,1],'-s',label='Experimental results $\mu=10$')
#plt.plot(0.58*exp2[:,0], exp2[:,1],'-s',label='Experimental results $\mu=2.54$')
#plt.plot(5./8.6*exp3[:,0], exp3[:,1],'-s',label='Experimental results $\mu=5$')
#plt.plot(15./32.*exp4[:,0], exp4[:,1],'-s',label='Experimental results $\mu=15$')


ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.xaxis.set_minor_locator(MultipleLocator(1))

ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))

ax.xaxis.grid(True,'minor')
ax.yaxis.grid(True,'minor')
ax.xaxis.grid(True,'major',linewidth=2)
ax.yaxis.grid(True,'major',linewidth=2)

plt.legend(loc=1)
plt.yscale('log')
plt.xscale('log')

if (saveImage):
    plt.savefig("./NpvsRe.png")
if (savePdf):
    plt.savefig("./NpvsRe.pdf")
if (saveTxt):
    N = [numpy.asarray(NList).T, numpy.asarray(NpSRF).T]
    numpy.savetxt("outputMethods", numpy.asarray(N).T, fmt='%.8e', delimiter=' ', newline='\n', header=' Reynolds\t  Np-SRF')

plt.show()

