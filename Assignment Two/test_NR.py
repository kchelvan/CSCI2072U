# Keshopan Arunthavachelvan
# 100694939
import numpy as np
from NR import *

# Constructs the three equations
def f(x):
    y = np.zeros((3, 1))
    y[0] = -(x[1]**2) - x[2]**2 - (1/4)*x[0] + 2
    y[1] = x[0]*x[1] - 4*x[0]*x[2] - x[1] + 1
    y[2] = 4*x[0]*x[1] + x[0]*x[2] - x[2]
    return y

# Creates a 3x3 array to define the Jacobian of the fucntion in f(x)
def Df(x):
    jacobian = np.zeros((3, 3))
    jacobian[0,0] = -1/4
    jacobian[0,1] = -2 * x[1]
    jacobian[0,2] = -2 * x[2]
    jacobian[1,0] = x[1] - 4*x[2]
    jacobian[1,1] = x[0] - 1
    jacobian[1,2] = -4 * x[0]
    jacobian[2,0] = 4*x[1] + x[2]
    jacobian[2,1] = 4 * x[0]
    jacobian[2,2] = x[0] - 1
    return jacobian

# Variable Declaration
x = np.zeros((3, 1))
x[0] = 7
x[1] = 0
x[2] = 0

# Computes the Newton-Raphson Iteration
x, error, residual = NR(x, f, Df, 0.00001, 0.00001, 15)