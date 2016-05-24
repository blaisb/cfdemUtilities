###############################################################################
#
#   File    : plotPressureRun.py
#
#   Run Instructions    : python plotPressureRun file1 file2 file3
#
#   Author : Bruno Blais
# 
#   Description :  Plot ergun pressure runs for as many files as required 
#                   
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

#=====================
#   User parameters
#=====================
presentationMode=False
png=True
pdf=False
skip=0
step=1

#-----------------------------
#Figure size and parameters
#-----------------------------
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

#=====================
#   Main plot
#=====================

if (len(sys.argv)<2) :
    print "You need to enter a file argument"

#===================
# Ergun Analysis from Christoph
#===================
rhoG=10
dp = 0.001			# particle diameter
phip = 1			# sphericity
epsilon = 0.451335              # void fraction
L = 0.0156			# length of bed
nuG = 1.5*10**-4			# kinemat Visk in m2/s
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

for i in range(1,len(sys.argv)):
    print "Opening ", sys.argv[i]
    pMat = numpy.loadtxt(sys.argv[i], unpack=True,comments="#")
    t=pMat[0,:]
    dP=(pMat[1,:]-pMat[-1,:]) * rhoG
    if (presentationMode):
        if i==1 : plt.plot(t[skip::step],dP[skip::step],label="0 RPM",alpha=1.0,linewidth=2)
        if i==2 : plt.plot(t[skip::step],dP[skip::step],label="100 RPM",alpha=0.8,linewidth=2)
        if i==3 : plt.plot(t[skip::step],dP[skip::step],label="500 RPM",alpha=0.35,linewidth=2.5)

    else:
        plt.plot(t[skip::step],dP[skip::step],label=sys.argv[i])



dpUmf= numpy.ones(len(t)) * L * (
                150*((1-epsilon)**2/epsilon**3)*((muG*Umf)/(phip*dp)**2) 
              +1.75*((1-epsilon)/epsilon**3)*((rhoG*Umf**2)/(phip*dp))
        );

plt.plot(t[::9],dpUmf[::9],'k',label="Ergun correlation",linewidth=4,alpha=0.75)
plt.ylim([-60,200])
#plt.xlim([0,0.1])

plt.ylabel('Pressure drop [Pa]')
plt.xlabel('Time [s]')
plt.legend(loc=4)


if (png): plt.savefig("./pressureRuns.png")
if (pdf): plt.savefig("./pressureRuns.pdf")

plt.show()

