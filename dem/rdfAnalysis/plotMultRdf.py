# This plots the RDF of a LIGGGHTS post-processed analysis
# 
# USAGE : python ./file 
#
# Author : Bruno Blais

#Python imports
#----------------
import os
import sys
import numpy
import matplotlib.pyplot as plt
#----------------


#********************************
#   OPTIONS AND USER PARAMETERS
#********************************
pdf=True
dp=3e-3
dpAdim=True
leg=["Initial configuration" , "3 s." , "6 s." , "10 s.", "30 s.", "50 s."]

#Figure size
plt.rcParams['figure.figsize'] = 10, 7

params = {'backend': 'ps',
             'axes.labelsize': 24,
             'text.fontsize': 16,
             'legend.fontsize': 18,
             'xtick.labelsize': 16,
             'ytick.labelsize': 16,
             'text.usetex': True,
             }
   
plt.rcParams.update(params)

#======================
#   MAIN
#======================
tFold= 0

#Read the logs files
if (len(sys.argv)<2):
    print 'Files must be specified when running this python script'
    sys.exit("Crashed because files were not specified")


n,x,rdf,cord = numpy.loadtxt(sys.argv[1], unpack=True,skiprows=4)

# Plot
fig, ax1 = plt.subplots() 
plt.ylabel('Radial distribution function ')
if(dpAdim):
    plt.xlabel('Dimensionless distance $\mathbf{x}/d_{p}$')
else:
    plt.xlabel('Distance $\mathbf{x}$')
    
ax1.set_ylabel('Radial distribution function g(r)')


for i in range(1,len(sys.argv)):
    print sys.argv[i]
    n,x,rdf,cord = numpy.loadtxt(sys.argv[i], unpack=True,skiprows=4)
    if (dpAdim):
        if (i==6):
            ax1.plot(x/dp,rdf,'k',linewidth=2.0,label=leg[i-1])
        else:
            ax1.plot(x/dp,rdf,linewidth=2.0,label=leg[i-1])
    else:
        ax1.plot(x,rdf,linewidth=2.0)

if (pdf): plt.savefig("./rdf.pdf")
plt.legend()
plt.show()

