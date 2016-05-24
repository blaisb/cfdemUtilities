#------------------------------------------------------------------------------------------------------------
#
# This program carries out line sampling of a phase averaged VTK file
# It returns the value of the void fraction on a line 
# 
#
# Usage : python phaseAverage.py folder outputFile label t0 tf
#
# Author : Bruno Blais
#
#-------------------------------------------------------------------------------------------------------------

# Python imports
#----------------
import numpy as np
from vtk.util import numpy_support 
from matplotlib import pyplot as plt
import vtk
import sys

#********************************
# FUNCTIONS
#********************************

def readVTK(filename):
    #read the vtk file with an unstructured grid
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    return reader

def createLine(p1,p2,numPoints):
    # Create the line along which you want to sample
    line = vtk.vtkLineSource()
    line.SetResolution(numPoints)
    line.SetPoint1(p1)
    line.SetPoint2(p2)
    line.Update()
    return line

def probeOverLine(line,reader):
    #Interpolate the data from the VTK-file on the created line.
    data = reader.GetOutput()
    # vtkProbeFilter, the probe line is the input, and the underlying dataset is the source.
    probe = vtk.vtkProbeFilter()
    probe.SetInputConnection(line.GetOutputPort())
    probe.SetSource(data)
    probe.Update()
    #get the data from the VTK-object (probe) to an numpy array
    q=numpy_support.vtk_to_numpy(probe.GetOutput().GetPointData().GetArray('scalars'))
    numPoints = probe.GetOutput().GetNumberOfPoints() # get the number of points on the line
    #intialise the points on the line    
    x = np.zeros(numPoints)
    y = np.zeros(numPoints)
    z = np.zeros(numPoints)
    points = np.zeros((numPoints , 3))
    #get the coordinates of the points on the line
    for i in range(numPoints):
        x[i],y[i],z[i] = probe.GetOutput().GetPoint(i)
        points[i,0]=x[i]
        points[i,1]=y[i]
        points[i,2]=z[i]
    return points,q

def setZeroToNaN(array):
    # In case zero-values in the data, these are set to NaN.
    array[array==0]=np.nan
    return array

#Define the filename of VTK file
filename=sys.argv[1]

#Set the points between which the line is constructed.
#p1=[0.0,0.,0.065]
#p2=[0.1825,0.,0.065]
p1=[0.0,0.,0.0010]
p2=[0.1825,0.,0.0010]

#Define the numer of interpolation points
numPoints=20005

ptLine=np.linspace(0,np.linalg.norm(np.asarray(p2)-np.asarray(p1)),numPoints+1)


reader = readVTK(filename) # read the VTKfile
#reader = vtk.vtkPolyDataReader()
#reader.SetFileName(filename)
#reader.Update()
        
polydata = reader.GetOutput()


line=createLine(p1,p2,numPoints) # Create the line
points,U =  probeOverLine(line,reader) # interpolate the data over the line

U = setZeroToNaN(U) # Set the zero's to NaN's
plt.plot(ptLine,U[:],'-*') #plot the data
plt.show()
