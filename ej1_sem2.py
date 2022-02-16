import open3d as o3d
import numpy as np
import copy

points = []
for i in range(100):
	for j in range(100):
		points.append([i,j,0])
		
suelo = o3d.geometry.PointCloud()
suelo.points = o3d.utility.Vector3dVector(np.array(points))

techo = copy.deepcopy(suelo).translate((50,50,100), relative=False)

R = suelo.get_rotation_matrix_from_xyz((0,-np.pi/2,0))
pared1 = copy.deepcopy(suelo).rotate(R,center=(0,0,0))

pared2 = copy.deepcopy(pared1).translate((100,50,50),relative=False)

R = techo.get_rotation_matrix_from_xyz((0,-2*np.pi/6,0))
tejado1 = copy.deepcopy(techo).rotate(R,center=(0,0,100))

R = techo.get_rotation_matrix_from_xyz((0,2*np.pi/6,0))
tejado2 = copy.deepcopy(techo).rotate(R,center=(100,0,100))

R = pared1.get_rotation_matrix_from_xyz((0,0,np.pi/2))
pared3 = copy.deepcopy(pared1).rotate(R,center=(50,50,0))

pared4 = copy.deepcopy(pared3).translate((50,100,50),relative=False)

# Mostrar nube de puntos
#o3d.visualization.draw_geometries([suelo,techo,pared1,pared2,pared3,pared4,tejado1,tejado2])

pcd = o3d.io.read_point_cloud("TUT_O3D/cloud_291.pcd")
# Mostrar nube
o3d.visualization.draw_geometries([pcd])