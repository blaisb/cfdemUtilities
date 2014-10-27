from paraview.simple import *
import glob
import re

#liste = glob.glob('/home/bruno/CFDEM/bruno-PUBLIC-2.2.1/runv2-6/particle_only/loadingSquare/post/cylinder*.vtk')
liste = glob.glob('./post/couette*.vtk')

#liste.sort()


def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

liste=natural_sort(liste)
#paraview.simple._DisableFirstRenderCameraReset()

#square = LegacyVTKReader( FileNames=[
#'/home/bruno/CFDEM/bruno-PUBLIC-2.2.1/runv2-6/particle_only/loadingSquare/post/square98000.vtk'] )


couette_ = STLReader( FileNames=['./initpost/couette_1000.stl'] )

square=LegacyVTKReader(FileNames=liste)


RenderView1 = GetRenderView()
RenderView1.CameraPosition = [-0.00032399967312812805, -0.0002795010805130005, 0.799224061999444]
RenderView1.CameraClippingRange = [0.5396848694000508, 0.5986885115576086]
RenderView1.CameraFocalPoint = [-0.00032399967312812805, -0.0002795010805130005, 0.23402100056409836]
RenderView1.CameraParallelScale = 0.1462853166497175
RenderView1.CenterOfRotation = [-0.00032399967312812805, -0.0002795010805130005, 0.23402100056409836]

DataRepresentation1 = Show()
DataRepresentation1.ConstantRadius = 0.00025
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
