#------------------------------------------------------------------------------------------------------------
#
# This program renames the vtk plane and slice files and put them in order sequentially to be open in 
# paraview
# 
#
# Usage : python FOLDERNAM
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import os
import sys
import numpy
import math
import matplotlib.pyplot as plt
import shutil
#----------------


#================================
#   MAIN
#================================

folder=sys.argv[1]
timeFolder=os.listdir(folder)

# Sort so that time will already be sorted
timeFolder.sort() 


# Loop through all times
print "Looping through folder"
k=0
for i in timeFolder:
    print i, k
    for j in os.listdir(folder+"/"+i):
        shutil.move(folder+"/"+str(i)+"/"+j,folder+j[:-4]+"_"+str(k)+j[-4:])
    k+=1

print "Post-processing over"

