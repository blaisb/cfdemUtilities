from paraview.simple import *
import glob
import re

#liste = glob.glob('/home/bruno/CFDEM/bruno-PUBLIC-2.2.1/runv2-6/particle_only/loadingSquare/post/cylinder*.vtk')
liste = glob.glob('./post/VTK/mixer_*.vtk')
listeImpl = glob.glob('./post/VTK/impeller_*.stl')
listeTank=glob.glob('/home/bruno/doctorat/mesh/PBT_Manon/tank.stl')
#liste.sort()


def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

liste=natural_sort(liste)
listeImpl=natural_sort(listeImpl)
#paraview.simple._DisableFirstRenderCameraReset()

# LOAD THE IMPELLER
impeller=STLReader(FileNames=listeImpl)

GetActiveSource()
DataRepresentation1 = Show()
DataRepresentation1.ConstantRadius = 0.08254999667406082
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.PointSpriteDefaultsInitialized = 1
DataRepresentation1.SelectionPointFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.SelectionCellFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.ColorArrayName = ('CELL_DATA', '')
DataRepresentation1.Texture = []
DataRepresentation1.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation1.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation1.RadiusRange = [-0.08255, 0.08255]
DataRepresentation1.ScaleFactor = 0.02920000106096268
DataRepresentation1.ColorAttributeType = 'CELL_DATA'

STLReader2 = FindSource( "STLReader2" )

my_representation0 = GetDisplayProperties( STLReader2 )

LegacyVTKReader1 = GetActiveSource()

my_representation1 = GetDisplayProperties( LegacyVTKReader1 )

a1_STLSolidLabeling_PiecewiseFunction = CreatePiecewiseFunction( Points=[-0.0333544984459877, 0.0, 0.5, 0.0, 0.0251924991607666, 1.0, 0.5, 0.0] )

a1_STLSolidLabeling_PVLookupTable = GetLookupTableForArray( "STLSolidLabeling", 1 )



# LOAD THE TANK

tank=STLReader(FileNames=listeTank)

STLReader2 = GetActiveSource()

RenderView1 = GetRenderView()
RenderView1.CameraPosition = [0.0, 0.0, 1.4038138401361357]
RenderView1.CameraClippingRange = [0.8459256875250272, 1.6967960548430514]
RenderView1.CameraFocalPoint = [0.0, 0.0, 0.18250000476837158]
RenderView1.CameraParallelScale = 0.31609928064038195
RenderView1.CenterOfRotation = [0.0, 0.0, 0.18250000476837158]

DataRepresentation1 = Show()
DataRepresentation1.ConstantRadius = 0.18250000476837158
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation1.PointSpriteDefaultsInitialized = 1
DataRepresentation1.SelectionPointFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.SelectionCellFieldDataArrayName = 'STLSolidLabeling'
DataRepresentation1.ColorArrayName = ('CELL_DATA', 'STLSolidLabeling')
DataRepresentation1.Texture = []
DataRepresentation1.AmbientColor = [0.0, 0.0, 0.0]
DataRepresentation1.CubeAxesColor = [0.0, 0.0, 0.0]
DataRepresentation1.RadiusRange = [-0.1825, 0.1825]
DataRepresentation1.ScaleFactor = 0.03650000095367432
DataRepresentation1.ColorAttributeType = 'CELL_DATA'

a1_STLSolidLabeling_PVLookupTable = GetLookupTableForArray( "STLSolidLabeling", 1, RGBPoints=[0.0, 0.0, 0.0, 1.0, 1e-16, 1.0, 0.0, 0.0], VectorMode='Component', NanColor=[0.498039, 0.498039, 0.498039], ColorSpace='HSV', ScalarRangeInitialized=1.0 )

a1_STLSolidLabeling_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1e-16, 1.0, 0.5, 0.0] )

DataRepresentation2 = GetDisplayProperties( STLReader2 )
DataRepresentation2.Opacity = 0.2
DataRepresentation2.ColorArrayName = ('CELL_DATA', '')





#Next
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
DataRepresentation1.PointSpriteDefaultsInitialized = 1
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
