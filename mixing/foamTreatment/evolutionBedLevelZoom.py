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
from matplotlib import ticker #Manually change number of tick
import matplotlib.patches as patches
#----------------

#================================
#   USER DEFINED VARIABLES  
#================================
pdf=False
tol=1e-4
paperMode=True
impeller=True
impellerType="pbtTs4"
contour=False
nContour=100
colorList=["c","m","g","r","b", "k","c","m","g","r","b","k"]
aval=0.5
nPoint=4
manualExtent=True

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
    folder = sys.argv[1:]
except:
    print "Insufficient number of arguments, need a folder argument"

# Acquire list of time step
speedFolder=folder

# Sort so that speed will already be sorted
speedFolder.sort() 
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)


for j,i in enumerate(speedFolder):
    subFolder=i +"/CFD/resultsCFD/postProcessing/probes"
    time=os.listdir(subFolder)

    fname = subFolder+"/"+max(time)+"/"+"voidfraction"
    print "Postprocessing file : ", fname
    
    rl,zl,acc,dev=scalarAverage(fname,impeller,impellerType)
    extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl))
   
    if (j==0 ):#or j==4): 
        accAll=acc
        xmin = numpy.min(rl)
        xmax = numpy.max(rl)
        ymin = numpy.min(zl)
        ymax = numpy.max(zl)
        xy = (xmin,ymin)
        width = xmax - xmin
        height = ymax - ymin

        # create the patch and place it in the back of countourf (zorder!)
        p = patches.Rectangle(xy, width, height, fill=True,color="k",alpha=0.4, zorder=-10)
        ax.add_patch(p)

        levels=(0.,1.1)
        CS=plt.contourf(accAll, levels, hold='on',alpha=1,  colors="w",origin='lower', extent=extent)

    elif(j<nPoint): accAll=numpy.maximum(acc,accAll)

    maxdiff=numpy.nanmax(acc)
    mindiff=numpy.nanmin(acc)
    levels = (0,0.5) # numpy.arange(mindiff, maxdiff+tol, (maxdiff-mindiff)/nContour)
    if (j<nPoint):
        plt.subplot(1,1,1)
        # get data you will need to create a "background patch" to your plot
        CS=plt.contourf(acc, levels, hold='on',alpha=0.5,  colors=colorList[j],origin='lower', extent=extent)
        CS=plt.contour(acc, levels, hold='on',alpha=1,  colors="k", origin='lower', extent=extent)

    else:
        a = plt.axes([0.3, 0.3, .50, .3], axisbg='w')
        plt.setp(a, xlim=(0,.2), xticks=[], yticks=[])
        CS=plt.contourf(acc, levels, hold='on',alpha=0.5,  colors=colorList[j-nPoint],origin='lower', extent=extent)
        CS=plt.contour(acc, levels, hold='on',alpha=1,  colors="k", origin='lower', extent=extent)

    #plt.clabel(CS, inline=1, fontsize=14,colors="white")



#Get artists and labels for legend and chose which ones to display
handles, labels = ax.get_legend_handles_labels()
display = (0,1,2)

#Create custom artists
a1 = patches.Rectangle((0,0),1,1,color=colorList[0],alpha=aval)
a2 = patches.Rectangle((0,0),1,1,color=colorList[1],alpha=aval)
a3 = patches.Rectangle((0,0),1,1,color=colorList[2],alpha=aval)
a4 = patches.Rectangle((0,0),1,1,color=colorList[3],alpha=aval)
#anyArtist = plt.Line2D((0,1),(0,0), color='k')
ax.legend([handle for i,handle in enumerate(handles) if i in display]+[a1,a2,a3,a4],
          [label for i,label in enumerate(labels) if i in display]+["100RPM","200RPM","300RPM","400RPM"])

plt.show()
if (pdf): plt.savefig("./levelAnalysis.pdf")
plt.show()
   


