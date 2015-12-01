from scipy.interpolate import griddata
import sys
import numpy as np
import vtk
from vtk.util import numpy_support

reader = vtk.vtkPolyDataReader()
reader.SetFileName(sys.argv[1])
reader.Update()

polydata = reader.GetOutput()
nodes_vtk_array= polydata.GetPoints().GetData()

#The "Temperature" field is the third scalar in my vtk file
temperature_vtk_array = polydata.GetCellData().GetArray(0)

#Get the coordinates of the nodes and their temperatures
nodes_nummpy_array = numpy_support.vtk_to_numpy(nodes_vtk_array)
x,y,z= nodes_nummpy_array[:,0] , nodes_nummpy_array[:,1] , nodes_nummpy_array[:,2]

temperature_numpy_array = numpy_support.vtk_to_numpy(temperature_vtk_array)
T = temperature_numpy_array
T = T*100. #
C=numpy_support.numpy_to_vtk(T)
polydata.GetCellData().SetScalars(C)
reader.Update()

writer=vtk.vtkPolyDataWriter()
writer.SetFileName("test.vtk")
writer.SetFileTypeToASCII()
writer.SetInputConnection(reader.GetOutputPort())
writer.Write()
