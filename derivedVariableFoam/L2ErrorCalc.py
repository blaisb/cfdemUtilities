# This programs calculates the L2 error for a given velocity file
#
# Usage : python L2ErrorUCouette.py Velocity file
#
# Author : Bruno Blais
# Last modified : December 3rd


#Python imports
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#***********************************
# Parameters for analytical solution
#***********************************

#===========================
# Main program
#===========================

fname = sys.argv[1]
nx = int(sys.argv[2])

# read the file
#print "R-> Velocity file has been read"
[x,y,z,p,psi,xi,V] = np.loadtxt(fname, unpack=True)

pi=np.pi

#Stocking variable for error calculations
errP =[]
errV=[]
errPsi=[]
errXi=[]
for i in range(0,len(x)):
    pT = np.sin(pi*x[i])*np.sin(pi*y[i])
    psiT = - 2*np.sin(pi*x[i]) * np.sin(pi*y[i]) 
    xiT =  4*np.sin (pi*x[i]) * np.sin(pi*y[i])
    errPsi.append([V[i]*(psi[i]-psiT)**2])
    errXi.append([V[i]*(xi[i]-xiT)**2])
    errV.append([V[i]])

L2errPsi = np.sqrt(np.sum(errPsi) / np.sum(errV))
L2errXi = np.sqrt(np.sum(errXi) / np.sum(errV))

print "%i %5.5e %5.5e" %(nx, L2errPsi,L2errXi)
