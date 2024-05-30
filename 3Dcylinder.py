from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

# Get radius and height from the user
R_outer = float(input("Enter the outer radius of the cylinder in cm: "))
R_inner = float(input("Enter the inner radius of the cylinder in cm: "))
H = float(input("Enter the height of the cylinder in cm: "))

# Define the variables
r, theta, z = sp.symbols('r theta z')

# Define the integrand for the volume in cylindrical coordinates
integrand = r

# Integrate in cylindrical coordinates for the outer cylinder
inner_integral_outer = sp.integrate(integrand, (r, R_inner, R_outer))
display(inner_integral_outer)

middle_integral_outer = sp.integrate(inner_integral_outer, (theta, 0, 2*sp.pi))
display(middle_integral_outer)

volume_integral_outer = sp.integrate(middle_integral_outer, (z, 0, H))
display(volume_integral_outer)

# Calculate the numerical value
volume_value = volume_integral_outer.evalf()
print(f"The volume of the hollow cylinder with outer radius {R_outer} cm, inner radius {R_inner} cm, and height {H} cm is approximately {volume_value:.2f} cubic centimeters.")

# Plotting the hollow cylinder
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the outer surface of the cylinder
z = np.linspace(0, H, 100)
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, z_grid = np.meshgrid(theta, z)
x_grid_outer = R_outer * np.cos(theta_grid)
y_grid_outer = R_outer * np.sin(theta_grid)

# Define the inner surface of the cylinder
x_grid_inner = R_inner * np.cos(theta_grid)
y_grid_inner = R_inner * np.sin(theta_grid)

# Plot the outer surface
ax.plot_surface(x_grid_outer, y_grid_outer, z_grid, alpha=0.7, rstride=5, cstride=5, color='dimgrey')

# Plot the inner surface
ax.plot_surface(x_grid_inner, y_grid_inner, z_grid, alpha=0.7, rstride=5, cstride=5, color='red')

# Set labels
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Z (cm)')
ax.set_title('')

# Set axis limits
ax.set_xlim([-R_outer, R_outer])
ax.set_ylim([-R_outer, R_outer])
ax.set_zlim([0, H])

plt.show()
