#--------------------------------------------------------------------------------------------------
#
#   Description :   Sample program to generate random trajectories and to analyse them using PCA
#                   Prototype for the radial coordinates
#
#   Usage : python pcaMixingRadial
#
#
#   Author : Bruno Blais
#
#
#
#--------------------------------------------------------------------------------------------------

# Imports
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
plot = False
write = False


# User imput parameters
# Available styles : random, rotation
vStyle="randomRotation" 
vR=0.0
vTheta=0.010

# Calculation of reduced deviation
def reDev(x):
    y = 1./numpy.std(x,ddof=1) * (x-numpy.mean(x))
    return y

# Write LAMMPS format output file
def writeFile(i,x,y,z):
    if (i<10):
        outname=sys.argv[1]+"_00"+str(i)+".dump"

    elif(i<100):
        outname=sys.argv[1]+"_0"+str(i)+".dump"

    else:
        outname=sys.argv[1]+"_"+str(i)+".dump"
    print "Writing the file : ", outname
    outfile=open(outname,'w')
    outfile.write("ITEM: TIMESTEP\n")
    outfile.write("%i\n" %i);
    outfile.write("ITEM: NUMBER OF ATOMS\n")
    outfile.write("%i\n" %numpy.size(x));
    outfile.write("ITEM: BOX BOUNDS ff ff ff\n-0.15 0.15\n-0.15 0.15\n-5e-06 0.300005\n")
    outfile.write("ITEM: ATOMS id type type x y z vx vy vz fx fy fz radius\n")

    x2=numpy.reshape(x,numpy.size(x))
    y2=numpy.reshape(y,numpy.size(x))
    z2=numpy.reshape(z,numpy.size(x))


    for i in range(0,numpy.size(x)):
        outfile.write("%i 1 1 %f %f %f 1 1 1 1 1 1 1\n" %(i,x2[i],y2[i],z2[i]))



nx, ny = (101, 101)
x = numpy.linspace(0.001, 1, nx)
y = numpy.linspace(0.001, 1, ny)
xv, yv = numpy.meshgrid(x, y)
rv=(xv*xv+yv*yv)**(1./2.)
tv=numpy.arctan2(yv,xv)


# Initialize figure for trajectories
#-------------------------------------
fig=plt.figure("Trajectories")
lFig=plt.figure("lambda")
lAx=lFig.add_subplot(111)
lAx.set_ylabel("Mixing index")
lAx.set_xlabel("Sampling time")
lAx.set_ylim(ymin=0,ymax=1.1)
ax = Axes3D(fig)
#-------------------------------------

rvl=xv
tvl=yv
C=numpy.zeros([2,2])
lamL=[]

for t in range(0,1100):
    
    if (t>100 and t<1000):
        if (vStyle=="rotation"):
            ur = 0
            ut = vTheta
        if (vStyle=="randomRotation"):
            ur = 0
            ut = vTheta + 10*vTheta*(numpy.random.random_sample([ny,nx])-0.5) 
        elif (vStyle=="uniaxial"):
            ur = 0
            ut = 0
        elif (vStyle=="random"):
            print "Not implemented yet"
        else:
            print "Invalid velocity profile"
        rvl = rvl + ur
        tvl = tvl + ut
    zvl = xv/xv #rvl/numpy.max(rvl,1e-6)*t
    if (t%5==0): 
        xvl = rvl * numpy.cos(tvl)
        yvl = rvl * numpy.sin(tvl)
        ax.scatter(xvl[::nx+1],yvl[::nx+1],zvl[::nx+1],'o')

    #Construct correlation matrix
    C[0,0]=numpy.mean(reDev(rvl)*reDev(rv))
    C[1,0]=numpy.mean(reDev(tvl)*reDev(rv))
    C[0,1]=numpy.mean(reDev(rvl)*reDev(tv))
    C[1,1]=numpy.mean(reDev(tvl)*reDev(tv))

    M = C*C.transpose()
    lam,R=numpy.linalg.eig(M)
    if (t==0): lam0=numpy.max(lam)
    lAx.scatter(t,numpy.sqrt(numpy.max(lam)/lam0))
    if (write): writeFile(t,xvl,yvl,zvl)
    lamL.extend([lam])

plt.show()

