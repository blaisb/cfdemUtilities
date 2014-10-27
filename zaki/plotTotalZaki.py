#This program makes the plot for the average velocity of the particles in a the Z direction for 
# a single case

# Author : Bruno Blais
# Last modified : December 3rd

#Python imports
import os
import sys
import math
import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FormatStrFormatter
import pylab 

#=====================
#   Main plot
#=====================

fname=sys.argv[1]

#INPUT
print "R-> %s" %fname
np, u,v,w, unorm, wStd, wMax, wMin = numpy.loadtxt(fname, unpack=True)

#Stokes solutions for a single sphere unsteady solution
dt = 2e-6	# time step of the simulation
rhof = 100.	# fluid density
rhos = 110.	# solid density
g = -10.	# gravity
dp = 0.0005	# particle diameter
mu = 0.0001	# viscosity of the fluid	
b= 18 * mu / (rhos * dp**2)
vt =  (rhos-rhof) * g * dp**2/18/mu * np / np # transient terminal velocity. Not so sure of the solution here

#Length of the geometry
x=0.05
y=0.05
z=0.25

#Volume of the geometry
vGeom=x*y*z
#Volume of a single particle
vPart = 4*math.pi/3 * (dp/2)**3

#Calculation of the volume fraction
phi =  1- np * vPart/vGeom  
w = abs(w)

#plt.rcParams.update({'font.size': 10})

fig = plt.figure()
ax = fig.add_subplot(111) # Create plot object
ax.errorbar(numpy.log(phi),numpy.log(w),yerr=wStd,fmt='ro', label="Average velocity", markeredgewidth=1)
#ax.plot(phi,wMin,'bo', label="Minimal velocity")
#ax.plot(phi,wMax,'go', label="Maximal velocity")

plt.ylabel('Average settling velocity [m/s]')
plt.xlabel('Log Volume Fraction ($\phi$)')
plt.title('Log Average velocity of the particles as a function of the volume fraction of particles')
plt.legend(loc=9)
#plt.yscale('log')
#plt.xscale('log')

a,b = numpy.polyfit(numpy.log(phi),numpy.log(w),1)
ax.plot(numpy.log(phi),numpy.log(phi)*a+b,label="Linear regression")

print "Origin : ", b, "  Slope : ", a

x1,x2,y1,y2 = plt.axis()
#plt.axis((0.1,1,y1,y2))

#Change tick sizes
#ax.tick_params('both', length=5, width=2, which='major')
#ax.tick_params('both', length=5, width=2, which='minor')

#Create 5 minor ticks between each major tick
#minorLocator=LogLocator(subs=numpy.linspace(2,10,6,endpoint=False))

#Format the labels
majorFormatter= FormatStrFormatter('%5.4f')

#Apply locator
#ax.xaxis.set_minor_locator(minorLocator)

#Modify y fontsizpythoe
#pylab.yticks(fontsize=40)
#matplotlib.rc('ytick.major', size=100)
plt.show()

