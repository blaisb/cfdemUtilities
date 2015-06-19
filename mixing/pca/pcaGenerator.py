#--------------------------------------------------------------------------------------------------
#
#   Description :   Sample program to generate random trajectories and to analyse them using PCA
#
#   Usage : python pcaMixingRadial
#
#
#   Author : Bruno Blais
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
writeFreq=20
analysis = False

#*********************************************
# User imput parameters
# Available styles : gauss, rotation, taylor
#*********************************************
vStyle="lamb"
vR=0.0
vTheta=2*3.14159* 0.005
timeEnd=320
timeStart=100

if (vStyle=="rotation" or vStyle=="gauss"):
    vTheta=2*3.14159* 0.005
elif (vStyle=="taylor"):
    vTheta=2*3.14159* 0.05
elif (vStyle=="lamb"):
    vTheta=2*3.14159* 0.20
    R1=0.50
    


# Calculation of reduced deviation
def reDev(x):
    y = 1./numpy.std(x,ddof=1) * (x-numpy.mean(x))
    return y

# Write LAMMPS format output file
def writeFile(i,x,y,z,ptype,npart):
    outname=sys.argv[1]+"_00"+str(i).zfill(7)+".dump"
    print "Writing the file : ", outname
    outfile=open(outname,'w')
    outfile.write("ITEM: TIMESTEP\n")
    outfile.write("%i\n" %i);
    outfile.write("ITEM: NUMBER OF ATOMS\n")
    outfile.write("%i\n" %npart);
    outfile.write("ITEM: BOX BOUNDS ff ff ff\n-0.15 0.15\n-0.15 0.15\n-5e-06 0.300005\n")
    outfile.write("ITEM: ATOMS id type type x y z vx vy vz fx fy fz radius\n")

    x2=numpy.reshape(x,numpy.size(x))
    y2=numpy.reshape(y,numpy.size(x))
    z2=numpy.reshape(z,numpy.size(x))
    ptype2=numpy.reshape(ptype,numpy.size(x))

    for i in range(0,numpy.size(x)):
        if (x2[i]**2+y2[i]**2<=1):
            outfile.write("%i 1 %i %f %f %f 1 1 1 1 1 1 1\n" %(i,ptype2[i],x2[i],y2[i],z2[i]))



nx, ny = (20, 20)
x = numpy.linspace(-1, 1, nx)
y = numpy.linspace(-1, 1, ny)
xv=numpy.zeros([nx,ny])
yv=numpy.zeros([nx,ny])
ptype=numpy.ones([nx,ny])
numberWithinCircle=0

#Clean array to generate circle
for i,xx in enumerate(x):
    for j,yy in enumerate(y):
        if ((xx*xx+yy*yy)<=1):
            numberWithinCircle+=1
        xv[i,j]=xx
        yv[i,j]=yy
        if (((xx*xx+yy*yy)<=R1) and xx>0):
            ptype[i,j]=1
        if (((xx*xx+yy*yy)<=R1) and xx<0):
            ptype[i,j]=2
        if (((xx*xx+yy*yy)>=R1) and xx>0):
            ptype[i,j]=3
        if (((xx*xx+yy*yy)>=R1) and xx<0):
            ptype[i,j]=4
        if (xx==0):
            ptype[i,j]=1


rv=(xv*xv+yv*yv)**(1./2.)+1e-20
tv=numpy.arctan2(yv,xv)
#r = numpy.linspace(0.01,1,nx)
#tv = numpy.linspace(0.,2*3.14159,ny)

# Initialize figure for trajectories
#-------------------------------------
rvl=rv
tvl=tv
C=numpy.zeros([2,2])
lamL=[]
tt=[]
lamt=[]
laml1=[]
laml2=[]
laml3=[]

for t in range(0,timeEnd):
    
    if (t>timeStart and t<timeEnd-timeStart):
        if (vStyle=="gauss"):
            ur = 0
            ut = vTheta + 10*vTheta*(numpy.random.random_sample([ny,nx])-0.5) 
        else:
            ur = 0
            ut = vTheta 
        rvl = rvl + ur
        if (vStyle=="taylor"):
            tvl = tvl + ut/rvl*0.1
        elif (vStyle=="lamb"):
            tvl = tvl + ut / (2.*numpy.pi*rvl) * (1- numpy.exp(-rvl**2))
        else:
            tvl = tvl + ut

    zvl = numpy.random.random_sample([ny,nx])
    xvl = rvl * numpy.cos(tvl)
    yvl = rvl * numpy.sin(tvl)
    if (t%5==0 and plot): 
        ax.scatter(xvl[::nx+1],yvl[::nx+1],zvl[::nx+1],'o')

    if (analysis):
        #Construct correlation matrix
        C[0,0]=numpy.mean(reDev(rvl)*reDev(rv))
        C[1,0]=numpy.mean(reDev(tvl)*reDev(rv))
        C[0,1]=numpy.mean(reDev(rvl)*reDev(tv))
        C[1,1]=numpy.mean(reDev(tvl)*reDev(tv))

        M = C*C.transpose()
        lam,R=numpy.linalg.eig(M)
        if (t==0): 
            lamInit=lam
            RInit=R
            lam0=numpy.max(lam)
        lamt.append([numpy.max(lam)/lam0])
        tt.append([t])
        #lAx.scatter(t,numpy.sqrt(numpy.max(lam)/lam0))
        lamL.extend([lam])
        laml1.extend([lam[0]])
        laml2.append([lam[1]])
   
    if (write and t%writeFreq ==0 ): 
        writeFile(t,xvl,yvl,zvl,ptype,numberWithinCircle)

plt.plot(tt,laml1,tt,laml2)
plt.show()

