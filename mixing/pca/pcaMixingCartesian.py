#--------------------------------------------------------------------------------------------------
#
#   Description :   Sample program to generate random trajectories and to analyse them using PCA
#                   This is really just a prototype
#
#   Usage : python pcaMixing
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


# User imput parameters
# Available styles : random, rotation
vStyle="rotationRandom" 
vScaleX=0.01
vScaleY=0.01



# Calculation of reduced deviation
def reDev(x):
    y = 1./numpy.std(x,ddof=1) * (x-numpy.mean(x))
    return y


nx, ny = (101, 101)
x = numpy.linspace(0.001, 1, nx)
y = numpy.linspace(0.001, 1, ny)
xv, yv = numpy.meshgrid(x, y)


fig=plt.figure("Trajectories")
lFig=plt.figure("lambda")
lAx=lFig.add_subplot(111)
lAx.set_ylabel("Mixing index")
lAx.set_xlabel("Sampling time")
lAx.set_ylim(ymin=0,ymax=1.1)

ax = Axes3D(fig)
xvl=xv
yvl=yv
C=numpy.zeros([2,2])

for t in range(0,1100):
    
    # Uniaxial flow ---> (u,v,w) = (0, 0,1)
    xvl = xvl 
    yvl = yvl

    if (t>100 and t<1000):
        if (vStyle=="rotation"):
            u = -vScaleX * yvl
            v =  vScaleX * xvl
        elif (vStyle=="rotationRandom"):
            temp = vScaleX *10* (numpy.random.random_sample([ny,nx])-0.5) 
            u = -vScaleX * yvl - temp * yvl 
            v =  vScaleX * xvl + temp * xvl
        elif (vStyle=="random"):
            u = vScaleX * (numpy.random.random_sample([ny,nx])-0.5) 
            v = vScaleY * (numpy.random.random_sample([ny,nx])-0.5)
        else:
            print "Invalid velocity profile"
        xvl = xvl + u
        yvl = yvl + v
    zvl = xvl/xvl*t
    if (t%5==0): ax.scatter(xvl[::nx+1],yvl[::nx+1],zvl[::nx+1],'o')

    #Construct correlation matrix
    C[0,0]=numpy.mean(reDev(xvl)*reDev(xv))
    C[1,0]=numpy.mean(reDev(yvl)*reDev(xv))
    C[0,1]=numpy.mean(reDev(xvl)*reDev(yv))
    C[1,1]=numpy.mean(reDev(yvl)*reDev(yv))

    M = C*C.transpose()
    lam,R=numpy.linalg.eig(M)
    if (t==0): lam0=numpy.max(lam)
    lAx.scatter(t,numpy.sqrt(numpy.max(lam)/lam0))
 
plt.show()

