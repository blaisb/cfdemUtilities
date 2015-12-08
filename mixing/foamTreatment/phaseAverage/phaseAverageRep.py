#------------------------------------------------------------------------------------------------------------
#
# This program carries out phase averaging of VTK output variable
# It works with both scalar and vector variables, the name only has to be specified
# In return an averaged file 
# 
#
# Usage : python phaseAverage.py folder outputFile t0 tf
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import os
import sys
from scipy.interpolate import griddata
import sys
import numpy as np
import vtk
from vtk.util import numpy_support


#================================
#   USER DEFINED VARIABLES  
#================================
UsCut=1e-6
muf=0.0516
rhof=1207
dp=0.003

#********************************
# FUNCTIONS
#********************************

def readVTK(reader,fname):
    reader.SetFileName(fname)
    reader.Update()
        
    polydata = reader.GetOutput()
    nodes_vtk_array= polydata.GetPoints().GetData()
    var_vtk_array = polydata.GetCellData().GetArray(0)

    #Get the coordinates of the nodes and their temperatures
    nodes_nummpy_array = numpy_support.vtk_to_numpy(nodes_vtk_array)
    x,y,z= nodes_nummpy_array[:,0] , nodes_nummpy_array[:,1] , nodes_nummpy_array[:,2]

    var_numpy_array = numpy_support.vtk_to_numpy(var_vtk_array)
    return var_numpy_array

       #T = T*100. #
    #C=numpy_support.numpy_to_vtk(T)
    #polydata.GetCellData().SetScalars(C)
    #reader.Update()


#================================
# MAIN
#================================

try:
    folder = sys.argv[1]
    outputFile = sys.argv[2]
    label=sys.argv[3]
    t0=float(sys.argv[4])
    tf=float(sys.argv[5])
except:
    print "**************************************************************************************************"
    print "Insufficient number of arguments, need a probe folder, an output file, name of the file, t0 and tf"
    print "**************************************************************************************************"
    raise

timeFolder=os.listdir(folder)

# Sort so that time will already be sorted
timeFolder.sort() 

reader = vtk.vtkPolyDataReader()

init=False
print "Looping through folder"
n=0

for i in timeFolder:
    if (float(i)>t0 and float(i)<tf) :
        print folder+"/"+i+"/"
        fname=folder+"/"+i+"/"+"U"+label
        dataU=readVTK(reader,fname)
        fname=folder+"/"+i+"/"+"U"+label
        dataUs=readVTK(reader,fname)
        dataInstant=(np.abs(dataUs-dataU))/muf*rhof*dp
        if (init==False):
            occ=np.zeros([np.size(dataInstant,0)])
        occ+=1
        for i in range(0,np.size(dataUs,0)):
            if ((abs(dataUs[i,0]) + abs(dataUs[i,1]) + abs(dataUs[i,2])) <UsCut):
                dataInstant[i,:]=0.
                occ[i]-=1
        if (init==False):
            data=dataInstant
            init=True
        else:
            data+=dataInstant
        n+=1

#Phase summation is complete
print "Phase averaging with N=",n, " samples is completed"
print "Minimal occurance : ", np.min(occ), " \tMaximal occurence : ", np.max(occ)

for i in range(0,np.size(occ)):
    data[i]=data[i]/max(occ[i],1)

reader.Update()
polydata = reader.GetOutput()

C=numpy_support.numpy_to_vtk(data)
polydata.GetCellData().SetScalars(C)
reader.Update()

writer=vtk.vtkPolyDataWriter()
writer.SetFileName(outputFile)
writer.SetFileTypeToASCII()
writer.SetInputConnection(reader.GetOutputPort())
writer.Write()


