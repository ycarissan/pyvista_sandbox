import numpy as np
import pyvista as pv
from pyvista import examples

# Define some helpers - ignore these and use your own data!
def generate_points(subset=0.02):
    """A helper to make a 3D NumPy array of points (n_points by 3)"""
    dataset = examples.download_lidar()
    ids = np.random.randint(low=0, high=dataset.n_points-1,
                            size=int(dataset.n_points * subset))
    return dataset.points[ids]


def readdata():
    fio = open("grid.csv","r")
    pts = []
    data = []
    for line in fio.readlines()[1:]:
#sepaerator        val = [ float(line.split(",")[i].strip()) for i in range(4) ]
        val = [ float(line.split()[i].strip()) for i in range(4) ]
        pts.append(np.asarray([val[0], val[1], val[2]]))
        data.append(val[3])
    return pts, data

def generate_points(subset=0.02):
    """A helper to make a 3D NumPy array of points (n_points by 3)"""
    dataset = examples.download_lidar()
    ids = np.random.randint(low=0, high=dataset.n_points-1,
                            size=int(dataset.n_points * subset))
    return dataset.points[ids]

# points = generate_points()
# point_cloud = pv.PolyData(points)
# #point_cloud.plot(eye_dome_lighting=True)
# data = points[:,-1]
# point_cloud["elevation"] = data
# point_cloud.plot(render_points_as_spheres=True)





points, data  = readdata()
points = pv.pyvista_ndarray(points)
datac = pv.pyvista_ndarray(data)

point_cloud = pv.PolyData(points)
print("Points uniquement")
point_cloud.plot(eye_dome_lighting=True)
#datac = points[:,-1]
point_cloud["NICS"] = datac
print("Points et valeurs sur des spheres")
point_cloud.plot(render_points_as_spheres=True)

#s = point_cloud.extract_surface()
#s.plot()
#surf = s.delaunay_3d()
#surf.plot()
for i in range(11):
    alpha = 0.1*i
    print("Alpha = ", alpha)
    surf = point_cloud.delaunay_3d(alpha=alpha, tol=0.1, offset=1)
    surf.plot(show_edges=False)





# Create a spatial reference
numPoints = 70
inc = 9.424778 / (numPoints - 1)
x = np.arange(0, numPoints) * inc
y = np.arange(0, numPoints) * inc
xx, yy, _ = np.meshgrid(x, y, [0])
zz = np.sin(np.sqrt(xx*xx + yy*yy))
# Make a PyVista/VTK mesh
surface = pv.StructuredGrid(xx, yy, zz)

# Plot it!
surface.plot(show_edges=True, show_grid=True, notebook=False)

# or save it out for opening in ParaView
surface.save("my_surface.vtk")

x = [ points[i][0] for i in range(len(points)) ]
y = [ points[i][1] for i in range(len(points)) ]
z = [ points[i][2] for i in range(len(points)) ]

