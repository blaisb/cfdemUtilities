# Program for solving the relaxation of a simple sphere under rotation
#
# Author : Bruno Blais

#Python imports
#------------------------------------------------
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#------------------------------------------------

# User defined parameters
#------------------------------------------------
mu=0.05 #Pa.s
omega0=1000
rhoS=2500
rhoF=1000
R=0.0015

#------------------------------------------------

# solve the system dy/dt = f(y, t)
def f(y, t):
    # the model equations 
    df=-15 * mu * y / rhoS / R**2.
    return df
 
 # initial conditions
y0=[omega0]       # initial condition vector
t=np.linspace(0, 0.050, 10000)   # time grid

# solve the DEs
soln = odeint(f, y0, t)
y = soln

torque = -15 * mu / rhoS / R**2 * y**2
Rew= y * R * R *2 / mu * rhoF

# plot results
plt.figure()
plt.plot(t, y, label='Angular velocity')
#plt.plot(t, torque, label='Torque')
plt.xlabel('Time [s]')
plt.ylabel('Angular Velocity')
plt.legend(loc=0)
plt.show()
