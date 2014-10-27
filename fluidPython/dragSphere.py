# Last Modified: Tue 01 Apr 2014 11:32:25 AM EDT

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
uf=1
mu = 1
rhof = 1000 #fluid density
rhop = 1000 #particle density
dp = 0.001
tf = 0.0002 #final time of the test / stop the ODE
dt= 5.e-6 #timestep
#------------------------------------------

#Initial velocity of the particle
up=0
n=tf/dt

#Caclulate velocity evolution of particle
t = numpy.arange(0,tf+dt,dt)

#Mass of particle
m = 4 * numpy.pi / 3 * dp**3 / 8 * rhop
u=numpy.zeros([len(t)])

#Begin ODE scheme
for i in range(0,len(t)-1):
    ur = uf-u[i]
    Rep = numpy.abs(rhof * ur * dp/mu)
    Cd = 24 / Rep
    Fd = 0.5 * rhof * numpy.pi * dp**2 * numpy.abs(ur)*ur * Cd
    u[i+1] = u[i] + dt * Fd/m

# Numerical stability critera for comparison with measured stability
print "Stability criteria is : ", rhop * dp**2 / mu /72.

#Plot evolution of velocity in time
plt.figure()
plt.plot(t,u)
plt.show()
