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

#***************************
# Case chooser
#***************************
case = "finalVANS"
# Possible cases, void1, swirlVans, expVans, nonFreeDiv, unsteadyNS, finalVANS

#Amplitude of velocity field
A =0.01
#===========================
# Main program
#===========================

fname = sys.argv[1]
nx = sys.argv[2]
pi = numpy.pi


# read the file
#print "R-> Velocity file has been read"
[x,y,z,u,v,w] = numpy.loadtxt(fname, unpack=True)

nt = len(x)
nx = int(numpy.sqrt(nt))
uth = numpy.zeros([nt])
vth = numpy.zeros([nt])
#Analytical solution for theta velocity in eulerian frame of reference

if case=="void1":
    for i in range(0,nt):
	uth[i] =  -2 * numpy.sin(pi*x[i])**2 * numpy.sin(pi*y[i]) * numpy.cos(pi*y[i])
	vth[i] = 2 * numpy.sin(pi*y[i])**2 * numpy.sin(pi*x[i]) * numpy.cos(pi*x[i])

if case=="swirlVANS":
    for i in range(0,nt):
	uth[i] =  -2 *A* numpy.sin(pi*x[i]) * numpy.cos(pi*y[i])
	vth[i] = 2 *A* numpy.sin(pi*y[i]) * numpy.cos(pi*x[i])

if case=="expVANS":
    for i in range(0,nt):
	uth[i] =  A * numpy.cos(x[i]*y[i]) 
	vth[i] = -A * numpy.sin(x[i]*y[i])

if case=="nonFreeDiv":
    for i in range(0,nt):
    	uth[i] =  A * numpy.exp(-x[i]**2) * numpy.sin(pi*y[i]) * numpy.cos(pi*y[i]) 
	vth[i] = A * numpy.exp(-y[i]**2) * numpy.sin(pi*x[i]) * numpy.cos(pi*x[i])


if case=="unsteadyNS":
    for i in range(0,nt):
	uth[i] =  -2 * numpy.sin(pi*x[i])**2 * numpy.sin(pi*y[i]) * numpy.cos(pi*y[i]) * numpy.cos(numpy.pi/4.)
	vth[i] = 2 * numpy.sin(pi*y[i])**2 * numpy.sin(pi*x[i]) * numpy.cos(pi*x[i]) * numpy.cos(numpy.pi/4.)

if case=="finalVANS":
    for i in range(0,nt):
    	uth[i] =  A * numpy.exp(-x[i]**2) * numpy.sin(pi*y[i]) * numpy.cos(pi*y[i]) * numpy.cos(numpy.pi/4.)
	vth[i] = A * numpy.exp(-y[i]**2) * numpy.sin(pi*x[i]) * numpy.cos(pi*x[i]) * numpy.cos(numpy.pi/4.)

err = ((u-uth)**2 + (v-vth)**2)/A**2
L2err = numpy.sqrt(numpy.sum(err)/nt)
print "%i %5.5e" %(nx,L2err)

