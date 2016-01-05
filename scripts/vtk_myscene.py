import vtk

def getImageDataMapper():

    imageData = vtk.vtkImageData()
    imageData.SetDimensions(3, 3, 3)
    imageData.SetSpacing(1., 1., 1.)
    imageData.SetOrigin(0., 0., 0.)

    mapper = vtk.vtkDataSetMapper()

    mapper.SetInputData(imageData)


def getSphereActor():
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetRadius(0.7)
    sphereSource.SetThetaResolution(50)
    sphereSource.SetPhiResolution(50)

    mapper = vtk.vtkPolyDataMapper()

    mapper.SetInputConnection(sphereSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0, 1, 0)

    return actor

def getCubeActor():
    cubeSource = vtk.vtkCubeSource()
    cubeSource.SetBounds(-1, 1, -1, 1, -1, 1)
    mapper =  vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cubeSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.GetProperty().SetOpacity(0.5)
    actor.GetProperty().SetColor(1, 0, 0)
    actor.SetMapper(mapper)

    return actor

renderer = vtk.vtkRenderer()

source = vtk.vtkPlaneSource()
z = 0.6
source.SetOrigin(0, 0, z)
source.SetPoint1(3, 0, z)
source.SetPoint2(0, 3, z)
source.SetCenter(0, 0, z)
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(source.GetOutputPort())
actor = vtk.vtkActor()
actor.SetMapper(mapper)




sphereActor = getSphereActor()
cubeActor = getCubeActor()
renderer.AddActor(sphereActor)
renderer.AddActor(cubeActor)
renderer.AddActor(actor)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
iren.Initialize()
iren.Start()




# actor = vtk.vtkActor()

# actor.GetProperty().SetColor(1.0, 0.0, 0.0)

# actor.SetMapper(mapper)
# #actor.GetProperty().SetRepresentationToWireframe()

# renderer = vtk.vtkRenderer()

# source = vtk.vtkSphereSource()
# source.SetCenter(0, 0, 0)
# source.SetRadius(5)
# map2 = vtk.vtkPolyDataMapper()
# map2.SetInputConnection(source.GetOutputPort())

# renderer.AddActor(actor)

# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(renderer)

# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)
# iren.Initialize()
# iren.Start()
