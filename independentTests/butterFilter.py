# This program is a prototype to test the low pass butterWorth filter
# 
# USAGE : python butterFilter.py 
#
# Author : Bruno Blais

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
pdf=False
cutoff=0.050
fs=1
lorder=5

# Figures
plt.rcParams['figure.figsize'] = 10, 7
params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 16,
             'legend.fontsize': 18,
             'xtick.labelsize': 16,
             'ytick.labelsize': 16,
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
#Generate random data set
x=numpy.linspace(0,1,1000)
y=x*x*30+3*(numpy.random.random_sample([len(x)])-0.5)

# Plotting stage
ax=plt.figure("Data and filter")
axp = ax.add_subplot(111) 
plt.ylabel(' Y ')
plt.xlabel('X')
#plt.title('Frequency spectrum of $C_L$  ')
#plt.yscale('log')
#plt.xscale('log')
plt.plot(x,y,'sk',linewidth=2.0,mfc='none')

z = butter_lowpass_filter(y, cutoff, fs, order=lorder)
plt.plot(x, z, label='Filtered signal',linewidth=4.0)
plt.plot(x,x*x*30,'-r',label='Real signal',linewidth=3.0)
axp.grid(b=True, which='major', color='k', linestyle='--') 
if (pdf): plt.savefig("./fftOnCylinder.pdf")
plt.show()

# Plot the frequency response.
b, a = butter_lowpass(cutoff, fs, lorder)

w, h = freqz(b, a, worN=8000)
plt.plot(0.5*fs*w/numpy.pi, numpy.abs(h), 'b')
plt.plot(cutoff, 0.5*numpy.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.show()

