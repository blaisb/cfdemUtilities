###############################################################################
#
#   File    : analysePressure.py
#
#   Run Instructions    : python analysePressure.py directory/with/the/files
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
#-------------------------------

#=====================
#   Main plot
#=====================

if (len(sys.argv)<2) :
    print "You need to enter a file argument"


for i,arg in enumerate(sys.argv):
    if (i>=1):
        print i, arg
        N,p = numpy.loadtxt(arg, unpack=True)
        sortIndex=numpy.argsort(N)
        NS=N[sortIndex]
        pS=p[sortIndex]
        plt.plot(NS,pS,'-s', label=arg)




plt.ylabel('Pressure at the bottom of the tank [Pa]')
plt.xlabel('Speed N[$s^{-1}$]')
plt.legend(loc=9)
plt.show()

