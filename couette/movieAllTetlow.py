# This script animates an averaged variable in time, Notably in the Telow case for the void fraction
#
# A FOLDER ./voidfraction/averaged must exist!

# Author : Bruno Blais
# Last modified : 24-02-2014

#Python imports
#----------------
import os
import sys
import numpy 
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#----------------

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************

#Initial time of simulation, final time and time increment must be specified by user
t0=2.0
tf=100.
dT=0.5
nt=int((tf-t0)/dT)
t=t0

#Number of r  and z cells has to be specified
nz=1
nr = 10

#Load first file to acquire the axis
print "Acquiring time : ", t0
fname='./voidFraction/averaged/radialVoidFraction_' + str(t0)
r,phi = numpy.loadtxt(fname, unpack=True) # Load data from text file

fig = plt.figure("Void Fraction in time")
ax = fig.add_subplot(111, autoscale_on=False, xlim=(min(r)-0.001,max(r)+0.001), ylim=(0.1, 0.8))
ax.grid()
ax.set_ylabel("Fraction of solid")
ax.set_xlabel("Radius")
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#plt.ylabel('Fraction of solid')
#plt.xlabel('Radius (r)')
#plt.legend(loc=9)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def onClick(event):
    global pause
    pause ^= True

def animate(t):
    print "Plotting time : ", t
    fname='./voidFraction/averaged/radialVoidFraction_' + str(t)
    r,phi = numpy.loadtxt(fname, unpack=True) # Load data from text file
    line.set_data(r,1-phi) # Update the data
    time_text.set_text(time_template%(t))
    return line,time_text

ani = animation.FuncAnimation(fig, animate,numpy.arange(2,100,0.5), blit=True, init_func=init)

plt.show()

