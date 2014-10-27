# Last Modified: Tue 01 Apr 2014 11:39:06 AM EDT
# This program generates a particle file that can be read by LIGGGHTS in order to 
# initialize particle in a given geometrical configuration
# One can change the configuration by defining a new geometrical function in a typical pythonic fashion :)!

# Author : Bruno Blais

#Python imports
#----------------
import os
import sys
import numpy 
#----------------

#**********************
# USER PARAMETERS
#**********************
dpart = 0.0001
rhopart = 1000

#case='Stokes'
case='Circle'

# List of possible cases
    # fullSquare ---> Generates a square full of particles 
    # Circle ---> Generates a circle-contour of particles 

#===============================
#  GEOMETRICAL FUNCTIONS       
#===============================

def regularSquare(x0,y0,lx,ly,pz,nx,ny):
    nx = nx-1 #reduce number by one so that it does not lie on the boundaries
    ny = ny-1 #same as above
    dx = lx/(nx-1)
    dy = ly/(ny-1)
    
    x=numpy.zeros([nx*ny])
    y=numpy.zeros([nx*ny])
    z=numpy.ones([nx*ny]) * pz

    for i in range(0,nx):
	for j in range(0,ny):
	    x[(ny)*i+j] = i * dx + x0 + dx/2
	    y[(ny)*i+j] = j * dy + y0 + dy/2

    return x,y,z, nx*ny

def regularCircle(xc,yc,pz,r,n):

    x=numpy.zeros([n])
    y=numpy.zeros([n])
    z=numpy.ones([n]) * pz

    theta=0.
    dtheta=2. * numpy.pi / n
    for i in range(0,n):
	x[i] = xc + r * numpy.cos(theta)
	y[i] = yc + r * numpy.sin(theta)
	theta += dtheta

    return x,y,z,n



#===============================
# OUTPUT FILES
#===============================

def outputFile(x,y,z,rho,dp,typ,ntyp,x0,y0,lx,ly):
    outname=sys.argv[1]
    print "Writing the file : ", outname
    outfile=open(outname,'w')
    
    n = len(x)

    outfile.write("LAMMPS 3d particle file\n")
    outfile.write("\n")
    outfile.write("            %i  atoms\n" %n)
    outfile.write("            0  bonds\n")
    outfile.write("            0  angles\n")
    outfile.write("            0  dihedrals\n")
    outfile.write("            0  impropers\n")

    outfile.write("\n")

    outfile.write("            %i  atom types\n" %ntyp)
    outfile.write("            0  bond types\n")
    outfile.write("            0  angle types\n")
    outfile.write("            0  dihedral types\n")
    outfile.write("            0  improper types\n")

    outfile.write("\n")

    outfile.write("%5.5e %5.5e   xlo xhi\n" %(x0,x0+lx))
    outfile.write("%5.5e %5.5e   ylo yhi\n" %(y0,y0+ly))
    outfile.write("0. %5.5e   zlo zhi\n" %(numpy.max(z)*2.))

    outfile.write("\n")

    outfile.write("Atoms\n")
    for i in range(0,n):
	# ID Type Diameter density x y z
	outfile.write("\n%i %i %5.5e %5.5e %5.5e %5.5e %5.5e" %(i+1,typ[i],dp[i],rho[i],x[i],y[i],z[i]))

    outfile.close()
    return 

#======================
#   MAIN
#======================   

#Parametes for the Stokes case
if case=='fullSquare' :
    x0 = -numpy.pi
    y0 = -numpy.pi
    lx = 2*numpy.pi
    ly = 2*numpy.pi
    [x,y,z,n] = regularSquare(x0,y0,lx,ly,0.5,101,101)

#Parameters for the Circle case
if case=='Circle' : 
    xc = 0.01
    yc = 0.01
    r  = 0.01
    x0=-0.03
    y0=-0.03
    lx = 0.06
    ly = 0.06
    [x,y,z,n] = regularCircle(xc,yc,0.05,r,201)

rho = numpy.ones([n]) * rhopart
dp = numpy.ones([n]) * dpart
ntyp = 1
typ= numpy.ones([n])

outputFile(x,y,z,rho,dp,typ,ntyp,x0,y0,lx,ly)





