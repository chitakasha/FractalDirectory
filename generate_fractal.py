# Import libraries
import math
import matplotlib.pyplot as plt

# Define parameters
theta = math.pi / 4 # Angle of rotation
c = 0 # Constant
z = 1 # Initial value of complex number
n = 1000 # Number of iterations

# Define function that applies quantum spiral formula
def f(z):
    return math.e ** (1j * theta) * z + c

# Initialize lists to store real and imaginary parts of complex numbers
x = []
y = []

# Use loop to apply function and generate sequence of complex numbers
for i in range(n):
    # Append real and imaginary parts to lists
    x.append(z.real)
    y.append(z.imag)
    # Apply function to current value of z
    z = f(z)

# Plot sequence of complex numbers on plane
plt.plot(x, y)
plt.show()
