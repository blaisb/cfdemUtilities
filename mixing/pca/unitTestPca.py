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
    y = 1./numpy.std(x,ddof=1) * (x-numpy.mean(x))
    return y

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


 


nx, ny = (20, 20)
x = numpy.linspace(0.001, 1, nx)
y = numpy.linspace(0.001, 1, ny)
xv, yv = numpy.meshgrid(x, y)


#fig=plt.figure("Trajectories")
lFig=plt.figure("lambda")
lAx=lFig.add_subplot(111)
lAx.set_ylabel("Mixing index")
lAx.set_xlabel("Sampling time")

#ax = Axes3D(fig)
xvl=xv
yvl=yv
zvl=xv
zv= xv
lamL=[]
C=numpy.zeros([3,3])

for t in range(0,1000):
    
    # Uniaxial flow ---> (u,v,w) = (0, 0,1)
    xvl = xvl 
    yvl = yvl
    zvl = zvl

    if (t>100 and t<800):
        u = vScaleX * (numpy.random.random_sample([ny,nx])-0.5) 
        v = vScaleY * (numpy.random.random_sample([ny,nx])-0.5)
        xvl = xvl + u
        yvl = yvl + v
        zvl = zvl+ xvl/xvl*0.1 * (numpy.random.random_sample([ny,nx])-0.5)


    #ax.scatter(xvl,yvl,zvl,'o')

    #Construct correlation matrix
    C[0,0]=numpy.mean(reDev(xvl)*reDev(xv) )
    C[1,0]=numpy.mean(reDev(yvl)*reDev(xv))
    C[2,0]=numpy.mean(reDev(zvl)*reDev(xv))
    C[0,1]=numpy.mean(reDev(xvl)*reDev(yv))
    C[1,1]=numpy.mean(reDev(yvl)*reDev(yv))
    C[2,1]=numpy.mean(reDev(zvl)*reDev(yv))
    C[0,2]=numpy.mean(reDev(xvl)*reDev(zv))
    C[1,2]=numpy.mean(reDev(yvl)*reDev(zv))
    C[2,2]=numpy.mean(reDev(zvl)*reDev(zv))



    M = numpy.dot(C,C.transpose())
    lam,R=numpy.linalg.eig(M)

    lAx.scatter(t,numpy.sqrt(numpy.max(lam)/3.))
    writeFile(t,xvl,yvl,zvl)
    lamL.extend([lam])

for i in lamL:
    print numpy.sort(i), " \n" 
plt.show()

