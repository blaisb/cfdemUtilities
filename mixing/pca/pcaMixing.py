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
plot = True
vScaleX=0.15
vScaleY=0.15


# Calculation of reduced deviation
def reDev(x):
    y = 1./numpy.std(x) * (x-numpy.mean(x))
    return y


nx, ny = (15, 15)
x = numpy.linspace(0.001, 1, nx)
y = numpy.linspace(0.001, 1, ny)
xv, yv = numpy.meshgrid(x, y)


fig=plt.figure("Trajectories")
lFig=plt.figure("lambda")
lAx=lFig.add_subplot(111)
lAx.set_ylabel("Mixing index")
lAx.set_xlabel("Sampling time")

ax = Axes3D(fig)
xvl=xv
yvl=yv
C=numpy.zeros([2,2])

for t in range(0,500):
    
    # Uniaxial flow ---> (u,v,w) = (0, 0,1)
    xvl = xvl 
    yvl = yvl

    if (t>100 and t<400):
        u = vScaleX * (numpy.random.random_sample([ny,nx])-0.5) 
        v = vScaleY * (numpy.random.random_sample([ny,nx])-0.5)
        xvl = xvl + u
        yvl = yvl + v
    zvl = xvl/xvl*t
    ax.scatter(xvl,yvl,zvl,'o')

    #Construct correlation matrix
    C[0,0]=numpy.mean(reDev(xvl)*reDev(xv) )
    C[1,0]=numpy.mean(reDev(yvl)*reDev(xv))
    C[0,1]=numpy.mean(reDev(yv)*reDev(yvl))
    C[1,1]=numpy.mean(reDev(yvl)*reDev(yv))

    M = C*C.transpose()
    lam,R=numpy.linalg.eig(M)

    lAx.scatter(t,numpy.sqrt(numpy.max(lam)/3.)/numpy.sqrt(1./3.))
 
plt.show()

