#This program is a simple calculator to obtain kp from a given power value

# USAGE : python ./kp.py TorquePressure TorqueViscosity

# Author : Bruno Blais
# Last modified : 10-02-2014

#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
#----------------
mu=1
rho = 1400
N=60./60.
D=0.127

P = (float(sys.argv[1]) + float(sys.argv[2])) * 2 * numpy.pi * N
Re = N * D * D / mu * rho
kp = P/(N**2 * D**3*mu)
print "La valeur de Kp est de :  %5.5e" %kp
print "La valuer de Np est de :  %5.5e" %(kp/Re)
print "La valuer de Re est de :  %5.5e" %(Re)
print "La valuer de P est de :  %5.5e" %(P)
