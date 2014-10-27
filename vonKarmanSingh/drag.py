# This program analyses the X and Y drag coefficient (drag and lift) from the cylinder immersed
# boundary test cases 
# It can be compared visually afterward to experimental data
# Currently is not generic and can only load 2 data set, but anyway more makes it an unreadable mess
# 
# USAGE : python ./FOLDERWHEREDATA-1-IS ./FOLDERWHEREDATA-2-IS 
#
# Author : Bruno Blais

#Python imports
#----------------
import os
import sys
import numpy
import time
import scipy
import matplotlib.pyplot as plt
import re 
#----------------

#TODO
# - Make everything in a single loop instead

#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
skip=50
tminFFT=0.

#======================
#   MAIN
#======================
tFold= 0

#Read the logs files
if (len(sys.argv)<1):
    print 'Folder must be specified when running this python script'
    sys.exit("Crashed because folder was not specified")

if (len(sys.argv)>3):
    print 'Too many arguments, only the first two folders will be post-processed'

folder = [sys.argv[1], ' ']
if (len(sys.argv)>2):
    tFold=  1
    folder = [sys.argv[1], sys.argv[2]]


tx1, dx1 = numpy.loadtxt(folder[0]+'/dragX', unpack=True)
ty1, dy1 = numpy.loadtxt(folder[0]+'/dragY', unpack=True)

# Take absolute value
dx1= numpy.abs(dx1)

index = numpy.where(ty1>tminFFT)

# Manual FFT to get amplitude and frequencies right!
Fs = 1. / (tx1[2]-tx1[1]) # Sampling frequency
df = 1. /  ty1[-1]
N= len(dy1[index]) # Number of points

# First normalise the amplitude with respect to the number of points
spectrum = abs(numpy.fft.fft(dy1[index])) / N
f1 = numpy.arange(0.,Fs/2.-df,df)

# Keep positive part of the FFT spectrum
Nf = (N)/2
spectrum1 = 2 * spectrum[0:len(f1)]

if (tFold):
    tx2, dx2 = numpy.loadtxt(folder[1]+'/dragX', unpack=True)
    ty2, dy2 = numpy.loadtxt(folder[1]+'/dragY', unpack=True)
    index = numpy.where(ty2>tminFFT)

    # Take absolute value
    dx2= numpy.abs(dx2)

    # Manual FFT to get amplitude and frequencies right!
    Fs = 1. / (tx2[2]-tx2[1]) # Sampling frequency
    df = 1. /  ty2[-1]
    N= len(dy2[index]) # Number of points

    # First normalise the amplitude with respect to the number of points
    spectrum = abs(numpy.fft.fft(dy2[index])) / N

    f2 = numpy.arange(0.,Fs/2.-df,df)

    # Keep positive part of the FFT spectrum
    Nf = (N)/2
    spectrum2 = 2 * spectrum[0:len(f2)]

# Plotting stage
axfft=plt.figure("FFT C_L")
plt.ylabel(' FFT $C_L$ ')
plt.xlabel('Strouhal Number ($St$)')
plt.title('Frequency spectrum of $C_L$  ')
plt.yscale('log')
plt.xscale('log')

if (tFold ==0):
    plt.plot(f1,spectrum1)
if (tFold ==1):
    plt.plot(f1,spectrum1,f2,spectrum2)

ax = plt.figure("Drag coefficient") #Create window
plt.ylabel('$C_D$, $C_L$ ')
plt.xlabel('time [s]')
plt.title('Drag coefficients with time for 2D Kelvin-Helmholtz ')

if (tFold ==0):
    plt.plot(tx1[skip:],2*dx1[skip:],'-', label='$C_D$')
    plt.plot(ty1[skip:],-2*dy1[skip:],'-', label='$C_L$')
if (tFold ==1):
    plt.plot(tx1[skip:],2*dx1[skip:],'-', label=('$C_D$-'+sys.argv[1]))
    plt.plot(ty1[skip:],-2*dy1[skip:],'-', label=('$C_L$-'+sys.argv[1]))
    plt.plot(tx2[skip:],2*dx2[skip:],'-', label=('$C_D$-'+sys.argv[2]))
    plt.plot(ty2[skip:],-2*dy2[skip:],'-', label=('$C_L$-'+sys.argv[2]))

plt.legend(loc=1)
plt.show()
