###############################################################################
#
#   File    : analysePressure.py
#
#   Run Instructions    : python plotPressure.py directory/with/the/files
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
import pylab 

#-------------------------------


#=====================
# User parameters
#=====================
ptSims=[-7]
ptExp=[-10,-3]
datN={}
datP={}
data={}
datb={}
confFactor=2.35

# Figures
plt.rcParams['figure.figsize'] = 10, 7
params = {'backend': 'ps',
             'axes.labelsize': 20,
             'text.fontsize': 16,
             'legend.fontsize': 18,
             'xtick.labelsize': 16,
             'ytick.labelsize': 16,
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
            #Regression with three last points
            a,b = numpy.polyfit(Nss[ptExp[0]:ptExp[1]],ps[ptExp[0]:ptExp[1]],1)
            print a, b
            plt.plot(Ns,ps,'g-s',label="Experimental Data")
            plt.plot(Ns,a*Ns*Ns+b,'g--',linewidth=2.0)
           
        else:
            #Regression with three last points
            a,b = numpy.polyfit(Nss[ptSims[0]:],ps[ptSims[0]:],1)
            print a, b
            plt.plot(Ns,ps,'b-o',label="Simulations")
            Nt=numpy.insert(Ns,0,0.)

            plt.plot(Nt,a*Nt*Nt+b,'b--',linewidth=2.0)
        datN[arg]=Ns
        datP[arg]=ps
        data[arg]=a
        datb[arg]=b




plt.ylabel('Pressure at the bottom of the tank [Pa]')
plt.xlabel('Speed N[RPM]')
plt.legend(loc=4)
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111) 
for i,arg in enumerate(sys.argv):
    if (i>=1):
        rawfraction=[]
        fraction=[]
        rawfraction=datP[arg]- (data[arg]*datN[arg]*datN[arg]+b)
        for j in range(0,len(rawfraction)):
            fraction.append(max(rawfraction[j],rawfraction[0]))
        delta=max(rawfraction)-rawfraction[0]
        for k,val in enumerate(fraction):
            fraction[k] = (val-rawfraction[0])/delta
        
        if (i==1): 
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
            ax.errorbar(datN[arg],fraction,yerr=[stdmin,stdmax],fmt='g-s',label="Experimental Data",linewidth=1.5)
        else:  ax.plot(datN[arg],fraction,'b--o',label="Simulations",linewidth=2.0)


plt.ylabel('Fraction of suspended solid')
plt.xlabel('Speed N[RPM]')
plt.legend(loc=4)
plt.ylim([-0.05,1.05])
plt.show()

