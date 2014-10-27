#This program makes the plot for the average velocity of the particles in a the Z direction for 
# a single case

# Author : Bruno Blais
# Last modified : December 3rd

#Python imports
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys

#*********************
# Parameters
#*********************

A=0.167
g=10
tmin=0.26



#=====================
#   Main plot
#=====================

fname=sys.argv[1]

#INPUT
print "R-> %s" %fname
t,h,hmin,hmax = numpy.loadtxt(fname, unpack=True)

plt.figure(fname)
plt.plot(t,numpy.sqrt(h/(A*g)),'-o')
x1,x2,y1,y2 = plt.axis()
#y2+=0.001
#y1 -=0.001
plt.axis((x1,x2,y1,y2))

# Find data over tmin
index=numpy.where(t > tmin)
# Regression over the data range of interest
a,b = numpy.polyfit(t[index],numpy.sqrt(h[index]/(A*g)),1)
plt.plot(t[index],t[index]*a+b,label="Linear regression")
print "Origin : ", b, "  Slope ^2 : ", a**2

plt.ylabel('$(h/Ag)^{1/2}$')
plt.xlabel('Time (s)')
plt.title('Growth rate of the mixing width')
plt.show()

