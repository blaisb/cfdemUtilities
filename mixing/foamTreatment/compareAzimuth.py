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
pdf=False
contour=False
nContour=30
paperMode=True
impeller=True
impellerType="pbtTs4"

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
    fname2= sys.argv[2]
except:
    print "Insufficient number of arguments, need two files names"

rl,zl,acc,dev=scalarAverage(fname,impeller,impellerType)
rl2,zl2,acc2,dev2=scalarAverage(fname2,impeller,impellerType)

plt.figure(figsize=(6,8))
plt.subplots_adjust(left=0.02, bottom=0.09, right=0.95, top=0.94, wspace=0.15)
plt.subplot(1,1,1)
plt.xlabel("r [m]")
plt.ylabel("z [m]")

extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl))

diff=acc2[:,:]-acc[:,:]

plt.imshow(acc2[:,:]-acc[:,:],extent=extent,origin='lower',interpolation="bicubic")

cbar = plt.colorbar( drawedges=False)
tick_locator = ticker.MaxNLocator(nbins=7)
cbar.locator = tick_locator
cbar.update_ticks()
cbar.ax.tick_params(labelsize=20) 
cbar.solids.set_edgecolor("face")

if (len(sys.argv)>3):
    plt.title("%s" %(sys.argv[3]))
else:
    plt.title("%s" %(sys.argv[1]))


if(contour):
    maxdiff=numpy.nanmax(diff)
    mindiff=numpy.nanmin(diff)
    levels = numpy.arange(mindiff, maxdiff+tol, (maxdiff-mindiff)/10.)
    CS=plt.contourf(acc2[:,:]-acc[:,:], levels, hold='on',
        origin='lower', extent=extent)
    #plt.clabel(CS, inline=1, fontsize=14,colors="white")

plt.show()



