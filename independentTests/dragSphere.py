# This program is a simple ODE solver for the case of the drag around a single sphere
# This can be used to predict the stability of the CFDEM coupling time and to play around with the concepts
# Time integration is Euler scheme and Euler form for the drag is assumed

# TODO
# Verlet integration should be added to see if this changes or not something

# Author : Bruno Blais

# Python imports
import math
import numpy
import matplotlib.pyplot as plt

# Simulation parameters to input manually
#-----------------------------------------
uf=1e-5
mu = 1e-5
rhof = 1 #fluid density
rhop = 2400 #particle density
dp = 0.01
tf = 15.0000 #final time of the test / stop the ODE
ratio=1.3
drag="Rong" # or constant
g = 9.81
#------------------------------------------

#Initial velocity of the particle
up=0
dt =ratio * rhop * dp**2 / mu /18.
dt= ratio * 1./(3./4. * rhof/rhop * 1./dp * abs(uf)*0.44)
dt=0.0001
n=tf/dt

#Caclulate velocity evolution of particle
t = numpy.arange(0,tf+dt,dt)

#Mass of particle
m = 4 * numpy.pi / 3 * dp**3 / 8 * rhop
u=numpy.zeros([len(t)]) + up
x=numpy.zeros([len(t)]) 
ReMax=0

#Begin ODE scheme
for i in range(0,len(t)-1):
    ur = uf-u[i]
    Rep = numpy.abs(rhof * ur * dp/mu)
    ReMax=max(Rep,ReMax)
    if (drag=="Stokes"):
        Cd = 24 / Rep
    elif (drag=="Rong"):
        Cd = (0.63 + 2.4/(Rep)**(1./2.))**2
    elif (drag=="Newton"):
        Cd=0.44
    Fd = 0.125 * rhof * numpy.pi * dp**2 * numpy.abs(ur)*ur * Cd
    u[i+1] = u[i] + dt * Fd/m - dt * g


# Numerical stability critera for comparison with measured stability
print "Stability criteria is : ", rhop * dp**2 / mu /18.
print "Stability criteria ratio is: ", dt/ (rhop * dp**2 / mu /18.)
print "Maximal Reynolds reached is: ", ReMax

#Plot evolution of velocity in time
plt.figure()
plt.plot(t,u)
plt.show()

#Plot evolution of velocity in space
plt.figure()
plt.plot(x,u)
plt.show()


