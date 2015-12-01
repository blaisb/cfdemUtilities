###############################################################################
#
#   File    : plotPressure.py
#
#   Run Instructions    : python plotPressure.py file
#
#   Author : Bruno Blais
# 
#   Description :   Plots P vs N and compares with ergun
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

#-------------------------------
#
#-------------------------------

#=====================
#   Main plot
#=====================
#Figure size and parameters
#-------------------------
plt.rcParams['figure.figsize'] = 10, 7

params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 16,
             'legend.fontsize': 18,
             'xtick.labelsize': 20,
             'ytick.labelsize': 20,
             'text.usetex': True,
             }
   
plt.rcParams.update(params)

pdf=True

if (len(sys.argv)<2) :
    print "You need to enter a file argument"


for i,arg in enumerate(sys.argv):
    if (i>=1):
        print i, arg
        N,p = numpy.loadtxt(arg, unpack=True)
        sortIndex=numpy.argsort(N)
        NS=N[sortIndex]
        pS=p[sortIndex]
 


#===================
# Ergun Analysis from Christoph
#===================
rhoG=1000
dp = 0.001			# particle diameter
phip = 1			# sphericity
epsilon = 0.451335              # void fraction
U=numpy.linspace(0,max(NS),10000)
deltaU=max(U);
Ua = U / epsilon;		# physical velocity
L = 0.0151 			# length of bed --- was 0.0156
nuG = 1.*10**-4			# kinemat Visk in m2/s
muG = nuG*rhoG			# dynam visc in Pa s

dpErgun= L * (
                150*((1-epsilon)**2/epsilon**3)*((muG*U)/(phip*dp)**2) 
              +1.75*((1-epsilon)/epsilon**3)*((rhoG*U**2)/(phip*dp))
        );


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

dpUmf= L * (
                150*((1-epsilon)**2/epsilon**3)*((muG*Umf)/(phip*dp)**2) 
              +1.75*((1-epsilon)/epsilon**3)*((rhoG*Umf**2)/(phip*dp))
        );

for i in range(0,len(U)):
    if U[i]>Umf : dpErgun[i]=dpUmf

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(U,dpErgun,'k-',alpha=0.8,linewidth=3,label="Ergun equation")
plt.plot(NS,pS,'--sc',linewidth=2.5,markersize=8,alpha=1, label="Explicit momentum exchange")
plt.ylabel('Pressure drop [Pa]')
plt.xlabel('Inlet velocity u [m.s$^{-1}$]')
plt.plot((Umf,Umf ), (0,100), 'k--',linewidth=2.5)
ax.annotate(' $U_{mf}$', xy=(Umf+0.000001, 70), xytext=(Umf+0.00001,60 ),
            arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=26)
plt.legend(loc=4)
if (pdf): plt.savefig("./pressureErgun.pdf")
plt.show()

