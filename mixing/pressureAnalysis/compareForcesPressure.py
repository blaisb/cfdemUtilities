##################################################################################################
#
#   File    : compareForcesPressure.py
#
#   Run Instructions    : python compareForcesPressure.py directory/with/the/pressures Velocity
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the pressure with velocity N in a folder
#                   Filters them using a low pass butterworth filter
#                   Then plots them in a single comparison
#
#
##################################################################################################



#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter,freqz
from itertools import cycle
#----------------



#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
pdf=True
plotRaw=False
cutoff=0.300
fs=5.
filterOrder=3

#*******************************
# List of forces
#*******************************
forces={"std"  : "Standard ",
        "lift" : "Lift Force",
        #"drag" : "Only Drag",
        "visc" : "No Visc force",
        "p" : "No Pressure force"}

suffix="Forc_1_1e8_0.90_148700_"



# Figures parameters
plt.rcParams['figure.figsize'] = 12, 9
params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 20,
             'legend.fontsize': 19,
             'xtick.labelsize': 20,
             'ytick.labelsize': 20,
             'text.usetex': True,
             }
plt.rcParams.update(params)

lines = ["-.","-","--",":"]
lineCycler = cycle(lines)
colors = ["g","c","r","k"]
colorCycler = cycle(colors)


#=======================
#   Functions
#=======================
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

#======================
#   MAIN
#======================

# Directory to work within
try:
    folder=sys.argv[1]
except:
    print "You need a folder argument"

# Velocity to analyse
try:
    N=sys.argv[2]
except:
    print "You need a velocity argument"

#Initiate figure 
ax=plt.figure("Data and filter")
axp = ax.add_subplot(111) 
plt.ylabel('Pressure at the bottom [Pa] ')
plt.xlabel('Time [s]')

# Loop through all times
for i in forces:
    print "Opening ", i
    t,p = numpy.loadtxt(folder+"/"+i+ suffix+ str(N), unpack=True,comments="#")
    sortIndex=numpy.argsort(t)
    t=t[sortIndex]
    pS=p[sortIndex]
    pF=butter_lowpass_filter(pS,cutoff,fs,order=filterOrder)
    if (plotRaw): axp.plot(t, pS,'ko', label='Brute signal - ' +N+ ' RPM'+i,mfc='none')
    axp.plot(t, pF,next(lineCycler),color=next(colorCycler), label=forces[i],linewidth=5)

#box = axp.get_position()
#axp.set_position([box.x0, box.y0, box.width * 0.9, box.height])
#plt.legend(loc='center left', bbox_to_anchor=(1., 0.5))
plt.legend(loc='best')
#plt.ylim([-10,550])
#plt.xlim([0,200])
axp.grid(b=True, which='major', color='k', linestyle='--') 
if (pdf): plt.savefig("./compareForces_"+str(N)+".pdf")
plt.show()
