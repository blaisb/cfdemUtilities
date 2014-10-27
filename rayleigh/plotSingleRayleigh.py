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

#=====================
#   Main plot
#=====================

fname=sys.argv[1]

#INPUT
print "R-> %s" %fname
z,phi = numpy.loadtxt(fname, unpack=True)
phi = abs(1-phi)

plt.figure(fname)
plt.plot(z,phi,'-o')
x1,x2,y1,y2 = plt.axis()
y2+=0.001
y1 -=0.001
plt.axis((x1,x2,y1,y2))

plt.ylabel('Volume fraction of particles $\phi$')
plt.xlabel('Vertical position Z [m]')
plt.title('Average volume fraction of particle for different heights')
plt.show()

