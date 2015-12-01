###############################################################################
#
#   File    : analysePressure.py
#
#   Run Instructions    : python analysePressure.py directory/with/the/files
#
#   Author : Bruno Blais
# 
#   Description :   This script takes all the files in a folder and output
#                   a two column file that is N vs P
#
#
###############################################################################

#Python imports
#-------------------------------
import os
import math
import numpy
import matplotlib.pyplot as plt
import sys
#-------------------------------

#Figure size and parameters
#-------------------------
plt.rcParams['figure.figsize'] = 10, 7

params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 16,
             'legend.fontsize': 20,
             'xtick.labelsize': 20,
             'ytick.labelsize': 20,
             'text.usetex': True,
             }
   
plt.rcParams.update(params)

pdf=True

#=====================
#   Main plot
#=====================

if (len(sys.argv)<2) :
    print "You need to enter a file argument"

#===================
# Ergun Analysis from Christoph
#===================
rhoG=1000
dp = 0.001			# particle diameter
phip = 1			# sphericity
epsilon = 0.451335              # void fraction
L = 0.0151			# length of bed
nuG = 1.*10**-4			# kinemat Visk in m2/s
muG = nuG*rhoG			# dynam visc in Pa s

#==================================
# min fluidization velocity in m/s
#==================================
rhoP = 2000                     # particle density in kg/m3
g = 9.81                        # gravity m/s2

Umf = dp**2*(rhoP-rhoG)*g/(150*muG)*(epsilon**3*phip**2)/(1-epsilon);
ReMF = Umf*dp*rhoG/muG;
if (ReMF>=1000):
    Umf = sqrt(dp*(rhoP-rhoG)*g/(1.75*rhoG)*epsilon**3*phip);
    ReMF = Umf*dp*rhoG/muG;




#=================================
#       Output files
#=================================

print "Opening ", sys.argv[1]
pMat1 = numpy.loadtxt(sys.argv[1], unpack=True,comments="#")
t1=pMat1[0,::9]
dP1=(pMat1[1,::9]-pMat1[-1,::9]) * rhoG
print "Opening ", sys.argv[2]
pMat2 = numpy.loadtxt(sys.argv[2], unpack=True,comments="#")
t2=pMat2[0,::9]
dP2=(pMat2[1,::9]-pMat2[-1,::9]) * rhoG



plt.plot(t1,0.99*dP1,'g',label="Implicit momentum exchange",alpha=0.3,linewidth=2)
plt.plot(t2,0.99*dP2,'m',label="Explicit momentum exchange",alpha=0.8,linewidth=2)



dpUmf= numpy.ones(len(t1)) * L * (
                150*((1-epsilon)**2/epsilon**3)*((muG*Umf)/(phip*dp)**2) 
              +1.75*((1-epsilon)/epsilon**3)*((rhoG*Umf**2)/(phip*dp))
        );

plt.plot(t1,dpUmf,'k',label="Ergun equation",linewidth=3)
plt.ylim([-10,150])


plt.ylabel('Pressure drop [Pa]')
plt.xlabel('Time [s]')
plt.legend(loc=4)

if (pdf): plt.savefig("./pressureRuns.pdf")


plt.show()

