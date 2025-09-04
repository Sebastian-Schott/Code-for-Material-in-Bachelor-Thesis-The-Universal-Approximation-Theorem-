import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator

# Parameters for the cylinder
theta_res = 50       # resolution around the circle
z_res = 50           # resolution along the height
radius = 1.0         # unit radius in x1-x2 plane
height = 1.0         # height along x3-axis

# Create the mesh for the curved surface
theta = np.linspace(0, 2 * np.pi, theta_res)
z = np.linspace(0, height, z_res)
Theta, Z = np.meshgrid(theta, z)
X = radius * np.cos(Theta)
Y = radius * np.sin(Theta)

# Set random seed for reproducibility
np.random.seed(40)

# Generate random points on the curved surface
num_points = 70
theta_rand = np.random.uniform(0, 2 * np.pi, num_points)
z_rand = np.random.uniform(0, height, num_points)
X_rand = radius * np.cos(theta_rand)
Y_rand = radius * np.sin(theta_rand)
Z_rand = z_rand


fig = plt.figure(figsize=(10, 12))
ax = fig.add_subplot(111, projection='3d')

# Plot the transparent curved surface in red (more transparent)
ax.plot_surface(X, Y, Z, color='red', alpha=0.15, linewidth=0, shade=False)

# Plot the random points on the surface
ax.scatter(X_rand, Y_rand, Z_rand, color='red', s=30)

ax.view_init(elev=22, azim=20)

# Adjust axis limits to be 1.5 times larger, cylinder height remains between 0 and 1
ax.set_xlim(-1.5 * radius, 1.5 * radius)
ax.set_ylim(-1.5 * radius, 1.5 * radius)
ax.set_zlim(0, 1.2 * height)

# Labels and aspect ratio
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')

# Reduce number of ticks on each axis for clarity
ax.xaxis.set_major_locator(MaxNLocator(4))
ax.yaxis.set_major_locator(MaxNLocator(4))
ax.zaxis.set_major_locator(MaxNLocator(4))

plt.savefig("manifold.svg", format='svg', bbox_inches='tight', pad_inches=0.2)
plt.close()
#plt.show()
