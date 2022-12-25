from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

n_angles = 36
n_radii = 8

# 반경의 배열
# 반경 r = 0을 포함하지 않는다. 이것은 중복 점을 제거하기 위한 것이다.
radii = np.linspace(0.125, 1.0, n_radii)

# 각도 배열
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# 각 반경에 대해 모든 각도 반복
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# 극 좌표(반경, 각도)를 직각 좌표 (x, y) 좌표로 변환
# (0, 0)이 여기에 추가된다. (x, y) 점에는 중복 점이 없다.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# 프랭글(pringle) 표현
z = np.sin(-x*y)
fig = plt.figure()

ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)

plt.show()

