from paraview.simple import *
import glob
import re

opacityBaffles=0.6
opacityImpeller=1.0
opacityTank=0.2

liste = glob.glob('./post/VTK/mixer_*.vtk')
listeImpl = glob.glob('./post/VTK/impeller_*.stl')
listeTank = glob.glob('/home/bruno/cfdem/run/mesh/PBT_Manon/tank.stl')
listeBafflesB = glob.glob('/home/bruno/cfdem/run/mesh/PBT_Manon/baffles/baffB.stl')
listeBafflesF = glob.glob('/home/bruno/cfdem/run/mesh/PBT_Manon/baffles/baffF.stl')
listeBafflesL = glob.glob('/home/bruno/cfdem/run/mesh/PBT_Manon/baffles/baffL.stl')
listeBafflesR = glob.glob('/home/bruno/cfdem/run/mesh/PBT_Manon/baffles/baffR.stl')

# Function to sort the files in a natural fashion
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

liste=natural_sort(liste)
listeImpl=natural_sort(listeImpl)

# LOAD THE IMPELLER
impeller=STLReader(FileNames=listeImpl)

#GetActiveSource()
DataRepresentation1 = Show()
DataRepresentation1.SelectionPointFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.SelectionCellFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.ColorArrayName = ('CELL_DATA', '')
DataRepresentation1.ScaleFactor = 0.02920000106096268

STLReader2 = FindSource( "STLReader2" )
my_representation0 = GetDisplayProperties( STLReader2 )
RenameSource("Impeller", STLReader2)

# LOAD THE TANK

tank=STLReader(FileNames=listeTank)

STLReader2 = GetActiveSource()
RenderView1 = GetRenderView()
DataRepresentation1 = Show()
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.SelectionPointFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.SelectionCellFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.ColorArrayName = ('CELL_DATA', 'STLSolidLabeling')
DataRepresentation1.ScaleFactor = 0.03650000095367432

DataRepresentation2 = GetDisplayProperties( STLReader2 )
DataRepresentation2.Opacity = opacityTank
DataRepresentation2.ColorArrayName = ('CELL_DATA', '')
RenameSource("Tank", STLReader2)

#PARTICLES

square=LegacyVTKReader(FileNames=liste)

RenderView1 = GetRenderView()
RenderView1.CameraPosition = [-0.00032399967312812805, -0.0002795010805130005, 0.799224061999444]
RenderView1.CameraClippingRange = [0.5396848694000508, 0.5986885115576086]
RenderView1.CameraFocalPoint = [-0.00032399967312812805, -0.0002795010805130005, 0.23402100056409836]
RenderView1.CameraParallelScale = 0.1462853166497175
RenderView1.CenterOfRotation = [-0.00032399967312812805, -0.0002795010805130005, 0.23402100056409836]

DataRepresentation1 = Show()
DataRepresentation1.ConstantRadius = 0.0015
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.SelectionPointFieldDataArrayName = 'f'
DataRepresentation1.SelectionCellFieldDataArrayName = 'radius'
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'radius')
DataRepresentation1.Texture = []
DataRepresentation1.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation1.Representation = 'Point Sprite'
DataRepresentation1.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation1.RadiusRange = [-0.10308, 0.102432]
DataRepresentation1.ScaleFactor = 0.020727699995040896

a1_radius_PVLookupTable = GetLookupTableForArray( "radius", 1, RGBPoints=[0.004000000189989805, 0.0, 0.0, 1.0, 0.004000000189989905, 1.0, 0.0, 0.0], VectorMode='Component', NanColor=[0.498039, 0.498039, 0.498039], ColorSpace='HSV', ScalarRangeInitialized=1.0 )

a1_radius_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.004000000189989805, 0.0, 0.5, 0.0, 0.004000000189989905, 1.0, 0.5, 0.0] )

Render()

# LOAD THE BAFFLES one by one..
# R Baffle

bafflesR=STLReader(FileNames=listeBafflesR)

STLReader3 = GetActiveSource()
DataRepresentation2 = GetDisplayProperties( STLReader3 )
DataRepresentation2.Opacity = opacityBaffles
DataRepresentation2.ColorArrayName = ('CELL_DATA', '')
RenameSource("BaffR", STLReader3)

##PARTICLES

square=LegacyVTKReader(FileNames=liste)

RenderView1 = GetRenderView()
RenderView1.CameraPosition = [-0.00032399967312812805, -0.0002795010805130005, 0.799224061999444]

## L Baffle

bafflesL=STLReader(FileNames=listeBafflesL)

STLReader4 = GetActiveSource()
DataRepresentation2 = GetDisplayProperties( STLReader4 )
DataRepresentation2.Opacity = opacityBaffles
DataRepresentation2.ColorArrayName = ('CELL_DATA', '')

# F baffle

bafflesF=STLReader(FileNames=listeBafflesF)

STLReader5 = GetActiveSource()
DataRepresentation2 = GetDisplayProperties( STLReader5 )
DataRepresentation2.Opacity = opacityBaffles
DataRepresentation2.ColorArrayName = ('CELL_DATA', '')

# B baffle

bafflesB=STLReader(FileNames=listeBafflesB)

STLReader6 = GetActiveSource()
DataRepresentation2 = GetDisplayProperties( STLReader6 )
DataRepresentation2.Opacity = opacityBaffles
DataRepresentation2.ColorArrayName = ('CELL_DATA', '')
