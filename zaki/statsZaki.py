# This program considers the content of a single case and applies statistics to the velocity of the particles before
# outputting them to a text file

# This program should be launched from the root folder of the case within which reside DEM and CFD folders

# Format of output file : uAvg, vAvg, wAvg, uNormAvg, wStd, wMax, wMin

# Author : Bruno Blais
# Last modified : 06-01-2014

#Python imports
import os
import sys
import numpy 


#**********************
#   OPTIONS
#**********************
zCut		= True  # Find particles above a certain z value
calcStat	= True  # Calculate statistics from particles
zCutVal	    = 0.05 # Value of Z above which the particles are considered
outname= "../../"+sys.argv[1]

#====================
#   DUMP READER	
#====================
def readf(fname):
    infile = open(fname,'r')
    if (infile!=0):
	print "R-> %s" %fname
	
	#Read current timestep
	infile.readline()
	t=int(infile.readline())

	#Read number of particles
	infile.readline()
	n=int(infile.readline())

	#Clear garbage lines
	for i in range(0,5,1):
	    infile.readline()

	#Pre-allocate particles array
	xu= numpy.zeros([n,7])
	
	for i in range(0,n,1):
	    numbers=infile.readline()
	    numbers_str=numbers.split()
	    numbers_fl=[float(x) for x in numbers_str]
	    for j in range(0,3,1):
		xu[i][j] = numbers_fl[3+j]

	    for j in range (3,6,1):
		xu[i][j] = numbers_fl[3+j]
    
    infile.close();
    return t, n, xu

#=====================
#   PARTICLES FINDER
#=====================

def findCutZ(xu):
    
    index = numpy.where(xu[:,2] > zCutVal)
    id_xu = xu[index,:]

    return id_xu

#=====================
#   STATISTICS
#=====================
def calcStats(xu):
   
    uMean=numpy.zeros([4])
    for i in range (0,4):
	uMean[i]=numpy.mean(xu[:,i+3])
    
    uStd=numpy.std(xu[:,5])
    uMax=numpy.max(xu[:,5])
    uMin=numpy.min(xu[:,5])
    
    return uMean, uStd, uMax, uMin


#======================
#   MAIN
#======================

os.chdir("./DEM/post") # go to directory
outfile = open(outname,'w')

#outfile.write("t\tu\t v\t w\t unorm\t wStd\t wMax\t wMin\n")
#Extract statistics for all the datafiles from LIGGGHTS
for fname in os.listdir("."): # for all files in current directory
    
    if fname.endswith("liggghts_restart") :
        
	# Get data from file
	[t, n, xu] = readf(fname)

	# Create velocity magnitude data
	xu[:,6] = map(numpy.linalg.norm, xu[:,3:5])

	if (zCut):
	    [id_xu] = findCutZ(xu)
	else:
	    id_xu = xu

	if (id_xu.size>0):
	    if (calcStat):
		[uMean, uStd, uMax, uMin] = calcStats(id_xu)

	    #Print result of local file
	    outfile.write("%i " %t)
	    for i in range(0,4):
		outfile.write("%5.5e " %uMean[i])
	    
	    outfile.write("%5.5e " %uStd)
	    outfile.write("%5.5e " %uMax)
	    outfile.write("%5.5e " %uMin)
	    outfile.write("\n")
outfile.close()

#Reorder data
outfile = open(outname,'r')
N, u,v,w, unorm, wStd, wMax, wMin = numpy.loadtxt(outfile, unpack=True)
outfile.close()

#Sort arrays
indices= N.argsort()
N=N[indices]
u=u[indices]
v=v[indices]
w=w[indices]
unorm=unorm[indices]
wStd=wStd[indices]
wMax=wMax[indices]
wMin=wMin[indices]

#Print ordered results
outfile = open(outname,'w')
for i in range(0,len(N)):
    outfile.write("%5.5e %5.5e %5.5e %5.5e %5.5e %5.5e %5.5e %5.5e\n  " %(N[i], u[i], v[i], w[i], unorm[i], wStd[i], wMax[i],wMin[i]))

outfile.close()
os.chdir("../..") # go to initial directory




