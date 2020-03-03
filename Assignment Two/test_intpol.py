# Keshopan Arunthavachelvan
# 100694939
import numpy as np
import matplotlib.pyplot as plt

def vandermonde_matrix():
    # Constructs Matix for V
    V = np.zeros((4, 4))
    V[0] = [1, -1.2, 1.44, -1.728]
    V[1] = [1, 0.5, 0.25, 0.125]
    V[2] = [1, 2.2, 4.84, 10.648]
    V[3] = [1, 3.1, 9.61, 29.791]

    # Constructs Matix for Y
    Y = np.array([-0.4, 1.2, 5.5, 10.2])
    
    # Solves the linear system using the V and Y matricies
    A = np.linalg.solve(V, Y)

    # Returns the solution for the A values and the V and Y matricies
    return V, A, Y

V, A, Y = vandermonde_matrix()
print("V: \n", V)
print("X: \n", A)
print("A: \n", Y)