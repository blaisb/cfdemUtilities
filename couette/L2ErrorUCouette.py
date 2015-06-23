# This programs calculates the L2 error for a given velocity file
#
# Usage : python L2ErrorUCouette.py Velocity file
#
# Author : Bruno Blais
# Last modified : December 3rd


#Python imports
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#***********************************
# Parameters for analytical solution
#***********************************
omega = 0.1000
R=0.1
k = 1./4.;
analyseShear=False
analysePseudo=True


#===========================
# Main program
#===========================

fname = sys.argv[1]
nx = int(sys.argv[2])

# read the file
#print "R-> Velocity file has been read"
if analysePseudo:
    [x,y,z,u,v,w,p,V,pseudo] = numpy.loadtxt(fname, unpack=True)
elif analyseShear:
    [x,y,z,u,v,w,p,V,shear] = numpy.loadtxt(fname, unpack=True)
else:
    [x,y,z,u,v,w,p,V] = numpy.loadtxt(fname, unpack=True)

r = numpy.sqrt(x**2 + y**2)
ut = numpy.sqrt(u**2 + v**2)

#Analytical solution for theta velocity 
rplot=[]
errU =[]
errV=[]
errS=[]
for i in range(0,len(r)):
    if (r[i]>k*R and r[i] < R):
        uth = omega *k* R * (-r[i]/(R) + (R)/r[i]) / (1/k - k)
        rplot.append([r[i]])
        errU.append([V[i]*(ut[i]-uth)**2])
        errV.append([V[i]])
        
        
        if(analyseShear):
            shearth=2*(-2 * omega * (R/r[i])**2 * (k**2/(1-k**2)))**2
            errS.append([V[i]*(shear[i]-shearth)**2])
        if(analysePseudo):
            pseudoth=16 * 2*(-2 * omega * (R)**2 * (k**2/(1-k**2)))**2 * r[i]**(-6)
            errS.append([V[i]*(pseudo[i]-pseudoth)**2])
            #print "Pseudo, pseudo th  : ", pseudo[i], pseudoth, r[i]
nt = len(errU)

L2errU = numpy.sqrt(numpy.sum(errU) / numpy.sum(errV)) / omega / R

if (analyseShear or analysePseudo):
    L2errS = numpy.sqrt(numpy.sum(errS) / numpy.sum(errV)) / omega

if (analyseShear or analysePseudo):
    print "%i %5.5e %5.5e" %(nx, L2errU,L2errS)
else:
    print "%i %5.5e" %(nx, L2errU)
