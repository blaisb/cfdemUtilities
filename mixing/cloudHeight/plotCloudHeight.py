###############################################################################
#
#   File    : analysePressure.py
#
#   Run Instructions    : python plotPressure.py directory/with/the/files
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the files in a folder and output
#                   a two column file that is N vs P
#
#
###############################################################################

#Python imports
#-------------------------------
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys
import pylab 

#-------------------------------


#=====================
# User parameters
#=====================
fTag="out_averaged_x"
datN=[]
datH=[]

# Figures
plt.rcParams['figure.figsize'] = 10, 7
params = {'backend': 'ps',
             'axes.labelsize': 20,
             'text.fontsize': 16,
             'legend.fontsize': 18,
             'xtick.labelsize': 16,
             'ytick.labelsize': 16,
             'text.usetex': True,
             }
plt.rcParams.update(params)

#=====================
#   Main plot
#=====================

if (len(sys.argv)<2) :
    print "You need to enter a file argument"



# Suspended solid fraction analysis
print "*********************************"
print "Cloud Height analysis"
print "*********************************"

folder=sys.argv[1]
folderContent=os.listdir(sys.argv[1])
for i,arg in enumerate(numpy.sort(folderContent)):
    fname="./"+folder+"/"+arg+"/"+fTag
    temp=numpy.loadtxt(fname,unpack=True,comments="#",skiprows=1)
    t=temp[0,:]
    Ht=temp[-2,:]
    sortIndex=numpy.argsort(t)
    ts=t[sortIndex]
    Hs=Ht[sortIndex]
    H=numpy.average(Ht[-10:])
    datH.append(H)
    datN.append(float(arg))


#Experimental data
fexp="experimentalData"
Nexp,Hexp=numpy.loadtxt(fexp,unpack=True,skiprows=1)


fig = plt.figure()
ax = fig.add_subplot(111) 

plt.ylabel('Cloud Height [m]')
plt.xlabel('Impeller Speed $N$ [RPM]')
plt.plot(datN,datH,'-o',label="Simulations")
plt.plot(Nexp,Hexp,'-s',label="Experimental")

plt.legend(loc=4)
plt.show()

