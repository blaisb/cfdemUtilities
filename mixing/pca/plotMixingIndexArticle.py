####################################################################################
#
#   File    : plotPcaIndexArticle2D.py
#
#   Run Instructions    : python plotPcaMixingArticle2D.py PCAFILE
#
#   Author : Bruno Blais
# 
#   Description :   This script plots the results from a PCA analysis for the 2D 
#                   demonstration in the article
#
#
####################################################################################



#Python imports
#----------------
import os
import sys
import numpy
import time
import matplotlib.pyplot as plt
#----------------



#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
dt=1
nMixing=2
pdf=True
annotate=True

#********************************
#   Anotation options
#********************************
lastAnnotationShift=-0.025

#********************************
#   Figures options
#********************************

plt.rcParams['figure.figsize'] = 10, 7
params = {'backend': 'ps',
             'font.size' : 18,
             'axes.labelsize': 20,
             'text.fontsize': 20,
             'legend.fontsize': 18,
             'xtick.labelsize': 18,
             'ytick.labelsize': 18,
             'text.usetex': True,
             }

annotateFont=20
plt.rcParams.update(params)

#=====================
#   MAIN
#=====================

fname=sys.argv[1]

# Read input data from file fname and distribute it to significantly named variables
print "R-> %s" %fname
data= numpy.loadtxt(fname, unpack=False, skiprows=1)
it=data[:,0]
lam = data[:,1:4] # eigenvalues are sorted by default
v=data[:,4:13]

listAnnotate=[1*len(it)/5., 3.*len(it)/5, len(it)-0.05*len(it)]

#Normalize first two elements of v vector
for i in range(0,len(it)):
    for j in range(0,4,3):
        norme = numpy.sqrt(v[i,0+j]**2 + v[i,1+j]**2 )
        for k in range(0,2) : v[i,k+j]=v[i,k+j]/norme
    

t = (it-it[0]) * dt
fig, axes = plt.subplots(nrows=nMixing, ncols=1)
for i in range(0,nMixing,1):
    plt.subplot(nMixing,1,i+1)

    plt.plot(t,numpy.sqrt(lam[:,i]),'-k',linewidth=2.0)
    plt.ylabel('Mixing index ' + str(i))
    plt.ylim([-0.1,1.5])
    plt.xlim([-10, 12000])
    y=numpy.sqrt(lam[:,i])
    if annotate:
        for j in listAnnotate:
            plt.annotate( "[%3.2f, %3.2f ]" %(v[j,0+i], (-1)**i * v[j,1-i]), 
                    xy=(t[j], y[j]), xytext=(t[j],y[j]+0.3),
                    arrowprops=dict(facecolor='black', shrink=0.05),
                )
    plt.grid(b=True, which='major', color='grey', linestyle='--',linewidth=0.25) 

    plt.annotate( "%3.4f" %(y[-1]), xy=(numpy.max(t), numpy.min(y)), xytext=(numpy.max(t)-lastAnnotationShift*max(t), numpy.min(y)+0.1))

    if (i==1): plt.xlabel('time [s]')
if (pdf and len(sys.argv) >2): plt.savefig(sys.argv[2]+".pdf")
plt.show()

