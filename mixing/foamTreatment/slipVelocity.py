#------------------------------------------------------------------------------------------------------------
#
#   This program plots the slip (up-u) velocity and the particle Reynolds number
#
#   Requirements: functionAverage.py 
# 
#   Usage : python probefolder "Mode"(vector or re)
#
#   Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import os
import sys
import numpy
import math
import matplotlib.pyplot as plt
from matplotlib import ticker 
#----------------

#================================
#   USER DEFINED VARIABLES  
#================================
pdf=False
contour=True
nContour=20
paperMode=False
impeller=True
impellerType="pbtTs4"
vmax=0.5
vmin=0.
saturate=True

mu=1
dp=0.003
rhof=1400

#Functions for the averaging
from functionAverage import *

#===============================
#   FIGURE OPTIONS
#===============================
#Figure size
plt.rcParams['figure.figsize'] = 17, 8

params = {'backend': 'ps',
             'axes.labelsize': 26,
             'axes.titlesize': 26,
             'text.fontsize': 20,
             'legend.fontsize': 20,
             'xtick.labelsize': 22,
             'ytick.labelsize': 22,
             'text.usetex': True,
             }
   
plt.rcParams.update(params)



#================================
#   MAIN
#================================

try:
    folder=sys.argv[1]
    mode=sys.argv[2]
except:
    print "Insufficient number of arguments, need two files names"

#rl,zl,u=vectorAverageBody(folder+"/U",folder+"/body",impeller,impellerType)
#rl,zl,up=vectorAverageBody(folder+"/Us",folder+"/body",impeller,impellerType)
rl,zl,u=vectorAverage(folder+"/U",impeller,impellerType)
rl,zl,up=vectorAverage(folder+"/Us",impeller,impellerType)
extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl))

acc=up-u

#If up is exactly 0 it means there are no particles within the cell, for sure
for i in range(0,numpy.size(up,0)):
    for j in range(0,numpy.size(up,1)):
        if (abs(up[i,j,0]) + abs(up[i,j,1]) + abs(up[i,j,2]) <1e-10):
            acc[i,j,:]=0.


# The variable is a vector bro-dude-migo
if (mode=="vector"):
    
    # Make the graph of the three coordinates:
    # Radial graph
    plt.figure()
    plt.subplots_adjust(left=0.07, bottom=0.07, right=0.95, top=0.94, wspace=0.35)
    plt.subplot(1,3,1)
    if paperMode:
        plt.imshow(acc[:,:,0],extent=extent,origin='lower',interpolation="bicubic",vmin=-0.5,vmax=1.5)
    else:
        plt.imshow(acc[:,:,0],extent=extent,origin='lower',interpolation="bicubic")
  
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
    plt.title("Radial velocity")
    cbar = plt.colorbar( drawedges=False)
    tick_locator = ticker.MaxNLocator(nbins=4)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.ax.tick_params(labelsize=20) 
    cbar.solids.set_edgecolor("face")


    # Azimuthal graph
    plt.subplot(1,3,2) 
    plt.imshow(acc[:,:,1],extent=extent,origin='lower',interpolation="bicubic")
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
    plt.title('Azimuthal velocity' )
    cbar = plt.colorbar( drawedges=False)
    tick_locator = ticker.MaxNLocator(nbins=6)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.ax.tick_params(labelsize=20) 
    cbar.solids.set_edgecolor("face")

    # Axial graph
    plt.subplot(1,3,3)
    plt.title("Axial velocity")
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
    if paperMode:
        plt.imshow(acc[:,:,2],extent=extent,origin='lower',interpolation="bicubic",vmin=-1.,vmax=1.)
    else:
        plt.imshow(acc[:,:,2],extent=extent,origin='lower',interpolation="bicubic")
       
    cbar = plt.colorbar( drawedges=False)
    tick_locator = ticker.MaxNLocator(nbins=4)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.ax.tick_params(labelsize=20) 
    cbar.solids.set_edgecolor("face")
    
    # Time to display some stuff
    if (pdf): plt.savefig("./velocity_prof.pdf")

#-------------------
# Scalar graphic!
#-------------------


if (mode=="re"):
    
    plt.figure(figsize=(6,8))
    plt.subplots_adjust(left=0.02, bottom=0.09, right=0.95, top=0.94, wspace=0.15)
    plt.subplot(1,1,1)
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
    
    re= numpy.sqrt(acc[:,:,0]**2. + acc[:,:,1]**2 + acc[:,:,2]**2)
    re = re *dp/mu*rhof
    for i in (range(0,numpy.size(re,0))):
            for j in (range(0,numpy.size(re,1))):
                if(re[i,j]<1e10):
                    re[i,j]=min(vmax,re[i,j])



    if(contour):
        maxdiff=min(numpy.nanmax(re),vmax)
        mindiff=max(numpy.nanmin(re),vmin)
        levels = numpy.arange(mindiff, maxdiff+tol, (maxdiff-mindiff)/nContour)
        CS=plt.contourf(re, levels, hold='on',# colors = 'k',
            origin='lower', extent=extent)
        #plt.clabel(CS, inline=1, fontsize=14,colors="white")
    else:
        plt.imshow(re[:,:],extent=extent,origin='lower',interpolation="bicubic")
    
    if (len(sys.argv)>3):
        plt.title("%s" %(sys.argv[3]))
    else:
        plt.title("%s" %(sys.argv[1]))


    cbar = plt.colorbar( drawedges=False)
    tick_locator = ticker.MaxNLocator(nbins=7)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.ax.tick_params(labelsize=20) 
    cbar.solids.set_edgecolor("face")
    if (pdf): plt.savefig("./voidfraction_prof.pdf")
plt.show() 


