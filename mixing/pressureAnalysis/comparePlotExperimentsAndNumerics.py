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
#                   This version of the script is the most generic and allows for
#                   repeated pressure experiments
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
confFactor=2.7

ptSims=[-5]
ptExp=[-5]
datN={}
datP={}
datA={}
datB={}
xSusp={}
argList=[]
avgList=[]
confFactor=3.182
plotExp=False
plotAvg=True

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

colors=['red','blue','green','pink']


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
        #if "experimentalData" in arg:
        #    N,p,wStd=numpy.loadtxt(arg,unpack=True)
        
        if "experimental" in arg:
            print "Experimental data exception"
            data=numpy.loadtxt(arg,skiprows=1)
            nExp=numpy.size(data,1)/2
            for j in range(0,nExp,1):
                Ns=data[:,j]
                ps=data[:,j+nExp]
                Nss=Ns*Ns
                #Regression for experimental data
                a,b = numpy.polyfit(Nss[ptExp[0]:],ps[ptExp[0]:],1)
                print a, b

                #Plot results
                plt.plot(Ns,a*Ns*Ns+b,'--',linewidth=2.0,color=colors[j])
                plt.plot(Ns,ps,'-o',linewidth=2.5,ms=9,mfc='none',mew=2,color=colors[j],label="Experimental Data")
               
                k=str(arg+str(j))
                datN[k]=Ns
                datP[k]=ps
                datA[k]=a
                datB[k]=b
                argList.append(k)
                avgList.append(k)
                print k
                nPtExp=len(Ns)

        else:
            #Regression for numerical data
            N,p=numpy.loadtxt(arg,unpack=True)
            sortIndex=numpy.argsort(N)
            Ns=N[sortIndex]
            ps=p[sortIndex]
            Nss=Ns*Ns
            
            a,b = numpy.polyfit(Nss[ptSims[0]:],ps[ptSims[0]:],1)
            print a, b
            Nt=numpy.insert(Ns,0,0.)

            # Plot results
            plt.plot(Nt,a*Nt*Nt+b,'k--',linewidth=2.0)
            plt.plot(Ns,ps,'k-^', linewidth=2.5,ms=10,mfc='none',mew=2,label="Simulations")
        
            # Keep data for suspended fraction analysis
            datN[arg]=Ns
            datP[arg]=ps
            datA[arg]=a
            datB[arg]=b
            argList.append(arg)

plt.ylabel('Pressure at the bottom of the tank [Pa]')
plt.xlabel('Speed N [RPM]')
plt.legend(loc=4)
if (pdf): plt.savefig("./pressure_vs_N.pdf")
plt.show()


fig = plt.figure()
ax = fig.add_subplot(111) 
for i,arg in enumerate(argList):
    if (i>=0):
        rawfraction=[]
        fraction=[]
        rawfraction=datP[arg]- (datA[arg]*datN[arg]*datN[arg])
        for j in range(0,len(rawfraction)):
            fraction.append(max(rawfraction[j],rawfraction[0]))
        delta=max(rawfraction)-rawfraction[0]
        for k,val in enumerate(fraction):
            fraction[k] = (val-rawfraction[0])/delta
       
        if "experimental" in arg:
            lab=arg
            if(plotExp):
                ax.plot(datN[arg],fraction,'--o',label=lab,linewidth=2.0,ms=11,mfc='none',mew=2)
        else:
            lab="Simulations"
            ax.plot(datN[arg],fraction,'k-^',label=lab,linewidth=2.0,ms=11,mfc='none',mew=2)
        
        xSusp[arg]=fraction


if (plotAvg):
    xToAvg=numpy.zeros([nPtExp,nExp])
    NToAvg=numpy.zeros([nPtExp,nExp])
    for i,arg in enumerate(avgList):
        xToAvg[:,i]=xSusp[arg]
        NToAvg[:,i]=datN[arg]
    xAvg=numpy.average(xToAvg,axis=1)
    NAvg=numpy.average(NToAvg,axis=1)
    xErr=numpy.std(xToAvg,axis=1)
    NErr=numpy.std(NToAvg,axis=1)
    lab="Averaged experiments"
    (_, caps, _)=ax.errorbar(NAvg,xAvg,xerr=confFactor*NErr,yerr=confFactor*xErr,fmt='o-',label=lab,linewidth=2.0,ms=11,mfc='none',mew=2)

plt.ylabel('Fraction of suspended solid')
plt.xlabel('Speed N [RPM]')
plt.legend(loc=4)
plt.ylim([-0.05,1.05])
if (pdf): plt.savefig("./suspended_vs_N.pdf")
plt.show()



