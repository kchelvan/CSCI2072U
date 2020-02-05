# Keshopan Arunthavachelvan
# 100694939
# January 21, 2020
# Assignment One Part One

def recursion(x0, f, df, tolerance, max_iterations, iteration = 0, residual = None, error = None):
    '''
    Description: Calculates solution of iterations using Newton's method with using recursion

    Parameters
    x0: initial point
    f: function that is being used for iteration (residual)
    df: derivative of the function f
    tolerance: lower bound for when the iteration should terminate (estimated error)
    max_iterations: maximum number of iterations
    iteration: current iteration counter
    '''
    # Instantiates the current node with the first point
    cur_node = float(x0)
    if (residual == None or error == None):
        residual = f
        error = f(x0)
    # Iterates until the maximum number of iterations is exceeded or the current node is less than the tolerance value
    if (iteration < max_iterations):
         # If current node is less than the tolerance, print the current solution and return the current node
        if (abs(f(cur_node)) < tolerance):
            print("Found solution of " + str(cur_node) + " at the " + str(iteration) + "th iteration.")
            print("The estimated error is " + str(abs(error - cur_node)) + " and the residual is " + str(residual(x0)))
            return cur_node
        
        # increases iteration counter by one
        iteration += 1
        # recursively calls function to perform newton's method to find solution
        cur_node = recursion(cur_node - float(f(cur_node))/float(df(cur_node)), f, df, tolerance, max_iterations, iteration, residual, error )
    else:
        # If current iteration exceeds maximum number of iterations, print the current solution and return null
        print('Next iteration exceeds maximum number of iterations. Current solution is ' + str(cur_node) + ". \nDoes not Converge.")
        return None
