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
    fio = open("tmp.csv","r")
    pts = []
    data = []
    for line in fio.readlines():
        val = [ float(line.split(",")[i].strip()) for i in range(4) ]
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
point_cloud.plot(eye_dome_lighting=True)
#datac = points[:,-1]
point_cloud["elevation"] = datac
point_cloud.plot(render_points_as_spheres=True)

