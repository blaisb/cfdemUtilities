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

#===============================
#   FIGURE OPTIONS
#===============================
#Figure size
plt.rcParams['figure.figsize'] = 17, 8

params = {'backend': 'ps',
             'axes.labelsize': 24,
             'axes.titlesize': 24,
             'text.fontsize': 20,
             'legend.fontsize': 20,
             'xtick.labelsize': 20,
             'ytick.labelsize': 20,
             'text.usetex': True,
             }
   
plt.rcParams.update(params)


#================================
#   FUNCTION
#================================


def getCoordFromLine(l):
    l_str = l.split(" ")
    a = [x for x in l_str if x != ""]
    y=[]
    for i,val in enumerate(a):
        if (i>=2):
            y.append(float(val))
    return numpy.array(y)

def getScalarFromLine(l):
    l_str = l.split(" ")
    a = [x for x in l_str if x != ""]
    y=[]
    for i,val in enumerate(a):
        if (i>=1):
            y.append(float(val))
    return numpy.array(y)


def getVectorFromLine(l):
    l=l.replace(")"," ")
    l=l.replace("("," ")
    
    l_str = l.split(" ")
    a = [x for x in l_str if x != ""]  

    u=[]
    v=[]
    w=[]

    for i in range(1,len(a)-1,3):
        u.append(float(a[i]))
        v.append(float(a[i+1]))
        w.append(float(a[i+2]))
        

    return numpy.array(u),numpy.array(v),numpy.array(w)

#================================
#   MAIN
#================================

fname=sys.argv[1]
mode=sys.argv[2]

infile = open(fname,'r')


#Get the first three lines to get the x y z positions
l=infile.readline()
x=getCoordFromLine(l)
l=infile.readline()
y=getCoordFromLine(l)
l=infile.readline()
z=getCoordFromLine(l)

#Transform the x y z positions to r t z
r = numpy.sqrt(x*x+y*y)
theta = numpy.arctan2(y,x)

#Remove useless buffer line
l=infile.readline()

#Count number of different radiuses
rr=-1
nr=0
rl=[]
z0=z[0]
for ind,i in enumerate(r) :
    if (abs(z[ind]-z0)>tol):break # Don't want to count nr * nz instead of nr
    if (abs(i-rr)>tol): 
        rr=i
        rl.append(rr)
        nr+=1
rl.append(r[-1])

rr=-1
zl=[]
nz=0
for i in z :
    if (abs(i-rr)>tol): 
        rr=i
        nz+=1
        zl.append(rr)
zl.append(z[-1])


#The variable is a vector bro-dude-migo
if (mode=="velocity"):
    #Acquire the U V and W vector associated with each position
    l=infile.readline()
    u,v,w=getVectorFromLine(l)

    #clean the velocities
    for i in range(1,len(u)):
        if (abs(u[i])>10): u[i]=u[i-1]
        if (abs(v[i])>10): v[i]=v[i-1]
        if (abs(w[i])>10): w[i]=w[i-1]


    ur =   numpy.cos(theta)*u + numpy.sin(theta)*v
    ut = - numpy.sin(theta)*u + numpy.cos(theta)*v


    #Averaging procedure
    acc=numpy.zeros([nz,nr,3])
    j=0
    k=0
    count=0
    pR=r[0]
    pZ=z[0]
    temp=numpy.array([0.,0.,0.])
    for i in range(0,len(z)):
        if (abs(r[i]-pR)>tol):
            count=max(count,1)
            acc[k,j]=temp/count
            j+=1
            count=0
            pR=r[i]
            temp=numpy.array([0.,0.,0.])

        if (abs(z[i]-pZ)>tol):
#            acc[j,k]=temp/count
            pZ=z[i]
            j=0
            k+=1

        temp[0]+=ur[i]
        temp[1]+=ut[i]
        temp[2]+=w[i]
        count+=1
        if (i ==(len(z)-1)): acc[k,j]=temp/count

# Make the graph of the three coordinates:

    # Radial graph
    plt.figure()
    plt.subplots_adjust(left=0.06, bottom=0.06, right=0.95, top=0.94, wspace=0.35)
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
   
if (mode=="scalar"):
    #Acquire the U V and W vector associated with each position
    l=infile.readline()
    s=getScalarFromLine(l)

    #clean the scalar
    for i in range(1,len(s)):
        if (abs(s[i])>1e5): s[i]=s[i-1]

    #Averaging procedure
    acc=numpy.zeros([nz,nr])
    acc2=numpy.zeros([nz,nr])
    j=0
    k=0
    count=0
    pR=r[0]
    pZ=z[0]
    temp=0
    temp2=0
    for i in range(0,len(z)):
        if (abs(r[i]-pR)>tol):
            count=max(count,1)
            acc[k,j]=temp/float(count)
            acc2[k,j]=temp2/float(count)
            j+=1
            count=0
            pR=r[i]
            temp=0.
            temp2=0.

        if (abs(z[i]-pZ)>tol):
#            acc[j,k]=temp/count
            pZ=z[i]
            j=0
            k+=1

        temp+=s[i]
        temp2+=s[i]*s[i]
        count+=1
        if (i ==(len(z)-1)):
            acc[k,j]=temp/count
            acc2[k,j]=temp2/float(count)
            

    var = acc2-acc**2

    dev = numpy.sqrt(var)
    plt.figure(figsize=(12,8))
    plt.subplots_adjust(left=0.02, bottom=0.08, right=0.95, top=0.94, wspace=0.15)
    plt.subplot(1,2,1)
    plt.xlabel("r [m]")
    plt.ylabel("z [m]")
   


    plt.imshow(acc[:,:],extent=(numpy.min(rl),numpy.max(rl),numpy.min(zl),numpy.max(zl)),origin='lower',interpolation="bicubic",vmin=0.4,vmax=1.)
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
    if (pdf): plt.savefig("./voidfraction_prof.pdf")
    plt.show()
   


