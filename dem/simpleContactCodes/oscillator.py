# Program for solving a simple oscillator ode to analyse
# DEM collision model
#
#
#
#
# Author : Bruno Blais

#Python imports
#----------------
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#----------------

eps=2.1
 
# solve the system dy/dt = f(y, t)
def f(y, t):
    # the model equations 
    df=y[1]
    ddf = -eps*y[1] - y[0]
    
    return [df, ddf]
 
 # initial conditions
y0=[0,1]       # initial condition vector
t=np.linspace(0, 25, 10000)   # time grid

# solve the DEs
soln = odeint(f, y0, t)
y = soln[:, 0]
dy = soln[:,1]

  
# plot results
plt.figure()
plt.plot(t, y, label='Displacement')
plt.plot(t, dy, label='Velocity')
plt.xlabel('Time [s]')
plt.ylabel('Displacement / Velocity')
plt.legend(loc=0)
plt.show()
