###############################################################################
#
#   File    : plotPressure.py
#
#   Usage    : python plotPressure.py experimentalData numericalData
#
#   Author : Bruno Blais
# 
#   Description :   This script plot the pressure from experimental and
#                   numerical data and carries out the pressure analysis
#                   to obtain the fraction of suspended solid
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
import pylab 

#-------------------------------


#=====================
# User parameters
#=====================
pdf=True

ptSims=[-6]
ptExp=[-10,-3]
datN={}
datP={}
data={}
datb={}
confFactor=3.182

# Figures
plt.rcParams['figure.figsize'] = 10, 7
params = {'backend': 'ps',
             'axes.labelsize': 20,
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



# Suspended solid fraction analysis
print "*********************************"
print "Suspended solid fraction analysis"
print "*********************************"
for i,arg in enumerate(sys.argv):
    if (i>=1):
        if (arg=="experimentalData"):
            N,p,wStd=numpy.loadtxt(arg,unpack=True)
        else:
            N,p=numpy.loadtxt(arg,unpack=True)
        sortIndex=numpy.argsort(N)
        Ns=N[sortIndex]
        ps=p[sortIndex]
        Nss=Ns*Ns
        if(arg=="experimentalData"):
            print "Experimental data exception"
            #Regression for experimental data
            a,b = numpy.polyfit(Nss[ptExp[0]:ptExp[1]],ps[ptExp[0]:ptExp[1]],1)
            print a, b

            #Plot results
            plt.plot(Ns,a*Ns*Ns+b,'k--',linewidth=2.0)
            plt.plot(Ns,ps,'k-o',linewidth=2.5,ms=9,mfc='none',mew=2,label="Experimental data")
           
        else:
            #Regression for numerical data
            a,b = numpy.polyfit(Nss[ptSims[0]:],ps[ptSims[0]:],1)
            print a, b
            Nt=numpy.insert(Ns,0,0.)

            # Plot results
            plt.plot(Nt,a*Nt*Nt+b,'k--',linewidth=2.0)
            plt.plot(Ns,ps,'k-^', linewidth=2.5,ms=10,mfc='none',mew=2,label="Simulation results")
        
        # Keep data for suspended fraction analysis
        datN[arg]=Ns
        datP[arg]=ps
        data[arg]=a
        datb[arg]=b

plt.ylabel('Pressure at the bottom of the tank [Pa]')
plt.xlabel('Speed N [RPM]')
plt.legend(loc=4)
if (pdf): plt.savefig("./pressure_vs_N.pdf")
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111) 
for i,arg in enumerate(sys.argv):
    if (i>=1):
        rawfraction=[]
        fraction=[]
        rawfraction=datP[arg]- (data[arg]*datN[arg]*datN[arg])
        for j in range(0,len(rawfraction)):
            fraction.append(max(rawfraction[j],rawfraction[0]))
        delta=max(rawfraction)-rawfraction[0]
        for k,val in enumerate(fraction):
            fraction[k] = (val-rawfraction[0])/delta
       
        if (i!=1):
          ax.plot(datN[arg],fraction,'k--^',label="Simulation results",linewidth=2.0,ms=11,mfc='none',mew=2)
        elif (i==1): 
            error=confFactor*wStd*fraction
            stdmin=[]
            stdmax=[]
            for m,n in enumerate(fraction):
                stdmin.append(min(error[m],n))
                stdmax.append(min(error[m],1.-n))
            #for m,n in enumerate(fraction):
                #if ((n - error[m])<0.) : stdmin[m]=n
                #if ((n + error[m])>1.) : 
                    #stdmax[m]=1.-n
                    #stdmin[m]=error[m]
            
            (_, caps, _) = ax.errorbar(datN[arg],fraction,yerr=[stdmin,stdmax],fmt='k-o',label="Experimental data",linewidth=1.0,ms=8,capsize=6,mfc='none',mew=2)

            for cap in caps:
                cap.set_markeredgewidth(2)

plt.ylabel('Fraction of suspended solids')
plt.xlabel('Speed N [RPM]')
plt.legend(loc=4)
plt.ylim([-0.05,1.05])
if (pdf): plt.savefig("./suspended_vs_N.pdf")
plt.show()

