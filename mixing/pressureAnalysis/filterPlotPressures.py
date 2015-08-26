####################################################################################
#
#   File    : filterPlotPressure.py
#
#   Run Instructions    : python filterPlotPressure.py directory/with/the/pressures
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the pressures in a folder and make
#                   a pressure vs time plot with a filter on
#
#
####################################################################################



#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter,freqz
#----------------



#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
pdf=True
plotRaw=False
cutoff=0.300
fs=5.
filterOrder=3
manual=False


# Figures parameters
plt.rcParams['figure.figsize'] = 14, 9
params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 16,
             'legend.fontsize': 19,
             'xtick.labelsize': 20,
             'ytick.labelsize': 20,
             'text.usetex': True,
             }
plt.rcParams.update(params)



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
if (len(sys.argv)<2) :
    print "You need to enter a folder argument"

folder=sys.argv[1]


# Acquire list of time step
speedFolder=os.listdir(folder)

# Sort so that time will already be sorted
speedFolder.sort() 


#Initiate figure 
ax=plt.figure("Data and filter")
axp = ax.add_subplot(111) 
plt.ylabel('Pressure at the bottom [Pa] ')
plt.xlabel('Time [s]')
#plt.title('Frequency spectrum of $C_L$  ')
#plt.yscale('log')
#plt.xscale('log')

# Loop through all times
for k,i in enumerate(speedFolder):

    print "Opening ", i
    t,p = numpy.loadtxt(folder+"/"+i, unpack=True,comments="#")
    tempString= i.split("_")
    sortIndex=numpy.argsort(t)
    N=(tempString[-2])
    if (float(N)>1000): N=(tempString[-1])
    t=t[sortIndex]
    pS=p[sortIndex]
    pF=butter_lowpass_filter(pS,cutoff,fs,order=filterOrder)
    if (plotRaw): axp.plot(t, pS,'ko', label='Brute signal - ' +N+ ' RPM'+i,mfc='none')
    
    if (float(N)>510): 
        axp.plot(t, pF,'--', label=N + ' RPM',linewidth=3.5)#,color=(0,(k-12)/6.,0,1))
    elif (float(N)<360):
        axp.plot(t[::6], pF[::6],'^',markeredgecolor='none', label=N + ' RPM',linewidth=3.5)
    
    else:
        axp.plot(t, pF, label=N + ' RPM',linewidth=3.5)
    #col=k/float(len(speedFolder))
    #axp.plot(t,pF,label=N+ ' RPM', linewidth=3.0, color=(col,0,0, 1))

box = axp.get_position()
axp.set_position([box.x0, box.y0, box.width * 0.9, box.height])
plt.legend(loc='center left', bbox_to_anchor=(1., 0.5))
plt.ylim([-10,550])
#plt.xlim([0,200])
axp.grid(b=True, which='major', color='k', linestyle='--') 
if (pdf): plt.savefig("./filterPressure.pdf")
plt.show()
