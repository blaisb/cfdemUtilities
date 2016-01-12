#------------------------------------------------------------------------------------------------------------
#
# This program carries out phase averaging of VTK output variable
# It works only for the special case of the Particulate Reynolds number and the solid velocity
# This is necessary because they both require special treatment due to the lagrangian nature of the particle
# data
# 
#
# Usage : python phaseAverageRep.py folder outputFile label t0 tf
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import os
import sys
import sys
import numpy as np
import vtk
from vtk.util import numpy_support


#================================
#   USER DEFINED VARIABLES  
#================================
UsCut=1e-5
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
    outputFolder = sys.argv[2]
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
        fname=folder+"/"+i+"/"+"Us"+label
        dataUs=readVTK(reader,fname)
        dataInstant=(np.abs(dataUs-dataU))/muf*rhof*dp
        if (init==False):
            occ=np.zeros([np.size(dataInstant,0)])
        occ+=1
        for j in range(0,np.size(dataUs,0)):
            UsNorm= abs(dataUs[j,0]+dataUs[j,1]+dataUs[j,2])
            if (UsNorm <UsCut):
                dataInstant[j,:]=0.
                occ[j]-=1
        if (init==False):
            acc=dataInstant
            accUs=dataUs
            init=True
        else:
            acc+=dataInstant
            accUs+=dataUs
        n+=1

#Phase summation is complete
print "Phase averaging with N=",n, " samples is completed"
print "Minimal occurance : ", np.min(occ), " \tMaximal occurence : ", np.max(occ), "\tMedian occurence : ", np.median(occ)

for i in range(0,np.size(occ)):
    acc[i]=acc[i]/max(occ[i],1)
    accUs[i]=accUs[i]/max(occ[i],1)

reader.Update()
polydata = reader.GetOutput()

C=numpy_support.numpy_to_vtk(acc)
polydata.GetCellData().SetScalars(C)
reader.Update()

writer=vtk.vtkPolyDataWriter()
writer.SetFileName(outputFolder+"/Rep"+label)
writer.SetFileTypeToASCII()
writer.SetInputConnection(reader.GetOutputPort())
writer.Write()

C=numpy_support.numpy_to_vtk(accUs)
polydata.GetCellData().SetScalars(C)
reader.Update()

writer=vtk.vtkPolyDataWriter()
writer.SetFileName(outputFolder+"Us"+label)
writer.SetFileTypeToASCII()
writer.SetInputConnection(reader.GetOutputPort())
writer.Write()
