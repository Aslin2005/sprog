import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL('./lib.so')
lib.LUsolver.argtypes = [ctypes.c_int]
lib.LUsolver.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_float))

# Define the system of equations
x = np.linspace(-10, 10, 1000)

# Equation 1: 
y1 = (9 - 8*x)/5

# Equation 2: 
y2 =  (4 - 3*x)/2

# Solve using LU decomposition
solution = lib.LUsolver(2)

# Extract the solution values for x and y
x_sol = solution[0][0]
y_sol = solution[1][0]
print("x = ",x_sol,",y = ",y_sol)

# Plot the lines
plt.plot(x, y1, color='red', label="8x + 5y = 9")
plt.plot(x, y2, color='blue', label="3x + 2y = 4")

# Plot the solution as a point
plt.scatter(x_sol, y_sol, color='green', label='Solution')
plt.text(x_sol, y_sol + 1, f'({x_sol:.2f}, {y_sol:.2f})', color='black', ha='center')

# Plot settings
plt.xlabel("x")
plt.ylabel("y")
plt.title("System of Linear Equations")
plt.grid(True)
plt.legend()
plt.savefig("../figure/fig.png")
plt.show()
