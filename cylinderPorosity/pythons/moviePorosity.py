# This script animates the volume fraction plot extracted from the porosity fortran tool 
# to create a movie that runs in a singel loop
# 
# The script takes into argument the name of the file you wish to launch it with
#
# Example : python moviePorosity.py particlesInfo_Results
#
# Author : Bruno Blais
# Last modified : 05-03-2014

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
fname =sys.argv[1]

print "R-> %s" %fname
data = numpy.loadtxt(fname, unpack=False, skiprows=8)

nt = numpy.size(data,1)

#Load file to acquire the axis
fig = plt.figure("Void Fraction in time")
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0.0064,0.0238), ylim=(0., 0.9))
ax.grid()
ax.set_ylabel("Fraction of solid")
ax.set_xlabel("Radius")
line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def onClick(event):
    global pause
    pause = True

#Animation function is very coarse right now because it keeps on reloading the text-file to re-acquire the data
#This is obviously far from optimal...
def animate(t):
    print "Plotting iteration : ", t 
    #reload data file completely
    data2 = numpy.loadtxt(fname, unpack=False, skiprows=8)

    #Data is updated. Loading is done
    line.set_data(data2[:,0],1-data2[:,t]) # Update the data
    time_text.set_text(time_template%(t))
    return line,time_text


#Launch the animation itself
ani = animation.FuncAnimation(fig, animate,range(1,nt,1), blit=True, init_func=init)

#Render stage
plt.show()

