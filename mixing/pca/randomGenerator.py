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
write = True


# User imput parameters
# Available styles : random, rotation
vStyle="rotation" 

vR=0.0
vTheta=0.002



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
        outfile.write("%i 1 1 %f %f %f 1 1 1 1 1 1 1\n" %(i+1,x2[i],y2[i],z2[i]))



rv=[]
tv=[]
zv=[]
t=2
npart=155600

for t in range (2,10):
    rv=[]
    tv=[]
    zv=[]
    for i in range(1,npart+1):
        rv.append(0.365*numpy.random.random_sample(1) )
        tv.append(2*numpy.pi*numpy.random.random_sample(1))
        zv.append(0.365*numpy.random.random_sample(1) )

    xv = rv * numpy.cos(tv)
    yv = rv * numpy.sin(tv)
    writeFile(t,xv,yv,zv)


