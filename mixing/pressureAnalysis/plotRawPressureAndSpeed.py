# This program makes the plot of the pressure at the bottom of the tank with function of time and velocity
# for the falling particle unit test cases

# Author : Bruno Blais

#Python imports
import math
import numpy
import sys
import operator
import matplotlib.pyplot as plt

#================================
#   Graphical properties
#================================

plt.rcParams['legend.numpoints'] = 1
params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 28,
             'legend.fontsize': 17,
             'xtick.labelsize': 15,
             'ytick.labelsize': 15,
             'text.usetex': True,
             }
plt.rcParams.update(params)


#=====================
#   Main 
#=====================

if (len(sys.argv) <2):
    raise Exception("This program requires one file argument")

fname=sys.argv[1]

# Load input file
print "R-> %s" %fname
t,N,P = numpy.loadtxt(fname, unpack=True)

fig, ax1=plt.subplots()
ax1.plot(t,P,'bo', label="Pressure")
plt.ylabel('Pressure at the bottom of the tank [Pa]')
plt.xlabel('time [s]')
plt.legend()

ax2=ax1.twinx()
ax2.plot(t,N,'g', label="Velocity",linewidth=3.0)
plt.ylabel('Impeller velocity - N [1/s]')
ax1.legend(loc=1)
ax2.legend(loc=2)
plt.show()
