from sympy import symbols, integrate, pi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the variables
x, y, z = symbols('x y z', real=True, positive=True)
R = symbols('R', real=True, positive=True)  # Radius of the sphere
h, r = symbols('h r', real=True, positive=True)  # Height and base radius of the cylinder
a, b, c = symbols('a b c', real=True, positive=True)  # Length, width, and height of the rectangular prism

# Input the shape from the user
shape = input("Choose a 3-D shape to calculate volume (sphere/cylinder/rectangular prism): ")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

if shape.lower() == 'sphere':
    # Input the radius from the user
    radius_input = float(input("Enter the radius of the sphere: "))
    R_value = radius_input

    # Define the integrand for the sphere
    integrand = 1

    # Perform the triple integral for the sphere
    volume = integrate(integrand, (x, -R_value, R_value), (y, -R_value, R_value), (z, -R_value, R_value))

    # Print the symbolic steps
    print("\nSymbolic Steps for Sphere:")
    print("Volume = ∭dV")
    print("       = ∭1 dV")
    print(f"       = ∫(x=-{R_value})^{R_value} ∫(y=-{R_value})^{R_value} ∫(z=-{R_value})^{R_value} 1 dx dy dz")
    print(f"       = ∫(x=-{R_value})^{R_value} ∫(y=-{R_value})^{R_value} {2*R_value} dz dy")
    print(f"       = ∫(x=-{R_value})^{R_value} {2*R_value} dy")
    print(f"       = {2*R_value} * {2*R_value} * {2*R_value}")
    print(f"       = {volume}")

    # Plotting the sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = R_value * np.outer(np.cos(u), np.sin(v))
    y = R_value * np.outer(np.sin(u), np.sin(v))
    z = R_value * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='b', alpha=0.5)

elif shape.lower() == 'cylinder':
    # Input the height and base radius from the user
    height_input = float(input("Enter the height of the cylinder: "))
    radius_input = float(input("Enter the base radius of the cylinder: "))
    h_value = height_input
    r_value = radius_input

    # Define the integrand for the cylinder
    integrand = 1

    # Perform the triple integral for the cylinder
    volume = integrate(integrand, (x, -r_value, r_value), (y, -r_value, r_value), (z, 0, h_value))

    # Print the symbolic steps
    print("\nSymbolic Steps for Cylinder:")
    print("Volume = ∭dV")
    print("       = ∭1 dV")
    print(f"       = ∫(x=-{r_value})^{r_value} ∫(y=-{r_value})^{r_value} ∫(z=0)^{h_value} 1 dx dy dz")
    print(f"       = ∫(x=-{r_value})^{r_value} ∫(y=-{r_value})^{r_value} {h_value} dz dy")
    print(f"       = ∫(x=-{r_value})^{r_value} {h_value} dy")
    print(f"       = {h_value} * {2*r_value} * {2*r_value}")
    print(f"       = {volume}")

    # Plotting the cylinder
    u = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, h_value, 100)
    U, Z = np.meshgrid(u, z)
    X = r_value * np.cos(U)
    Y = r_value * np.sin(U)

    ax.plot_surface(X, Y, Z, color='r', alpha=0.5)

elif shape.lower() == 'rectangular prism':
    # Input the dimensions from the user
    length_input = float(input("Enter the length of the rectangular prism: "))
    width_input = float(input("Enter the width of the rectangular prism: "))
    height_input = float(input("Enter the height of the rectangular prism: "))
    a_value = length_input
    b_value = width_input
    c_value = height_input

    # Define the integrand for the rectangular prism
    integrand = 1

    # Perform the triple integral for the rectangular prism
    volume = integrate(integrand, (x, -a_value/2, a_value/2), (y, -b_value/2, b_value/2), (z, -c_value/2, c_value/2))

    # Print the symbolic steps
    print("\nSymbolic Steps for Rectangular Prism:")
    print("Volume = ∭dV")
    print("       = ∭1 dV")
    print(f"       = ∫(x=-{a_value/2})^{a_value/2} ∫(y=-{b_value/2})^{b_value/2} ∫(z=-{c_value/2})^{c_value/2} 1 dx dy dz")
    print(f"       = ∫(x=-{a_value/2})^{a_value/2} ∫(y=-{b_value/2})^{b_value/2} {c_value} dz dy")
    print(f"       = ∫(x=-{a_value/2})^{a_value/2} {c_value} dy")
    print(f"       = {c_value} * {a_value} * {b_value}")
    print(f"       = {volume}")

    # Plotting the rectangular prism
    X, Y = np.meshgrid(np.linspace(-a_value/2, a_value/2, 100), np.linspace(-b_value/2, b_value/2, 100))
    Z = np.ones_like(X) * (-c_value/2)

    ax.plot_surface(X, Y, Z, color='g', alpha=0.5)
    ax.plot_surface(X, Y, Z + c_value, color='g', alpha=0.5)


else:
    print("Invalid shape chosen. Please choose either 'sphere', 'cylinder', or 'rectangular prism'.")

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set title
ax.set_title(f'{shape.capitalize()} Model')

plt.show()
