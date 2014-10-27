#This program makes the plot for the average velocity of the particles in a the Z direction for 
# a single case and compares it with the analytical solution for a single particle

# Author : Bruno Blais
# Last modified : December 3rd

#Python imports
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys
dt = 5e-6	# time step of the simulation

#=====================
#   Main plot
#=====================

fname=sys.argv[1]

#INPUT
print "R-> %s" %fname
N, u,v,w, unorm, wStd, wMax, wMin = numpy.loadtxt(fname, unpack=True)

t = N * dt
#Single sphere unsteady solution using Euler finite difference scheme
Dt = 1e-3	# time step of Euler method
rhof = 1000.	# fluid density
rhos = 1100.	# solid density
g = -10.	# gravity
dp = 0.0005	# particle diameter
mu = 0.001	# viscosity of the fluid	
m = 4*numpy.pi/3 * (dp/2)**3 * (rhos)
V= 4*numpy.pi/3 * (dp/2)**3 

niter=int(max(t)/Dt)
vt=numpy.zeros([niter])
T=numpy.zeros([niter])
for i in range(0,niter-1,1):
    Rep = dp * abs(vt[i])*rhof/mu+10**-6
    Cd = (0.63 + 4.8/math.sqrt(Rep+10**-5))**2
    Fd = - 0.125 * Cd *math.pi* rhof * dp**2 * abs(vt[i]) * vt[i]
    T[i+1]=T[i]+Dt
    vt[i+1] = vt[i] + Dt/m * (V*(rhos-rhof)*g+Fd )

plt.figure(fname)
plt.errorbar(t,w,yerr=wStd,fmt='ro', label="Average velocity")
plt.plot(t,wMax,'go', label="Maximal velocity")
plt.plot(T,vt,'-', label="Stokes analytical solution")
plt.ylabel('Average settling velocity [m/s]')
plt.xlabel('time [s]')
plt.title('Average velocity of the particles')
plt.legend(loc=9)
plt.show()

