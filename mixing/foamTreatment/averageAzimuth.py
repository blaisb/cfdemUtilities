#------------------------------------------------------------------------------------------------------------
#
# This program averages openfoam probe data azimuthally. If variable is a scalar it also outputs the std-dev 
# 
# Output format : velocity : r z ux uy uz ur ut uz
#                 scalar   : r z scalar                  
#
# Usage : python UProbefile
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import os
import sys
import numpy
import math
import matplotlib.pyplot as plt
from matplotlib import ticker #Manually change number of tick bro
#----------------

#================================
#   USER DEFINED VARIABLES  
#================================
pdf=True
tol=1e-4
paperMode=True
impeller=True
impellerType="pbtTs4"
contour=False
nContour=100

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
    fname=sys.argv[1]
    mode=sys.argv[2]
except:
    print "Insufficient number of arguments, need two files names"

# The variable is a vector bro-dude-migo
if (mode=="velocity"):
    
    rl,zl,acc=vectorAverage(fname,impeller,impellerType)

# Make the graph of the three coordinates:

    # Radial graph
    plt.figure()
    plt.subplots_adjust(left=0.07, bottom=0.07, right=0.95, top=0.94, wspace=0.35)
    plt.subplot(1,3,1)
    if paperMode:
        plt.imshow(acc[:,:,0],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic",vmin=-0.5,vmax=1.5)
    else:
        plt.imshow(acc[:,:,0],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic")
  
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
    plt.imshow(acc[:,:,1],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic")
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
        plt.imshow(acc[:,:,2],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic",vmin=-1.,vmax=1.)
    else:
        plt.imshow(acc[:,:,2],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic")
       
    cbar = plt.colorbar( drawedges=False)
    tick_locator = ticker.MaxNLocator(nbins=4)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.ax.tick_params(labelsize=20) 
    cbar.solids.set_edgecolor("face")
    
    # Time to display some stuff
    if (pdf): plt.savefig("./velocity_prof.pdf")
    plt.show()
   

#-------------------
# Scalar graphic!
#-------------------


if (mode=="scalar"):
    
    rl,zl,acc,dev=scalarAverage(fname,impeller,impellerType)

    plt.figure(figsize=(12,8))
    plt.subplots_adjust(left=0.02, bottom=0.09, right=0.95, top=0.94, wspace=0.15)
    plt.subplot(1,2,1)
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
  
    extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl))
    plt.imshow(acc[:,:],extent=extent,origin='lower',interpolation="bicubic",vmin=0.4,vmax=1.)
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

    if(contour):
        maxdiff=numpy.nanmax(acc)
        mindiff=numpy.nanmin(acc)
        levels = numpy.arange(mindiff, maxdiff+tol, (maxdiff-mindiff)/nContour)
        CS=plt.contourf(acc, levels, hold='on',# colors = 'k',
            origin='lower', extent=extent)
        #plt.clabel(CS, inline=1, fontsize=14,colors="white")


    plt.subplot(1,2,2)
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
    plt.imshow(dev[:,:],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic")#,vmax=0.05)
    if (len(sys.argv)>3):
        plt.title("%s - std. dev." %(sys.argv[3]))
    else:
        plt.title("%s - std. dev." %(sys.argv[1]))

    cbar = plt.colorbar( drawedges=False)
    tick_locator = ticker.MaxNLocator(nbins=6)
    cbar.locator = tick_locator
    cbar.update_ticks()
    cbar.ax.tick_params(labelsize=20) 
    cbar.solids.set_edgecolor("face")


    if(contour):
        maxdiff=numpy.nanmax(dev)
        mindiff=numpy.nanmin(dev)
        levels = numpy.arange(mindiff, maxdiff+tol, (maxdiff-mindiff)/nContour)
        CS=plt.contourf(dev, levels, hold='on',# colors = 'k',
            origin='lower', extent=extent)
        #plt.clabel(CS, inline=1, fontsize=14,colors="white")


    if (pdf): plt.savefig("./voidfraction_prof.pdf")
    plt.show()
   


