#This program is a simple calculator to obtain kp from a given power value

# USAGE : python ./kp.py value

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
N=2./60.
D=0.21

P = float(sys.argv[1])
kp = P/(N**2 * D**3*mu)
print "La valeur de Kp est de :  %5.5e" %kp
